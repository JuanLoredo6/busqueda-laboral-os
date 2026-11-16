# Cómo se publica una versión

Las releases se publican solas: al subir un tag `vX.Y.Z`, el workflow `.github/workflows/release.yml` crea la release de GitHub con el texto de esa versión en `CHANGELOG.md`. Nadie escribe las notas a mano.

## Pasos

1. **Versioná el CHANGELOG dentro del PR.** La sección «Sin publicar» pasa a ser `## X.Y.Z — AAAA-MM-DD · Título` (raya `—`, punto medio `·`) y se abre una «Sin publicar» vacía arriba. El título es obligatorio: de ahí sale el de la release.
2. **Mergeá el PR y actualizá main:**

   ```bash
   git switch main
   git pull origin main
   ```

3. **Poné el tag anotado en ese commit y subilo solo:**

   ```bash
   git tag -a vX.Y.Z -m "vX.Y.Z · Título"
   git push origin vX.Y.Z
   ```

   De a un tag, no con `git push --tags`: así cada push dispara su propio workflow y no se sube un tag que no querías.
4. **Comprobá que salió:**

   ```bash
   gh run list --workflow release.yml --limit 1
   gh release view vX.Y.Z
   ```

## Qué revisa el workflow

El script `.github/scripts/release-desde-changelog.sh` falla, con un mensaje que dice cómo arreglarlo, si:

- el tag no tiene la forma `vX.Y.Z`, no existe o es liviano (tiene que ser anotado, `git tag -a`);
- el commit del tag no está en `origin/main`;
- `CHANGELOG.md` no tiene la sección `## X.Y.Z — `, o le falta el título o el contenido.

Si todo está bien:

- arma las notas con el texto de la sección y suma al final el link «Cambios completos» contra el tag anterior;
- marca la release como la última solo si es la versión más alta;
- si la release ya existe, no la toca;
- al final revisa que **todos** los tags `vX.Y.Z` tengan release y falla listando los que no. Así un tag sin release no pasa desapercibido.

## Correrlo a mano

Para una versión vieja, o si el workflow falló y ya lo arreglaste:

```bash
gh workflow run release.yml -f tag=vX.Y.Z
```

Para ver qué publicaría sin crear nada, desde la raíz del repo:

```bash
SOLO_REVISAR=1 bash .github/scripts/release-desde-changelog.sh vX.Y.Z
```
