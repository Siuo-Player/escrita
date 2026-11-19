# Season 1, Episode 4 — Memory Profiles and Hardware Limits

Status: EXPANDED OUTLINE / WORKING  
Updated: 2026-11-19

## Story window

**01–18 November 2009**

Drafting references: [Dialogue Naturalness Standard](../../canon/narrative/DIALOGUE_NATURALNESS_STANDARD.md), [Season 1 Relationship Pacing](../../canon/narrative/SEASON_1_RELATIONSHIP_PACING.md), [Prop and Clue Registry](../../canon/narrative/PROP_AND_CLUE_REGISTRY.md), [Foreknowledge Intervention Policy](../../canon/narrative/FOREKNOWLEDGE_INTERVENTION_POLICY.md).

Target finished length: **10,000–14,000+ words**.

---

## Central movement

**A disciplina do hardware e a primeira partilha de espaço íntimo.**

O código do jogo funciona, mas a arquitetura móvel de 2009 impõe um limite impiedoso: a memória RAM ativa raramente pode ultrapassar 40 MB sem o sistema operativo abortar o processo com um sinal de baixa memória. Nathan tem de perseguir fugas de memória e reutilizar buffers em C++ puro. No plano pessoal, as barreiras de isolamento que Nathan ergueu começam a ruir: Alex visita pela primeira vez a casa dos Callahan para uma sessão de estudo colaborativo e vê o seu espaço de trabalho; Jay Pritchett reconhece nele a postura séria de quem sabe manusear ferramentas; e Phil Dunphy ganha uma dívida de gratidão tecnológica.

---

## Persistent threads

### A — Nathan / Jogo (Trama Principal)
Perfilagem de memória com o Instruments da Apple sob Mac OS X Snow Leopard → substituição de alocações dinâmicas contínuas por uma pool estática de entidades de jogo → submissão do binário final à aprovação da Apple na App Store.

### B — Nathan + Alex (Subtrama Relacional 1)
Primeira sessão de estudo na casa de Nathan (06 de novembro). Alex repara na organização quase militar da secretária de Nathan, no MacBook Pro [PROP-001] e no iPhone 3GS de testes [PROP-004]. Nathan admite a sua insegurança em relação à receção do jogo.

### C — Nathan + Jay Pritchett (Subtrama Relacional 2)
Primeiro encontro no feriado do Veterans Day (11 de novembro) numa loja tradicional de ferragens e bricolagem em Santa Monica. Jay observa a seleção de esquadrias e parafusos de aço de Nathan para reforçar a mesa de trabalho e elogia a solidez da escolha.

### D — Nathan + Phil Dunphy (Subtrama de Vizinhança)
Phil passa um fim de tarde frustrado a tentar emparelhar um comando universal infravermelho e calibrar o receptor de som surround da sala dos Dunphys. Nathan, a caminho de casa após um treino, identifica o conflito de frequência em dois minutos e ajuda Phil a manter o orgulho intacto perante Claire.

### E — Modern Family AU em Paralelo
*En Garde* (04 de novembro - esgrima de Manny) e *Great Expectations* (18 de novembro - o aniversário de casamento de Phil e Claire com a convidada surpresa) decorrem paralelamente, ancorando a cronologia no universo canónico.

---

## Cenas e Cronologia Linear

### 02 de Novembro (Segunda-feira) — O Alerta de Memória
- **Contexto:** Quarto de Nathan, 21:00. O Instruments do Xcode acusa um consumo crescente de RAM no iPhone 3GS [PROP-004] ao fim de 15 minutos de execução.
- **Ação Técnica:** Nathan percebe que os nós de pesquisa do algoritmo de caminhos estão a ser instanciados com `new` e destruídos com `delete` centenas de vezes por frame, fragmentando o espaço de heap.
- **Solução:** Desenha uma estrutura pré-alocada de *object pool* de tamanho fixo em C++, eliminando qualquer alocação durante o gameplay ativo.

### 04 de Novembro (Quarta-feira) — Paralelo com *En Garde*
- **Canon AU:** Manny participa na competição de esgrima e a família celebra o seu sucesso desportivo temporário.
- **Nathan:** Na escola, durante o intervalo, Nathan e Maxwell Whitaker analisam o próximo adversário da equipa de futebol escolar. Maxwell nota que Nathan tem estado mais calado que o habitual devido ao esforço de programação, mas no treino de campo Nathan continua a cumprir o seu papel tático com perfeição.

