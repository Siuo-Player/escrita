# Registo de Adereços, Pistas e Backpropagation de Causalidade

Status: AUTHORITATIVE CAUSAL LEDGER  
Updated: 2026-11-19

Este registo garante o princípio de **backpropagation narrativa e integridade de adereços**: nenhum objeto relevante, pista ou detalhe crucial pode surgir do nada no momento em que a trama precisa dele. Cada elemento deve ter génese explicada, presenças em fundo de cena prévias e resolução merecida.

---

## Tabela de Adereços e Pistas Rastreadas

| ID | Elemento / Pista | Génese (Aquisição / Aparição Inicial) | Presença em Fundo de Cena (Passagens Naturais) | Ponto Causal / Payoff (Resolução) | Estado |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **PROP-001** | **MacBook Pro 15" (Unibody 2009)** | **EP01 (07/09/2009)**: Prenda de 13º aniversário dada por Clifford antes do anúncio da mudança. | **EP01 (12/09)**: Na mala de viagem; **EP01 (16/09)**: Secretária do quarto temporário; **EP02 (02/10)**: Na biblioteca. | **EP02**: Alex repara no código C++ e no terminal aberto, quebrando a barreira da timidez técnica. | ATIVO |
| **PROP-002** | **Manual Avançado de Álgebra / Cálculo** | **EP01 (15/09/2009)**: Retirado da caixa de livros técnicos na mudança para Los Angeles. | **EP01 (17/09)**: Em cima da secretária; **EP01 (18/09)**: Visível no cacifo de Nathan. | **EP01 (18/09)**: Alex repara no livro e inicia o primeiríssimo diálogo com Nathan para esclarecer uma dúvida. | ATIVO |
| **PROP-003** | **Bola de Treino e Chuteiras de Futebol** | **EP01 (07/09/2009)**: Nathan treina controlo de bola no quintal da casa de Seattle. | **EP01 (19/09)**: Mala de desporto no carro; **EP02 (03/10)**: No relvado do treino escolar. | **EP02 / EP03**: Maxwell Whitaker desafia Nathan no treino; Luke repara nos remates de Nathan do outro lado da vedação. | ATIVO |
| **PROP-004** | **Aparelho iPhone 3GS de Testes** | **EP01 (15/09/2009)**: Dispositivo desbloqueado de testes trazido pelo pai para perfilagem de CPU/GPU. | **EP02 (05/10)**: Conectado por cabo de 30 pinos branco ao computador na mesa de jantar. | **EP02 (12/10)**: Teste sob stress de 200 agentes com *flow field* que quase esgota a RAM (128MB livre). | ATIVO |
| **CLUE-001** | **Chaveiro com Pendente de Bússola Antiga (Objeto Perdido)** | **EP02 (08/10/2009)**: Visto no bolso do casaco de Nathan durante a ida ao parque; cai silenciosamente junto ao banco. | **EP03 (16/10)**: Luke passa de bicicleta e vê um reflexo de metal perto dos arbustos sem recolher imediatamente. | **EP04 (24/10)**: Nathan apercebe-se da perda; Luke traz o objeto na escola gerando a primeira interação direta Nathan-Luke. | ATIVO |
| **CLUE-002** | **Caderno de Esboços Algorítmicos** | **EP01 (08/09/2009)**: Comprado na papelaria em Seattle para diagramas de vetores de navegação. | **EP02 (04/10)**: Aberto ao lado do teclado na biblioteca; Alex vê um gráfico de vetores de passagem. | **EP03 (10/10)**: Alex pergunta a Nathan se aquilo é física ou matemática computacional, aprofundando o respeito mútuo. | ATIVO |

---

## Protocolo de Adição de Nova Pista ou Adereço Invertido (Backpropagation)

Quando surgir uma ideia para um capítulo futuro (ex: Capítulo $N$ com busca por algo perdido, ou segredo descoberto):
1. **Registar no ID acima** o adereço e a intenção de resolução no Capítulo $N$.
2. **Retroceder aos Capítulos Anteriores:**
   - No Capítulo $N-3$: Adicionar a cena casual onde o objeto é obtido ou usado casualmente por um personagem.
   - No Capítulo $N-2$: Adicionar um vislumbre em segundo plano (em cima de uma mesa, alguém a guardá-lo ou a deixá-lo cair sem reparar).
   - No Capítulo $N-1$: Adicionar uma consequência menor impercetível (alguém bate na mesa, ou procura noutro casaco).
3. **Auditoria com Testes Automáticos:** Correr `python tests/run_story_tests.py` para certificar que os ficheiros mantêm linearidade temporal e referência de proveniência.
