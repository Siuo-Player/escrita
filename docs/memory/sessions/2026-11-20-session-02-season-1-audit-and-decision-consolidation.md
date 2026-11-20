# Sessão 2026-11-20 — Auditoria global da Temporada 1 e consolidação de decisões

**Branch:** `audit/season-1-continuity-decisions-20261120`  
**PR:** [#24 — audit: consolidate Season 1 decisions and continuity](https://github.com/Siuo-Player/escrita/pull/24)  
**Estado à data desta nota:** alterações preparadas em branch; validação CI final do último commit ainda pendente.  
**Âmbito:** auditoria de continuidade e documentação da temporada 1 inteira, não revisão literária final de cada frase.

## 1. Objetivo e método

A tarefa foi transformar decisões espalhadas por perfis, cronologias, outlines, drafts, registos de objetos e documentação técnica numa referência única e auditável.

Foi utilizado o método *tests-first*:
1. foram criados testes de regressão para regras transversais;
2. os testes foram executados antes das correções e falharam nas contradições esperadas;
3. os documentos e drafts foram corrigidos;
4. as regressões foram executadas novamente em CI para Python 3.10, 3.11 e 3.12.

Os testes verificam invariantes documentais e estruturais. Não provam naturalidade dos diálogos, qualidade literária, ritmo ou causalidade semântica.

## 2. Decisões anteriores consolidadas

As decisões DEC-001 a DEC-010 mantêm a sua proveniência e estado em `canon/DECISION_LOG.md`:

| ID | Decisão mantida |
|---|---|
| DEC-001 | O protagonista chama-se Nathan. |
| DEC-002 | O apelido escolhido é Callahan. |
| DEC-003 | Maxwell Whitaker é o colega recorrente do futebol; continua uma proposta de trabalho, não uma escolha imutável. |
| DEC-004 | Os pais usam os nomes de trabalho Clifford e Heather; continuam revisáveis. |
| DEC-005 | Para escolhas criativas subdeterminadas, usar aleatoriedade controlada, com candidatos filtrados e resultado reproduzível; a preferência do autor prevalece. Não randomizar factos nem decisões causais importantes. |
| DEC-006 | Método dual-track: arquitetura top-down da série/temporada, construção causal cronológica de cenas, backpropagation de pistas e posterior leitura para a frente para detetar regressões. |
| DEC-007 | Transparência do repositório e disclaimer foram considerados; disclaimer não equivale a autorização nem imunidade jurídica. |
| DEC-008 | Todos os drafts e diálogos da obra são em inglês americano, adequado a 2009. |
| DEC-009 | Estilo de ficção seriada moderna, encenação física com sensibilidade teatral e POV/voz adaptados à personagem. |
| DEC-010 | Tramas simultâneas representadas por intervalos temporais e cortes editoriais/POV deliberados; cada episódio deve ter pelo menos três tramas consequentes, sem fillers. |

A referência consolidada também regista a premissa do universo paralelo (WD-001–WD-004), a memória limitada de Nathan, as suas fraquezas, a relação gradual com Alex, o projeto do jogo, o papel dos personagens e a hierarquia documental.

## 3. Novas decisões de continuidade

### DEC-011 — Separação escolar

Nathan está no 8.º ano e Alex no 7.º ano durante o ano letivo 2009–10. Esta diferença mantém-se até junho de 2010:
- Nathan conclui o 8.º ano e prepara a entrada no High School;
- Alex conclui o 7.º ano e transita para o 8.º ano;
- não se graduam juntos na middle school, nem se pressupõe aceleração/repetição de ano.

A decisão corrige a antiga descrição de ambos partilharem a distinção do 8.º ano e de ambos se graduarem juntos. Foi propagada para o plano da temporada e para a continuidade/escalas escolares.

### DEC-012 — Marcos do primeiro jogo

Os três marcos deixam de ser confundidos:
- **15/10/2009:** primeira versão vertical jogável, de ponta a ponta, para teste interno/privado; não é publicação pública.
- **18/11/2009:** Clifford, titular adulto da conta de developer, aceita os termos aplicáveis e submete a v1.0 à Apple.
- **03/12/2009:** a aplicação fica disponível na App Store após revisão.

A distinção está propagada para a continuidade, design técnico do jogo e outline do EP02. Preserva a regra legal já registada: Nathan desenvolve sob supervisão; Clifford é o titular adulto/publicador. A titularidade dos rendimentos e a sua transferência para Nathan continuam por resolver.

### DEC-013 — Pool de entidades e buffers

A pool do EP04 reutiliza registos de entidades e buffers de contactos temporários durante criação/remoção de agentes e reinício de cenários. Não deve ser justificada por alocar/libertar nós de pesquisa global centenas de vezes por frame. O flow field partilhado é construído uma vez e só é regenerado perante alterações relevantes no mapa/destino.

### DEC-014 — Escala de boids

No EP06, 30 agentes representam 435 pares por frame (26.100/s a 60 FPS), não uma saturação demonstrada do CPU. A grelha espacial serve a demonstração e a escalabilidade para o caso de stress de 200 agentes: 19.900 pares por frame (1.194 milhões/s a 60 FPS) na abordagem ingénua. A grelha reduz candidatos em distribuição normal, mas não elimina o pior caso quadrático de concentração numa célula.

## 4. Correções de continuidade e plausibilidade

### EP01
- A fala sobre os 256 MB do iPhone 3GS deixou de atribuir ao sistema uma divisão fixa de quase metade da RAM ou a Nathan um heap garantido de 128 MB.
- Nathan reconhece que a memória disponível à aplicação depende da atividade do sistema e que deve medir o build real.
- A métrica do ecrã passou de `Memory: 4.2 MB` para `ENGINE DATA: 4.2 MB`, para identificar o que está a ser medido.
- O estado do episódio passou a ser explicitamente um draft de trabalho de cerca de 7,600 palavras, abaixo do objetivo de 10,000–14,000+.

### EP02
- O estado passou a draft de trabalho de cerca de 4,400 palavras, abaixo do objetivo.
- Foi removida a afirmação pseudocientífica de que o cérebro consome vinte por cento da glicose diária.
- A métrica de 28.4 MB passou a chamar-se `LIVE HEAP`, e não RAM.
- O marco de 15 de outubro no outline foi renomeado para versão vertical jogável interna, sem confundir com a publicação.

### EP03
- Foi removido o segundo exemplar integral do Director's Cut de Luke de 16 de outubro, que estava duplicado no draft.
- Mantém-se o draft estrutural de cerca de 8,400 palavras, abaixo do objetivo.

### EP05
- Alex está no 7.º ano; a cena deixou de a colocar num contexto de escola secundária.
- O teste de química orgânica passou a teste de ciências, e a exaustão deixou de depender de quatro noites sem dormir.
- A linguagem sobre a vulnerabilidade de Alex foi suavizada: a personagem não é reduzida a uma “máscara de arrogância”.
- Nathan deixa de ser declarado, sem evidência suficiente, “o único amigo” em quem ela confia.

### EP04
- A *object pool* trata criação/remoção de entidades e buffers temporários de colisão em reinícios de cenários; deixa de atribuir ao flow field pesquisas globais por inimigo a cada frame.

### EP06 e design técnico
- A atualização v1.1 reutiliza a grelha espacial `SpatialGrid` criada no EP03 para deteção de colisões.
- Para raio de perceção até 32 px, os agentes consultam a célula atual e as oito adjacentes, seguidas de testes de distância exatos.
- Não é criada uma segunda estrutura espacial independente. Está registado que uma grelha uniforme reduz candidatos no caso normal, mas não garante custo linear no pior caso.
- O EP06 deixou de declarar o ciclo de introduções canon completo: Gloria continua a conhecer Nathan pela primeira vez no EP07.

### EP10–EP12
- EP11/EP12 respeitam agora a diferença de um ano entre Nathan e Alex.
- EP10 deixou de afirmar que Nathan pode comprar diretamente um iPad com receitas que a Apple teria transferido automaticamente para ele. O acesso/compra fica dependente de uma decisão explícita de Clifford e Heather sobre os recebimentos geridos pela conta adulta.
- Corrigida a identificação errada “Claire Callahan”; a referência correta é Claire Dunphy e Heather Callahan.

## 5. Contradições deixadas abertas deliberadamente

Estas questões não foram “resolvidas” inventando cenas ou factos:

1. **Quatro familiares até 23/09:** o objetivo de que quatro familiares Dunphy/Pritchett/Tucker conheçam Nathan até à âncora de *Pilot* não é satisfeito pelo registo atual. Só Alex o conhece antes dessa data; Phil entra em 28/09, Claire em 10/10 e Luke em 22/10. É necessário escolher entre criar encontros de bairro credíveis antes de 23/09 e registar todas as consequências, ou rever o objetivo.
2. **Receitas e impostos:** não está decidido como o dinheiro recebido pela conta adulta de Clifford passa a ser propriedade ou poupança de Nathan. O iPad do EP10 depende dessa decisão familiar/legal.
3. **Tração inicial da App Store:** 23 downloads no primeiro dia, 140 acumulados em 04/12, 500 em 06/12, 620 em 08/12 e 4.8 estrelas precisam de mecanismo de descoberta e dimensão de amostra de avaliações credíveis. São valores ficcionais do mundo narrativo, não médias históricas.
4. **v1.1:** a temporada antecipa submissão no início de janeiro, mas submissão, aprovação e publicação ainda precisam de datas e eventos próprios no Event Registry.
5. **Arco de foreknowledge:** a política está definida, mas ainda falta auditar oportunidades datadas em que Nathan tenha conhecimento, acesso e uma intervenção útil.
6. **Universidade/rota académica futura:** permanece aberta.
7. **Relações românticas após a amizade de Season 1:** permanecem em aberto; o possível arco adulto com Haley não tem data nem causa fixada.
8. **Personagens originais e plantéis:** Maxwell e várias personagens secundárias continuam propostas de trabalho, salvo decisões posteriores mais específicas.

## 6. Estado real da temporada

Contagens aproximadas a partir dos ficheiros atuais, não metas cumpridas:

| Episódio | Estado | Palavras aproximadas |
|---|---|---:|
| EP01 | Draft de trabalho; abaixo da meta | 7,600 |
| EP02 | Draft de trabalho; abaixo da meta | 4,400 |
| EP03 | Draft estrutural; abaixo da meta | 8,400 |
| EP04–EP06 | Outlines expandidos; sem drafts de prosa | — |
| EP07–EP12 | Resumos na arquitetura da temporada; sem outlines individuais | — |

O Event Registry contém EVT-001–EVT-028 para EP01–EP06 até 19/12/2009; o próprio registo indica cobertura parcial. A temporada não está escrita nem fechada.

## 7. PRs antigas encontradas

- **PR #11:** permanece aberta e não foi importada. Contém scene-state ledgers e material de elenco útil, mas também pressupostos incompatíveis com o estado atual, incluindo contactos no dia da mudança e um setup técnico diferente no arranque.
- **PR #14:** permanece aberta e não foi importada. A sua investigação histórica/Apple tem sobreposição substancial com a versão já integrada em `TECHNICAL_AND_LEGAL_FOUNDATIONS.md`; deve ser comparada antes de qualquer ação para evitar duplicação ou regressão.

Nenhuma destas PRs foi fundida como parte desta sessão.

## 8. Testes e validação

Foi acrescentado `tests/test_season_1_decision_consistency.py` para proteger:
- transição de ano escolar;
- separação dos três marcos de distribuição do jogo;
- objetivo dos quatro contactos ainda não resolvido;
- distinção entre RAM física, heap vivo e dados do motor;
- remoção da afirmação pseudocientífica de glicose;
- unicidade da cena POV de Luke;
- reutilização da grelha espacial;
- matéria escolar de Alex;
- estado de apresentação de Gloria;
- financiamento do iPad e nomenclatura de Claire.

A validação no commit de código **cd7849a59f862f1d067386d97eac9c7da18af6cb** passou no run **44793314776**: **73 testes passaram em cada versão de Python 3.10, 3.11 e 3.12**. A nota de sessão e o índice de memória foram acrescentados depois desse commit; a CI acionada pelo novo head documental deve igualmente ser confirmada antes de integrar a PR.

## 9. Ficheiros centrais a consultar

- `canon/narrative/SEASON_1_DECISION_AND_STATUS_REGISTER.md` — índice consolidado desta temporada.
- `canon/DECISION_LOG.md` — proveniência e estado DEC-001 em diante.
- `canon/STORY_DECISIONS_TO_MAKE.md` — questões ainda abertas.
- `canon/narrative/EVENT_REGISTRY.md` — cronologia causal registada.
- `canon/narrative/WORLD_DIFFERENCE_REGISTRY.md` — regras do universo paralelo.
- `canon/narrative/PROP_AND_CLUE_REGISTRY.md` — objetos, pistas e respetiva causalidade.
- `canon/timeline/SEASON_1_CONTINUITY.md` e `SEASON_1_RECURRING_SCHEDULES.md` — calendário e rotina.
- `canon/projects/NATHAN_FIRST_MOBILE_GAME.md` — design técnico do primeiro jogo.
- `tests/` — guardrails determinísticos, não avaliação literária.

## 10. Próximos passos

1. Confirmar CI no head final da PR #24 e integrar se todos os jobs passarem.
2. Resolver deliberadamente o objetivo dos quatro contactos antes de 23/09, sem alterar o evento sem registar o seu impacto.
3. Auditar a cronologia e relações dos EP01–EP06 cena a cena contra os scene-state ledgers relevantes e os registos de eventos/objetos.
4. Desenvolver EP04–EP06 para drafts completos com causalidade, sem expandir artificialmente.
5. Transformar EP07–EP12 de resumos em outlines individuais; registar os eventos novos antes de começar a prosa.
6. Só depois fazer uma revisão literária final de cada draft, incluindo vozes, ritmo, diálogo, POV e qualidade dramática.
