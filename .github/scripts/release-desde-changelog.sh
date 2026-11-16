#!/usr/bin/env bash
# Crea la release de GitHub de un tag vX.Y.Z con las notas de su sección del CHANGELOG.
#
# Uso:  .github/scripts/release-desde-changelog.sh vX.Y.Z
#       SOLO_REVISAR=1 .github/scripts/release-desde-changelog.sh vX.Y.Z   (no crea nada)
#
# Lo corre .github/workflows/release.yml. El proceso completo está en .github/RELEASE.md.
# Licencia MIT (ver LICENSE).
set -euo pipefail

falla() {
  echo "::error::$*" >&2
  exit 1
}

tag="${1:-}"
[ -n "$tag" ] || falla "Falta el tag. Uso: $0 vX.Y.Z"

raiz="$(git rev-parse --show-toplevel)"
cd "$raiz"
changelog="$raiz/CHANGELOG.md"

# --- 1. El tag -------------------------------------------------------------

[[ "$tag" =~ ^v([0-9]+\.[0-9]+\.[0-9]+)$ ]] \
  || falla "El tag «$tag» no tiene la forma vX.Y.Z (por ejemplo v0.8.0)."
version="${BASH_REMATCH[1]}"

git rev-parse -q --verify "refs/tags/$tag" >/dev/null \
  || falla "El tag $tag no existe. Crealo en el commit que cierra la versión: git tag -a $tag -m \"$tag · Título\" && git push origin $tag"

if [ "$(git cat-file -t "refs/tags/$tag")" != "tag" ]; then
  commit="$(git rev-parse "$tag^{commit}")"
  falla "El tag $tag es liviano y tiene que ser anotado. Rehacelo sobre el mismo commit: git tag -d $tag && git tag -a $tag -m \"$tag · Título\" $commit && git push --force origin $tag"
fi

git fetch --quiet origin main
git merge-base --is-ancestor "$tag^{commit}" origin/main \
  || falla "El tag $tag apunta a un commit que no está en origin/main. Mergeá el PR de la versión, actualizá main y poné el tag ahí: git tag -a $tag -m \"$tag · Título\" origin/main"

# --- 2. La sección del CHANGELOG -------------------------------------------

[ -f "$changelog" ] || falla "No encuentro CHANGELOG.md en $raiz."

encabezado="$(tr -d '\r' < "$changelog" | grep -m1 -F "## $version — " || true)"
[ -n "$encabezado" ] \
  || falla "CHANGELOG.md no tiene la sección «## $version — AAAA-MM-DD · Título». Versioná «Sin publicar» en el PR antes de poner el tag."

case "$encabezado" in
  *" · "*) titulo="${encabezado#* · }" ;;
  *) titulo="" ;;
esac
titulo="$(printf '%s' "$titulo" | sed 's/[[:space:]]*$//')"
[ -n "$titulo" ] \
  || falla "La sección de $version en CHANGELOG.md no tiene título. El encabezado tiene que ser «## $version — AAAA-MM-DD · Título»."

# Las líneas entre el encabezado y el próximo "## ", sin blancos al principio ni al final.
notas="$(tr -d '\r' < "$changelog" | awk -v enc="$encabezado" '
  dentro && /^## / { exit }
  dentro { print }
  $0 == enc { dentro = 1 }
' | sed -e '/./,$!d' | sed -e ':a' -e '/^\n*$/{$d;N;ba' -e '}')"
[ -n "$notas" ] || falla "La sección de $version en CHANGELOG.md está vacía."

# --- 3. Link de comparación y si es la última ------------------------------

repo="$(gh repo view --json nameWithOwner -q .nameWithOwner 2>/dev/null || true)"
if [ -z "$repo" ]; then
  remoto="$(git remote get-url origin)"
  repo="$(printf '%s' "$remoto" | sed -E 's#^(https://github\.com/|git@github\.com:)##; s#\.git$##')"
fi
[[ "$repo" =~ ^[^/]+/[^/]+$ ]] || falla "No pude sacar owner/repo del remote ni de gh repo view."

anterior="$(git describe --tags --abbrev=0 --match 'v*.*.*' "$tag^" 2>/dev/null || true)"
if [ -n "$anterior" ]; then
  notas="$notas

**Cambios completos:** https://github.com/$repo/compare/$anterior...$tag"
fi

mas_alta="$(git tag -l 'v*.*.*' | sort -V | tail -1)"
if [ "$tag" = "$mas_alta" ]; then ultima=true; else ultima=false; fi

titulo_release="$tag · $titulo"

# --- 4. Revisar o crear ------------------------------------------------------

if [ "${SOLO_REVISAR:-}" = "1" ]; then
  echo "Título: $titulo_release"
  echo "Última: $ultima"
  echo "--- notas ---"
  printf '%s\n' "$notas"
  exit 0
fi

if gh release view "$tag" --repo "$repo" >/dev/null 2>&1; then
  echo "La release $tag ya existe en $repo; no la toco."
else
  archivo_notas="$(mktemp)"
  trap 'rm -f "$archivo_notas"' EXIT
  printf '%s\n' "$notas" > "$archivo_notas"
  gh release create "$tag" --repo "$repo" --verify-tag \
    --title "$titulo_release" --notes-file "$archivo_notas" --latest="$ultima"
  echo "Release $tag creada en $repo (última: $ultima)."
fi

# --- 5. Ningún tag sin release ---------------------------------------------

faltan=()
while IFS= read -r t; do
  [[ "$t" =~ ^v[0-9]+\.[0-9]+\.[0-9]+$ ]] || continue
  gh release view "$t" --repo "$repo" >/dev/null 2>&1 || faltan+=("$t")
done < <(git tag -l 'v*.*.*' | sort -V)

if [ "${#faltan[@]}" -gt 0 ]; then
  falla "Estos tags no tienen release: ${faltan[*]}. Corré el workflow a mano para cada uno: gh workflow run release.yml -f tag=<tag>"
fi
echo "Todos los tags vX.Y.Z tienen su release."
