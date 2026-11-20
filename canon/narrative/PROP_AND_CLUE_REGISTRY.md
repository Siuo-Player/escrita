# Registo de Adereços, Pistas e Backpropagation de Causalidade

Status: AUTHORITATIVE CAUSAL LEDGER  
Updated: 2026-11-19

Este registo garante o princípio de **backpropagation narrativa e integridade de adereços**: nenhum objeto relevante, pista ou detalhe crucial pode surgir do nada no momento em que a trama precisa dele. Cada elemento deve ter génese explicada, presenças em fundo de cena prévias e resolução merecida.

---

## Tabela de Adereços e Pistas Rastreadas

| ID | Elemento / Pista | Génese (Aquisição / Aparição Inicial) | Presença em Fundo de Cena (Passagens Naturais) | Ponto Causal / Payoff (Resolução) | Estado |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **PROP-001** | **MacBook Pro 15" (Unibody 2009)** | **EP01 (07/09/2009)**: Prenda de 13º aniversário dada por Clifford antes do anúncio da mudança. | **EP01 (12/09)**: Na mala de viagem; **EP01 (16/09)**: Secretária do quarto temporário; **EP02 (02/10)**: Na biblioteca. | **EP02 (02/10/2009)**: Alex repara no código C++ e no terminal aberto, quebrando a barreira da timidez técnica. | ATIVO |
| **PROP-002** | **Manual Avançado de Álgebra / Cálculo** | **EP01 (15/09/2009)**: Retirado da caixa de livros técnicos na mudança para Los Angeles. | **EP01 (17/09)**: Em cima da secretária; **EP01 (18/09)**: Visível no cacifo de Nathan. | **EP01 (18/09)**: Alex repara no livro e inicia o primeiríssimo diálogo com Nathan para esclarecer uma dúvida. | ATIVO |
| **PROP-003** | **Bola de Treino e Chuteiras de Futebol** | **EP01 (07/09/2009)**: Nathan treina controlo de bola no quintal da casa de Seattle. | **EP01 (19/09)**: Mala de desporto no carro; **EP02 (03/10)**: No relvado do treino escolar. | **EP02 (02/10/2009) / EP03 (22/10/2009)**: Maxwell Whitaker desafia Nathan no treino; Luke repara nos remates de Nathan do outro lado da vedação. | ATIVO |
| **PROP-004** | **Aparelho iPhone 3GS de Testes** | **EP01 (15/09/2009)**: Dispositivo de testes trazido por Clifford para perfilagem de CPU/GPU; associado à conta Standard iPhone Developer Program de Clifford, sob a sua supervisão. | **EP02 (05/10)**: Conectado por cabo de 30 pinos branco ao computador na mesa de jantar. | **EP02 (12/10) / EP04**: Teste sob stress do motor com *flow field*: objetivo interno de manter as alocações vivas do heap abaixo de 35 MB. É um orçamento de engenharia de Nathan, não um limite nem um limiar de aviso do iPhone OS 3.1. | ATIVO |
| **PROP-005** | **Cronómetro Digital de Treino (Casio)** | **EP01 (14/09/2009)**: Retirado da gaveta de desporto em Seattle e colocado no pulso. | **EP01 (28/09)**: No pulso durante a corrida matinal; Phil repara na cadência métrica; **EP02 (03/10)**: Cronometrando séries com Maxwell. | **EP04 (07/11)**: Phil pede emprestado a Nathan para cronometrar uma experiência caseira de velocidade com Luke, cimentando a admiração de Phil. | ATIVO |
| **PROP-006** | **Edição Usada das Palestras de Feynman em Física (Capa Vermelha)** | **EP03 (24/10/2009)**: Avistado numa estante interior da secção de física de uma livraria em Westwood durante um recado com Heather. | **EP04 (14/11)**: Comprado por Nathan na secção de usados e guardado na gaveta da secretária. | **EP06 (18/12)**: Entregue discretamente a Alex como prenda de Natal sem alarido ("Custou dois dólares num caixote"), deixando-a profundamente comovida. | ATIVO |
| **CLUE-001** | **Chaveiro com Pendente de Bússola Antiga (Objeto Perdido)** | **EP02 (08/10/2009)**: Visto no casaco de Nathan durante treino no parque; cai silenciosamente junto aos arbustos da vedação. | **EP03 (16/10)**: Luke passa de bicicleta e repara num brilho metálico junto à sebe do parque. | **EP03 (22/10)**: Luke encontra a bússola nos arbustos ao devolver a bola [PROP-003], gerando a primeira interação direta entre Nathan e Luke. | ATIVO |
| **CLUE-002** | **Caderno de Esboços Algorítmicos** | **EP01 (08/09/2009)**: Comprado na papelaria em Seattle para diagramas de vetores de navegação. | **EP02 (04/10)**: Aberto ao lado do teclado na biblioteca; Alex vê um gráfico de vetores de passagem. | **EP03 (19/10/2009)**: Alex repara nos diagramas vetoriais do caderno, pergunta se Nathan está a calcular dinâmica de fluidos e ouve-o explicar o método de *flow field*, aprofundando o respeito mútuo. | ATIVO |
| **CLUE-003** | **Peça de Xadrez em Madeira (Cavalo Preto Esculpido)** | **EP01 (12/09/2009)**: Guardado no bolso lateral da mochila de viagem (peça solta do antigo tabuleiro do avô em Seattle). | **EP02 (06/10)**: Retirado ao procurar um lápis no cacifo; **EP04 (06/11)**: Alex repara na peça enquanto estuda no quarto de Nathan. | **EP05 (01/12)**: Na biblioteca municipal, ao ver Manny hesitar num problema tático na mesa pública, Nathan sugere a manobra de cavalo, iniciando o primeiro debate entre ambos. | ATIVO |

---

## Protocolo de Adição de Nova Pista ou Adereço Invertido (Backpropagation)

Quando surgir uma ideia para um capítulo futuro (ex: Capítulo $N$ com busca por algo perdido, ou segredo descoberto):
1. **Registar no ID acima** o adereço e a intenção de resolução no Capítulo $N$.
2. **Retroceder aos Capítulos Anteriores:**
   - No Capítulo $N-3$: Adicionar a cena casual onde o objeto é obtido ou usado casualmente por um personagem.
   - No Capítulo $N-2$: Adicionar um vislumbre em segundo plano (em cima de uma mesa, alguém a guardá-lo ou a deixá-lo cair sem reparar).
   - No Capítulo $N-1$: Adicionar uma consequência menor impercetível (alguém bate na mesa, ou procura noutro casaco).
3. **Auditoria com Testes Automáticos:** Correr `python tests/run_story_tests.py` para certificar que os ficheiros mantêm linearidade temporal e referência de proveniência.
