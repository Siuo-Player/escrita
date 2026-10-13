# escrita

Projeto de ficção episódica em português, situado no universo de *Modern Family* e construído com pesquisa factual, controlo temporal e continuidade narrativa.

## Objetivo

Criar uma história episódica em que um personagem original é introduzido no universo de *Modern Family*. A série original funciona como **baseline de continuidade**, mas a presença do protagonista produz um efeito de borboleta gradual: acontecimentos conhecidos podem mudar, surgir consequências novas e personagens podem evoluir, desde que as mudanças sejam causais, proporcionais e coerentes.

O foco do projeto não é escrever tudo de uma vez. Primeiro construímos o **modelo do mundo**, o **estado persistente dos personagens**, a **linha temporal** e a **estrutura narrativa**. A prosa vem depois.

## Princípios

1. **Continuidade primeiro.** Nenhum detalhe novo deve contradizer sem explicação um facto já estabelecido.
2. **Datas explícitas.** Quando a fonte permite uma data exata, usamos a data gregoriana completa. Quando não permite, registamos a incerteza em vez de inventar precisão.
3. **Causalidade.** Mudanças de personagem e de trama devem resultar de acontecimentos, escolhas ou consequências identificáveis.
4. **Efeito de borboleta gradual.** A presença do protagonista altera a trajetória, mas as divergências acumulam-se progressivamente.
5. **Memória limitada ao material conhecido pelo protagonista.** Ele conhece perfeitamente *Modern Family*, mas isso não lhe dá acesso automático a pensamentos, acontecimentos fora do ecrã ou informação que a série nunca revelou.
6. **Estado persistente.** O mundo e os personagens têm informação que sobrevive entre episódios.
7. **Backpropagation narrativa.** Depois de cada arco suficientemente desenvolvido, voltamos aos episódios anteriores para inserir pistas, motivos, callbacks e pequenas consequências que tornem a evolução retroativamente natural.
8. **Ficção documental.** Factos históricos, tecnológicos, culturais, escolares, geográficos e temporais relevantes são pesquisados e separados da invenção narrativa.

## Estrutura inicial

- `research/` — investigação externa e modelos narrativos.
- `canon/` — contrato de continuidade, calendário e estado persistente.
- `episodes/` — unidade principal da história; cada episódio contém acontecimentos e pastas dos personagens envolvidos.
- `templates/` — estruturas repetíveis para episódios, acontecimentos e personagens.

### Pesquisa narrativa atual

- `research/narrative/README.md` — evidência e modelos de estrutura narrativa.
- `research/narrative/STRUCTURE_MATRIX.md` — comparação de lentes estruturais.
- `research/narrative/MODERN_FAMILY_FANFIC_CASE_STUDIES.md` — estudo de receção e falhas recorrentes
  em fanfics de *Modern Family*.
- `canon/STORY_SCOPE_AND_PROTAGONIST_DESIGN.md` — regras de trabalho para manter uma vida
  independente do protagonista, uso limitado de conhecimento futuro e equilíbrio com a série.


## Aviso sobre fanfiction e direitos

Este repositório documenta o planeamento de uma obra de **fanfiction não oficial** ambientada no universo de *Modern Family*. Não é afiliado, patrocinado, autorizado nem endossado pelos titulares dos direitos da série. Os nomes, personagens, elementos do universo e outros materiais preexistentes de *Modern Family* pertencem aos respetivos titulares. Nathan Callahan, a família Callahan, as tramas originais e os restantes elementos criados especificamente para esta história são material original deste projeto.

O aviso identifica a natureza do projeto; **não constitui uma licença, não demonstra autorização e não garante que qualquer utilização esteja legalmente autorizada**. A lei aplicável e eventuais exceções dependem dos factos e da jurisdição. O projeto não deve reproduzir diálogos longos, guiões, imagens, episódios ou outro material protegido desnecessariamente. Este repositório é um projeto de planeamento narrativo; qualquer publicação ou exploração futura deve ser revista separadamente.

## Estado atual

**Fase 0 — Fundação.**

Ainda não existe uma história em prosa. Estamos a decidir o mundo, o protagonista, o ponto de entrada, o horizonte temporal e as regras de continuidade.

## Regra de confiança

Cada decisão será classificada como:

- **CANON** — suportada pela série ou por fonte primária/forte.
- **DERIVADA** — conclusão necessária ou muito forte a partir de factos canon.
- **WORKING** — hipótese de construção ainda alterável.
- **CRIADA** — elemento original da fanfic.
- **INCERTA** — o próprio canon contém contradições ou a evidência disponível é insuficiente.

A classificação não é decorativa: serve para sabermos o que pode ser alterado sem quebrar a coerência.

## Fluxo de trabalho

Investigação → decisão → registo → perguntas específicas → construção incremental → episódio → verificação temporal → verificação de continuidade → backpropagation → revisão da documentação → prosa final.


## Continuidade, decisões e método de escrita

- `canon/DECISION_LOG.md` — decisões escolhidas, alternativas, evidência, processo de validação e dependências.
- `canon/characters/CHARACTER_NAME_REGISTRY.md` — nomes escolhidos, nomes rejeitados e seleção aleatória reproduzível.
- `canon/narrative/NARRATIVE_AND_CAUSAL_METHOD.md` — arquitetura top-down recursiva, construção causal linear, registo de estado e backpropagation.


## Character state, supporting cast and ability continuity

- [Character state continuity standard](canon/characters/CHARACTER_STATE_CONTINUITY_STANDARD.md) — life-to-scene state, recent-past detail, knowledge limits, skills, props and backpropagation rules.
- [Nathan's knowledge and skill ledger](canon/characters/NATHAN_KNOWLEDGE_AND_SKILL_LEDGER.md) — the protagonist's internal skills, factual knowledge, previous-life memories and limitations.
- [Football teams and player backgrounds](canon/characters/FOOTBALL_TEAMS_AND_PLAYERS.md) — the Seattle team, the new Southern California team and each player's working background.
- [Secondary social circles](canon/characters/SECONDARY_SOCIAL_CIRCLES.md) — recurring classmates/friends around Alex and Haley and Claire's community contacts.
- [Cast naming draw audit](canon/characters/CAST_NAMING_DRAW_AUDIT.md) — reproducible name-generation pools, seeds, selections and a partial 2020 Census rank audit.
- [Modern Family core-character state baselines](canon/characters/MODERN_FAMILY_CORE_STATE_BASELINES.md) — canon starting states, character-specific behavior, and limits on what they know about Nathan.
- [Episode 1 scene-state ledger](episodes/season-1/EP01_SCENE_STATE_LEDGER.md) — dated pre-state, knowledge boundaries, props, causes and carry-forward changes for the September opening.
- [Episode 2 scene-state ledger](episodes/season-1/EP02_SCENE_STATE_LEDGER.md) — dated knowledge/relationship/football/game states and the private test-build endpoint.
- [First mobile game technical design](canon/projects/NATHAN_FIRST_MOBILE_GAME.md) — game architecture, 2009 hardware constraints and the working Mac/iPod touch build path.

The relationship calendar is not a rigid deadline: early episode drafts test the pacing, and the top-down plan and forward scene sequence may both be revised if the finished story needs it.
