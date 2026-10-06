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