### 06 de Novembro (Sexta-feira) — Alex na Casa dos Callahan <!-- EVT-017 | 2009-11-06 | 2009-11-06 -->
- **Contexto:** Tarde chuvosa. Alex vem a casa de Nathan para finalizar o relatório conjunto de física experimental da escola.
- **Observação do Espaço:** Alex entra no quarto de Nathan e fica surpreendida:
  - Não há posters desportivos vistosos nem desordem típica de rapaz de 13 anos.
  - A bancada tem o MacBook Pro [PROP-001] ligado ao telemóvel de testes [PROP-004], cabos organizados, o caderno de vetores [CLUE-002] e, pousada ao lado da base do ecrã, a peça de xadrez em madeira escura [CLUE-003] que Alex observa distraidamente enquanto tira os cadernos da mochila.
- **Diálogo:**
  - Alex pega delicadamente no telemóvel de testes onde corre o build: *"É isto em que tens trabalhado todas as tardes na biblioteca?"*
  - Nathan, corando ligeiramente e baixando o olhar: *"É só um projeto pequeno de simulação. Não é grande coisa."*
  - Alex joga durante dois minutos, esquivando-se aos inimigos vermelhos que antecipam os seus movimentos através do campo vetorial. Ela larga o aparelho e fita Nathan com seriedade analítica: *"Estás a brincar comigo? Isto é mais avançado do que qualquer aplicação comercial que vi na loja da Apple. Porque é que dizes sempre que não é nada?"*
  - Nathan engole em seco e desvia a conversa para o relatório de física: *"Temos de entregar o gráfico de incertezas na segunda-feira."*
- **Consequência:** A admiração de Alex transforma-se em genuíno respeito técnico e profunda curiosidade emocional sobre os motivos que levam Nathan a esconder o seu talento.

### 07 de Novembro (Sábado) — A Experiência de Velocidade de Phil e o Cronómetro [PROP-005] <!-- EVT-018 | 2009-11-07 | 2009-11-07 -->
- **Contexto:** Manhã de sábado ensolarada no passeio em frente à casa dos Callahan.
- **Incidente Cómico:** Phil Dunphy e Luke estão no jardim com patins em linha e uma fita métrica industrial. Phil tenta provar uma "lei de aerodinâmica doméstica" que viu na televisão e precisa de medir a velocidade de Luke em centésimos de segundo. O telemóvel de Phil descarregou a bateria.
- **Ação:** Nathan sai para correr com o seu cronómetro digital Casio [PROP-005]. Phil avista o relógio: *"Nathan! O homem com o tempo atómico no pulso! Podes emprestar-me o cronómetro por dez minutos antes que a Claire venha espreitar à janela?"* Nathan empresta o Casio cortesmente e ajuda a marcar as três partidas com precisão, salvando o dia de Phil e Luke.

### 11 de Novembro (Quarta-feira - Veterans Day) — Jay Pritchett na Loja de Ferragens <!-- EVT-019 | 2009-11-11 | 2009-11-11 -->
- **Contexto:** Manhã de feriado. Nathan precisa de suportes de aço para elevar o monitor externo na sua secretária e visita uma drogaria/ferragens antiga em Santa Monica.
- **Encontro:** Jay Pritchett está na mesma secção à procura de rebites e lixas de acabamento.
  - Jay vê um miúdo de 13 anos a comparar a espessura de cantoneiras galvanizadas e a testar a rosca dos parafusos com os dedos.
  - Jay aproxima-se: *"A maioria dos miúdos da tua idade agora só quer comprar plástico que quebra na primeira semana."*
  - Nathan responde calmamente: *"Se a madeira empenar com o peso do monitor, o plástico cede na junta. O aço aguenta a tensão."*
  - Jay solta uma gargalhada curta e aprobatória: *"Amén para isso, filho. Sou o Jay."*
  - Nathan aperta-lhe a mão com firmeza correta: *"Nathan Callahan. Bom dia, senhor."*
- **Consequência:** Jay fica com uma impressão excelente e duradoura de Nathan como um jovem com cabeça nos ombros e bom senso prático.

