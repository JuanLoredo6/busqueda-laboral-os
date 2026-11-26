# Búsqueda laboral OS (Sistema de busca de emprego)

[English](README.en.md) · [Español](README.md) · **Português**

Um sistema para organizar a sua busca de emprego com o **Claude Code**: seu perfil, LinkedIn e currículo, cada candidatura, a preparação para entrevistas e um painel que diz o que fazer hoje. Tudo fica em pastas no seu computador.

Montamos o sistema para uma oficina entre colegas de TI que estão buscando o próximo desafio. Serve para qualquer perfil: desenvolvimento, QA, dados, produto, design, infraestrutura, projetos.

> **Idioma:** o Claude conversa com você em **português do Brasil** se você escrever em português ou escolher esse idioma ao começar. Ele também escreve seu currículo, seu LinkedIn, suas mensagens e suas respostas de entrevista em português (ou em espanhol ou inglês, conforme a vaga). Por dentro, os comandos, os skills, os modelos e o painel continuam em espanhol: os comandos como `/empezar` têm nome em espanhol, mas você pode pedir tudo com as suas palavras, em português.

> **🎓 Oficina ao vivo «Buscá con sistema»** (em espanhol): dois encontros com acompanhamento personalizado para usar este sistema na sua busca. Datas, preços e bolsas em **[busca-con-sistema.pages.dev](https://busca-con-sistema.pages.dev/)**.
>
> Você é headhunter ou recrutador independente? Veja a seção **Recruiters** da mesma página.

---

## Instalação assistida

Você precisa de um plano **Claude Pro ou Max** e do **app de desktop do Claude** ([claude.com/download](https://claude.com/download)). Não precisa saber programar nem ter conta no GitHub.

1. Abra o app, aba **Code**, e escolha a sua pasta **Documentos** como pasta de trabalho.
2. Cole este pedido:

```
Instale o sistema de busca de emprego seguindo, etapa por etapa, o guia https://raw.githubusercontent.com/JuanLoredo6/busqueda-laboral-os/main/INSTALACION.md. Fale comigo em português do Brasil.
```

O Claude guia você etapa por etapa: baixa o sistema, ajuda a abri-lo na pasta dele, conecta o Gmail e o Google Calendar (só leitura) e confere que tudo funciona. O guia completo, com os passos prévios e o que fazer se algo travar, está em **[INSTALACION.md](INSTALACION.md)** (em espanhol; o Claude explica em português).

Ao terminar, na pasta do sistema, escreva:

```
/empezar
```

### Se preferir fazer à mão

Com o Git instalado, em um terminal:

```bash
git clone https://github.com/JuanLoredo6/busqueda-laboral-os.git minha-busca
```

No app de desktop: escolha a pasta `minha-busca` como pasta de trabalho de uma sessão nova.

### Problemas frequentes

| O que acontece | O que fazer |
|---|---|
| Escrevo `/empezar` e não aparece | O Claude Code está aberto em outra pasta. Abra uma sessão nova **na pasta do sistema** (a que tem o `CLAUDE.md` dentro). Os skills só carregam ali |
| O Claude me pede permissão para tudo | Dentro da pasta do sistema, ler e editar arquivos já está permitido. Ele vai pedir permissão para buscar na internet ou rodar outros comandos: leia o que ele quer fazer e aceite se fizer sentido |
| O painel diz «Todavía no hay datos» | Rode `/empezar` primeiro. Se já rodou, peça ao Claude: «regenere o painel» |
| O painel não atualiza | Recarregue a página (F5). Se continuar igual, peça ao Claude: «rode tablero/sincronizar.sh» |
| O painel diz que a sincronização automática está «atrasada» | A tarefa agendada só roda com o app de desktop do Claude aberto. Abra o app e toque em 🔄 SYNC para pôr em dia |
| `/sincronizar-correo` diz que falta um conector | Toque no **+** ao lado da caixa de mensagem → conectores → Gmail ou Google Calendar → Conectar. Se o Claude continuar sem ver, abra uma sessão nova. Detalhes em [INSTALACION.md](INSTALACION.md), etapa 5 |
| No Mac, diz que falta o `git` | Aceite a janela que oferece instalar as ferramentas de desenvolvimento, espere terminar e tente de novo |
| Não sei o que fazer agora | Pergunte ao Claude «o que eu faço agora?» ou escreva `/mapa-de-skills` |

---

## Como se usa

| Quando | O que você diz ao Claude |
|---|---|
| A primeira vez | `/empezar` |
| Para melhorar o LinkedIn e o currículo (deixe o PDF do LinkedIn em `linkedin/`, seu currículo em `cv/`, ou os dois) | `/mejorar-perfil` |
| Quando vê uma vaga que interessa | `/analizar-oferta` e cola o link ou o texto |
| Para se candidatar | `/nueva-postulacion` |
| Quando acontece algo ("me responderam da X") | Conte para ele, ou `/actualizar` |
| Para trazer o que chegou por e-mail ou na agenda | 🔄 SYNC no painel, ou `/sincronizar-correo` |
| Para escrever para alguém | `/redactar-mensaje` |
| Antes de uma entrevista | `/preparar-entrevista` |
| Às sextas | `/repaso-semanal` |
| Para ver tudo o que existe | `/mapa-de-skills` |

Não precisa lembrar os nomes: se você pedir algo com as suas palavras, o Claude escolhe o skill certo.

### O painel

Abra `tablero/tablero.html` com dois cliques e deixe aberto em uma aba. Ele mostra (em espanhol):

- **Hoy (hoje):** se você tem algo para fazer hoje e o quê.
- **Lo que tenés que hacer (o que fazer):** as ações agrupadas em atrasadas, hoje, próximos dias e sem data.
- **Postulaciones (candidaturas):** um kanban com as colunas A enviar, Esperando resposta e Em conversa, e os dias sem novidade de cada uma.
- **Números:** candidaturas enviadas, taxa de resposta, conversas ativas e ações atrasadas.

Ele se atualiza sozinho cada vez que o Claude muda algo.

**Para que o que você marca seja salvo sozinho**, abra com `tablero/abrir-tablero.bat` no Windows ou `tablero/abrir-tablero.command` no Mac (precisa de Python). Assim, marcar uma ação como feita, mover um cartão, anotar uma novidade, adicionar uma ação ou corrigir com ✏️ a data de envio fica salvo na hora, sem passar pelo Claude. Encerrar uma candidatura continua passando pelo Claude, porque precisa do resultado. O servidor só escuta no seu computador e para quando você fecha a janela dele.

Se você abrir com dois cliques, o que marcar fica pendente: toque em **Copiar pedido para Claude** e cole no Claude Code para que fique salvo. O botão **⚡** de cada ação copia um pedido para o Claude ajudar você com essa tarefa.

Com o servidor, o botão **🎯 Práctica** abre a prática das entrevistas que você preparou com `/preparar-entrevista`. Você responde cada pergunta escrevendo ou em voz alta (o ditado é opcional: se você tiver o [uv](https://docs.astral.sh/uv/) instalado, a voz é transcrita no seu computador com o Whisper e o áudio não sai dele; na primeira vez baixa uns 480 MB. Sem o uv, usa o ditado do navegador, que processa o áudio na nuvem). A página mede quanto tempo você leva, salva suas respostas na pasta da entrevista e dá um pedido de uma linha para o Claude devolver o feedback e atualizar sua pontuação de preparação.

Para ver o painel com dados de exemplo antes de carregar os seus, abra o painel e toque em **Ver el tablero con datos de ejemplo**.

### Novidades do Gmail e do Google Calendar (opcional)

O Claude pode olhar seu e-mail e sua agenda **só para ler** e levar ao painel o que chega: confirmações, respostas de recrutadores, entrevistas agendadas, recusas.

1. Conecte o Gmail e o Google Calendar em claude.ai → **Configurações → Conectores**, com a sua conta do Google. Depois abra uma sessão nova do Claude Code na pasta do sistema.
2. Toque em **🔄 SYNC** no painel e cole o pedido no Claude Code, ou escreva `/sincronizar-correo`. Na primeira vez, o Claude pede permissão para ler: escolha **permitir sempre** para buscar e ler e-mails e para listar eventos.
3. Para que rode sozinha **a cada 2 horas, das 8 às 22**, escreva `/sincronizar-correo configurar`. Isso cria uma tarefa agendada no app de desktop do Claude, que roda enquanto o app está aberto.

O que é claro (uma entrevista com data, uma recusa explícita) é aplicado sozinho. O duvidoso, as propostas e os e-mails suspeitos ficam em **«Para revisar»** no painel, para você decidir. O Claude nunca responde, arquiva nem apaga e-mails.

---

## O que tem dentro

```
busqueda-laboral-os/
├── INSTALACION.md     O guia de instalação assistida
├── CLAUDE.md          Instruções para o Claude: limites, pastas, modelo de dados
├── contexto/          Sua fonte de verdade: perfil, o que você busca, sua voz, decisões · importado/ com o que você trouxer de antes
├── linkedin/          Seu PDF do LinkedIn · sugerencias/ com os textos novos
├── cv/                Seu currículo
├── postulaciones/     postulaciones.json (dados do painel) + uma pasta por candidatura
├── entrevistas/       Uma pasta por empresa com a preparação
├── investigacion/     Relatórios datados: diagnóstico, mercado, métricas, revisões
├── tablero/           tablero.html (abra com dois cliques)
├── plantillas/        O que o /empezar copia na primeira vez
└── .claude/skills/    Os 19 skills
```

### Os skills

**Dia a dia**

| Skill | Para quê |
|---|---|
| `empezar` | Primeiros passos: traz o que você já tem (currículo, LinkedIn, notas, o contexto de outra IA), carrega seu perfil, o que você busca e sua voz, e deixa o painel pronto |
| `mejorar-perfil` | Lê seu PDF do LinkedIn, seu currículo ou os dois, compara o que cada um tem, entrevista você e entrega textos prontos para copiar e colar, mais o currículo. Também em português do Brasil, sem portunhol, e em inglês |
| `analizar-oferta` | Aderência de uma vaga ao seu perfil (0 a 100), requisito por requisito, e se vale a pena |
| `nueva-postulacion` | Pasta, currículo adaptado, respostas do formulário e cartão no painel |
| `actualizar` | Leva cada novidade ao painel e cria as próximas ações |
| `sincronizar-correo` | Traz as novidades do Gmail e do Google Calendar ao painel, sob demanda (🔄 SYNC) ou a cada 2 horas das 8 às 22 |
| `redactar-mensaje` | Mensagens para recrutadores, indicações, follow-ups e agradecimentos com a sua voz |
| `preparar-entrevista` | Perguntas prováveis, histórias reais para cada uma no formato STAR-L e simulação com feedback |
| `repaso-semanal` | Números da semana, o que está caindo e três prioridades |

**Estratégia da busca**

| Skill | Para quê |
|---|---|
| `diagnostico-busqueda` | Por que a busca não avança: sintoma, causa e hipóteses para testar, e que números olhar para saber se você está avançando |
| `mercado-laboral` | Onde há demanda para o seu perfil e em que empresas mirar, com fontes |
| `posicionamiento` | Para que cargo você mira, que problema resolve, para quem e o que descarta. Depois, ângulos para se apresentar, seu pitch de 30 segundos e seu título |
| `plan-de-networking` | A quem pedir uma conversa, o que perguntar e como escrever |
| `aprendizajes-busqueda` | O que o feedback real diz (recusas, entrevistas, conversas) |

**Ferramentas de critério**

| Skill | Para quê |
|---|---|
| `poner-a-prueba` | Questiona cada conquista e cada decisão até que se sustente |
| `recruiters-sinteticos` | Testa seu currículo, pitch ou mensagem contra recrutadores simulados |
| `disenador-visual` | Especificar e construir currículo, capa, apresentação ou portfólio |
| `mapa-de-skills` | O índice de tudo isso |

---

## Seus dados

- Tudo o que é seu (perfil, currículo, candidaturas) fica **só no seu computador**. O `.gitignore` evita que isso suba para o GitHub por engano.
- **Não suba a sua cópia para um repositório público.** Se quiser um backup, copie a pasta para a sua nuvem (Drive, OneDrive, iCloud) ou use um repositório **privado**.
- O Claude não envia mensagens nem candidaturas por você: ele redige, e você envia.
- O Claude não pede nem guarda documentos (CPF, RG, DNI), dados bancários nem senhas.

## Atualizar o sistema

Quando houver uma versão nova, abra o Claude Code na pasta do sistema e peça «atualize o sistema». Se a sua cópia for anterior à 0.12.0, cole este pedido:

```text
Actualizá el sistema de búsqueda laboral siguiendo la guía https://raw.githubusercontent.com/JuanLoredo6/busqueda-laboral-os/main/ACTUALIZACION.md
```

O Claude primeiro faz um backup dos seus dados, traz o código novo (com Git ou com o ZIP, conforme você instalou), adapta seus dados ao que mudou e conta o que há de novo. O passo a passo está em [ACTUALIZACION.md](ACTUALIZACION.md) (em espanhol).

O que mudou em cada versão: [CHANGELOG.md](CHANGELOG.md) (em espanhol).

## Se você trocar de computador

Seus dados não estão no GitHub (o `.gitignore` os deixa de fora), então não basta baixar o sistema de novo: você leva **a pasta inteira em um ZIP**, com as pastas ocultas (`.git`, `.claude`). Assim vão juntos seus dados, a versão dos seus dados e a conexão para receber atualizações.

1. **No computador atual**, abra o Claude Code na pasta do sistema e cole:

   ```text
   Vou passar este sistema para outro computador. Confirme que você está na pasta do sistema e me diga quais dados meus estão aqui. Crie um ZIP da pasta inteira, com as pastas e arquivos ocultos (.git, .claude, .version-datos), na minha Área de Trabalho, com o nome mi-busqueda-traspaso e a data de hoje. Confira que o ZIP tem esses itens, me diga quanto pesa e se eu tenho uma tarefa agendada de sincronização. Não envie o ZIP para lugar nenhum nem apague nada desta pasta.
   ```

2. **Leve o ZIP** num pendrive ou na sua própria nuvem (Drive, OneDrive, iCloud), sem compartilhar o link: seu CV está dentro. Quando terminar, apague de lá.
3. **No computador novo**, instale o app do Claude, entre com a mesma conta, aba **Code**, ambiente **Local**, abra a pasta **Documentos** e cole (com o local do ZIP):

   ```text
   Trouxe meu sistema de busca de emprego de outro computador num ZIP que está em [onde ficou]. Descompacte em Documentos como mi-busqueda (se já existir, não sobrescreva e me pergunte). Confira que estão CLAUDE.md, .claude/skills/empezar/SKILL.md e meus dados em postulaciones e contexto. Me diga o caminho completo e como abrir uma sessão nova nessa pasta.
   ```

4. Na sessão nova, escreva **continue a instalação**: o Claude vê que o sistema já está lá e retoma a partir dos conectores do Gmail e do Calendar e do painel.
5. Se você usava a sincronização automática, crie de novo com `/sincronizar-correo configurar`: tarefas agendadas não passam de um computador para outro. As conversas antigas também não, mas tudo o que importa está nos arquivos.

A cópia é uma foto do momento: a partir daí, trabalhe no computador novo. Se continuar anotando nos dois, eles se desencontram. A pasta antiga fica como backup.

---

## Instruções de instalação para o Claude Code

*Esta seção é para o Claude.* Se pediram para você instalar este sistema, siga o protocolo de [INSTALACION.md](INSTALACION.md), parte 2, etapa por etapa, conversando em português do Brasil.

---

## Créditos

- Sistema montado por Juan Rodríguez Loredo para a oficina. Licença MIT: ver [LICENSE](LICENSE).
- Treze peças do sistema (skills ou partes de um skill) são adaptações dos skills de produto de **Pedro Romero Luna** ([ai-first-product-skills](https://github.com/pedroromeroluna/ai-first-product-skills), licença MIT). Detalhes em [CREDITOS.md](CREDITOS.md).
- Várias seções adaptam métodos de **Paweł Huryn** ([The Product Compass](https://www.productcompass.pm)), publicados com licença MIT em [pm-skills](https://github.com/phuryn/pm-skills), [product-engineering](https://github.com/phuryn/product-engineering) e [pm-brain](https://github.com/phuryn/pm-brain). Detalhes em [CREDITOS.md](CREDITOS.md).