### 14 de Novembro (Sábado) — A Aquisição das Palestras de Feynman [PROP-006] <!-- EVT-020 | 2009-11-14 | 2009-11-14 -->
- **Contexto:** Tarde de sábado em Westwood. Nathan regressa à livraria *Second Chance Books* com as suas economias guardadas das prendas anteriores.
- **Ação:** Encontra o volume original de 1964 de *The Feynman Lectures on Physics* [PROP-006] com a capa vermelha ainda na secção de saldos por vinte e cinco dólares. Compra-o, leva-o para casa envolvido no saco de papel e guarda-o cuidadosamente na gaveta trancada da sua secretária, aguardando o momento oportuno para o oferecer a Alex no Natal sem gerar alarido.

### 15 de Novembro (Domingo) — Phil e a Cablagem da Sala
- **Contexto:** Fim de tarde de domingo. Nathan regressa a pé da papelaria e passa pela casa dos Dunphys.
- **Incidente:** Phil está no chão da sala de estar com a porta aberta, cercado por dezenas de cabos RCA e HDMI, a praguejar em voz baixa contra um manual de instruções bilingue.
- Nathan para junto ao degrau da entrada e pergunta cortesmente: *"Precisa de uma mão com a polaridade dos canais, Sr. Dunphy?"*
- Phil, aliviado por não ter de admitir a derrota a Claire, aceita. Em dez minutos, Nathan organiza o barramento de sinal e calibra a entrada óptica de áudio.
- Phil fica eufórico: *"És um mago, Nathan! Um verdadeiro Gandalf dos circuitos! A Claire não pode sonhar que não fui eu a decifrar isto à primeira."*
- Nathan sorri discretamente e garante que o segredo fica seguro.

### 18 de Novembro (Quarta-feira) — Submissão à Apple e *Great Expectations* <!-- EVT-021 | 2009-11-18 | 2009-11-18 -->
- **Canon AU:** Phil prepara a noite comemorativa de aniversário com a banda Spandau Ballet.
- **Marco de Nathan:** Às 23:15, no seu quarto, Nathan revê o checksum do pacote binário compilado.
- Clica no botão **Submit for Review** no portal do iOS Developer Center.
- Nathan recosta-se na cadeira. O coração bate rápido: o primeiro projeto independente está nas mãos dos revisores de Cupertino.

---

## Alterações de Estado Persistente no Final do EP04

1. **Relação Nathan / Jay Pritchett:** Primeiro contacto estabelecido com impressão de respeito mútuo por pragmatismo e qualidade de construção.
2. **Relação Nathan / Phil Dunphy:** Consolidação da cumplicidade técnica e simpatia de Phil.
3. **Relação Nathan / Alex:** Alex conhece o quarto e o projeto de Nathan; percebe a sua insegurança emocional e confronta-o sobre a autodesvalorização.
4. **Estado do Jogo:** Versão 1.0 completamente finalizada, com memória RAM estabilizada abaixo de 35 MB e submetida à Apple. Aguarda aprovação para lançamento no EP05.

---

## Cortes Editoriais e Quebras de Perspetiva (Director's POV Cuts)

1. **Corte Editorial 1 (06 de Novembro — Quarto de Nathan): Perspetiva de Alex Dunphy.**
   - Alex observa Nathan enquanto ele desce à cozinha para trazer dois copos de sumo de maçã. Sozinha no quarto dele por dois minutos, Alex aproxima-se da secretária: toca suavemente na peça de xadrez em madeira escura [CLUE-003], olha para as folhas com os testes de limites de memória e para o terminal Unix. Pela primeira vez, ela compreende a solidão e a disciplina quase cirúrgica que sustentam a modéstia de Nathan. O choque de perceber que alguém da sua idade é capaz de tanta profundidade sem necessidade de validação exterior.
2. **Corte Editorial 2 (11 de Novembro — Casa de Jay Pritchett): Perspetiva de Jay Pritchett.**
   - Jay está na sua oficina na garagem a lixar as esquadrias que comprou na loja de ferragens. Bebe um gole de cerveja e comenta com Gloria enquanto ela passa para entrar no carro: *"Conheci um rapaz na loja hoje. Treze anos. Sabia a espessura de parafusos de aço galvanizado e não olhou para um ecrã de telemóvel uma única vez. Se o Manny passasse duas semanas a aprender o valor de uma porca bem apertada em vez de escrever poemas em guardanapos, o mundo andava para a frente."* Gloria revira os olhos com afeto: *"Jay, deixa o meu menino em paz, ele é um poeta sensível!"*
