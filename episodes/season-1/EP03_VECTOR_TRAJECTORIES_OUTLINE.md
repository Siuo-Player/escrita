# Season 1, Episode 3 — Vector Trajectories and Street Physics

<!-- WD-001 -->
<!-- WD-002 -->
<!-- WD-003 -->
<!-- WD-004 -->

Status: EXPANDED OUTLINE / WORKING  
Updated: 2026-11-19

## Story window

**16–31 October 2009**

Drafting references: [Dialogue Naturalness Standard](../../canon/narrative/DIALOGUE_NATURALNESS_STANDARD.md), [Season 1 Relationship Pacing](../../canon/narrative/SEASON_1_RELATIONSHIP_PACING.md), [Prop and Clue Registry](../../canon/narrative/PROP_AND_CLUE_REGISTRY.md), [Foreknowledge Intervention Policy](../../canon/narrative/FOREKNOWLEDGE_INTERVENTION_POLICY.md).

Target finished length: **10,000–14,000+ words**.

---

## Central movement

**A inteligência abstrata colide com o mundo físico.**

Nathan conseguiu fazer os algoritmos de *flow field* navegarem com sucesso no telemóvel, mas agora precisa de física espacial e deteção de colisões sólidas sem estourar o limite de CPU do processador Cortex-A8 de 600 MHz do iPhone 3GS. Simultaneamente, o seu isolamento social em Los Angeles continua a abrir fissuras orgânicas: Luke Dunphy entra na sua vida através de um incidente cómico com uma bola e um adereço perdido no parque; Alex começa a vê-lo como o único colega com quem pode falar sem filtros nem condescendência; e Haley cataloga-o apressadamente à porta de casa dos Dunphys.

---

## Persistent threads

### A — Nathan / Jogo (Trama Principal)
Física 2D de grelha regular e colisões AABB (Axis-Aligned Bounding Box) → eliminação de cálculos de raiz quadrada dispendiosos no ciclo principal de renderização → primeiro nível completo jogável a 60 FPS constantes.

### B — Nathan + Alex (Subtrama Relacional 1)
O teste intercalar de ciências da escola acelera a ansiedade de Alex. Nathan recusa alimentar rivalidades estéreis de notas e oferece uma presença serena e pragmática; Alex repara nas equações vetoriais do seu caderno [CLUE-002].

### C — Nathan + Luke Dunphy (Subtrama Relacional 2)
Primeiro encontro direto a 22 de outubro no parque desportivo. Luke tenta usar uma catapulta caseira para devolver a bola de futebol de Nathan [PROP-003] por cima da vedação e encontra o chaveiro com pendente de bússola de Nathan caído na erva [CLUE-001].

### D — Callahan Family & Bairro
Clifford e Heather ajustam-se ao ritmo executivo da Califórnia; preparação do primeiro Halloween numa rua de subúrbio onde a vizinhança leva decorações a sério.

### E — Modern Family AU em Paralelo
*Coal Digger* (21 de outubro) e *Run for Your Wife* (28 de outubro) decorrem nas suas datas históricas, intersectando Nathan apenas em momentos quotidianos não forçados.

---

## Cenas e Cronologia Linear

### 16 de Outubro (Sexta-feira) — Otimização de Colisões
- **Contexto:** Quarto de Nathan, fim de tarde. O MacBook Pro 15" [PROP-001] compila o novo gestor de colisões espaciais.
- **Conflito:** As entidades no ecrã colidem entre si e encravam nos cantos dos obstáculos estáticos.
- **Ação:** Nathan substitui o teste exato de distâncias euclidianas por uma partição espacial em células de 32x32 pixels, poupando centenas de chamadas trigonométricas por segundo.
- **Consequência:** A simulação estabiliza; primeira vitória de engenharia palpável.

### 19 de Outubro (Segunda-feira) — O Caderno de Esboços na Biblioteca
- **Contexto:** Biblioteca escolar durante a hora de estudo autónomo.
- **Presença de Alex:** Alex está a rever resumos intensivos para o teste intercalar de biologia e química.
- **Interação:** Ela olha por cima da mesa e repara no caderno de Nathan [CLUE-002], aberto com diagramas de vetores de velocidade e interpolação linear:
  - *"Isso não é do currículo de 8º ano."*
  - Nathan, cauteloso e com receio habitual de soar arrogante, responde: *"É só uma forma de calcular para onde uma coisa se move sem ter de perguntar a cada pixel o que fazer."*
  - Alex analisa o esboço em silêncio durante três segundos antes de admitir que a lógica é elegante. É o primeiro momento em que Alex reconhece nele um intelecto que não tenta competir com o dela para se exibir.

### 21 de Outubro (Quarta-feira) — Paralelo com *Coal Digger*
- **Canon AU:** Conflito familiar na casa dos Pritchett sobre o comentário de Luke a respeito de Gloria ser "coal digger".
- **Nathan:** Totalmente alheio ao drama doméstico dos Pritchett/Dunphy. Janta com Heather e Clifford na cozinha; conversa familiar sobre as diferenças de trânsito e vizinhança entre Seattle e Los Angeles. Nathan preserva o espaço mental da família sem forçar qualquer intervenção desnecessária.

### 22 de Outubro (Quinta-feira) — A Bola, a Fisga e a Bússola Perdida [Luke Dunphy] <!-- EVT-014 | 2009-10-22 | 2009-10-22 -->
- **Contexto:** Fim de tarde no parque municipal adjacente ao campo de futebol.
- **Ação Causal:**
  - Nathan faz exercícios de controlo de bola e remates à baliza com as suas chuteiras e bola de treino [PROP-003].
  - Um remate com demasiado efeito salta por cima da rede de proteção e rola para junto do caminho pedonal.
  - Luke Dunphy (10 anos), que vinha a testar uma engenhoca feita com elásticos de borracha e um garfo de ramos de árvore, decide "catapultar" a bola de volta em vez de a chutar como uma pessoa normal.
  - A bola sobe torta e atinge um arbusto. Ao procurar a bola nos ramos baixos, Luke encontra o chaveiro com o pendente de bússola de metal de Nathan [CLUE-001], que caíra ali dias antes.
  - Luke aproxima-se da vedação: *"Apanhei a tua bola. E acho que deixaste cair uma bússola de explorador antigo."*
  - Nathan agradece, genuinamente surpreso e aliviado: *"Obrigado. Pensei que a tinha perdido na mudança."*
  - Luke inspeciona Nathan com curiosidade infantil desprovida de vergonha: *"És o rapaz novo da rua de baixo que corre sempre à mesma velocidade? O meu pai diz que pareces um robô da maratona."*
- **Consequência:** Fica estabelecido o primeiro contacto direto e bem-humorado entre Nathan e Luke. Luke ganha simpatia imediata por Nathan não ter gozado com a fisga dele.

### 24 de Outubro (Sábado) — A Livraria de Westwood e o Livro Raro [PROP-006] <!-- EVT-015 | 2009-10-24 | 2009-10-24 -->
- **Contexto:** Manhã de sábado. Nathan acompanha Heather num recado ao bairro universitário de Westwood, perto da UCLA.
- **Observação / Génese:** Enquanto Heather compra material de escritório, Nathan espreita uma livraria tradicional de alfarrabistas (*Second Chance Books*). Na montra de livros científicos antigos em segunda mão, avista uma edição de 1964 com capa de tecido vermelho: *The Feynman Lectures on Physics, Volume 1* [PROP-006]. Nathan repara no livro e lembra-se de uma conversa informal na biblioteca onde Alex mencionou querer consultar as notas de Feynman sobre mecânica. Nathan não compra o livro de imediato porque ainda quer verificar as suas poupanças, mas memoriza a localização na prateleira.

### 28 de Outubro (Quarta-feira) — A Corrida Matinal e Phil Dunphy
- **Canon AU:** *Run for Your Wife*. Phil e Claire disputam uma corrida a pé pelo bairro para provar quem está em melhor forma física.
- **Interseção:** Nathan faz a sua corrida matinal de condicionamento (6:45 da manhã).
- Phil surge a ofegar com fita na cabeça e passada desajeitada. Nathan abranda ligeiramente, acena com respeito e diz: *"Bom ritmo, Sr. Dunphy."*
- Phil sente-se validado no seu espírito competitivo e tenta um *high-five* em movimento, quase tropeçando no passeio. A interação é breve, limpa e natural.

### 29 de Outubro (Quinta-feira) — À Porta dos Dunphys [Haley Dunphy] <!-- EVT-016 | 2009-10-29 | 2009-10-29 -->
- **Contexto:** Fim de tarde de quinta-feira. Nathan vai a casa dos Dunphys devolver uma chave sextavada que Luke tinha deixado cair junto ao banco do parque.
- **Ação:** Nathan toca à campainha. Quem abre a porta é Haley (15 anos), maquilhada e apressada, ao telemóvel com uma amiga.
- Haley olha para Nathan de cima a baixo: *"Sim? Estás à procura da Alex? Ela está no quarto a sofrer com um livro qualquer."*
- Nathan: *"Não, é para o Luke. Ele deixou isto cair no relvado do parque."*
- Haley pega na chave com desdém casual: *"Certo, o clube de inventores malucos do Luke. Eu entrego-lhe. Obrigada, miúdo."*
- **Consequência:** Primeiro contacto com Haley. Haley vê Nathan como um rapaz educado e tímido dos círculos dos irmãos mais novos; Nathan mantém postura cortês e não reage à altivez típica de Haley.

### 31 de Outubro (Sábado) — Halloween e Marco de Engenharia
- **Contexto:** Noite de Halloween. Crianças do bairro mascaradas na rua; Heather distribui doces à porta.
- **Resultado Técnico:** No quarto, Nathan compila o build v0.8 do jogo no iPhone 3GS [PROP-004].
- O jogo corre agora 10 minutos seguidos sem quebras de framerate e sem crashes de memória.
- Nathan desce à cozinha, aceita um chocolate da mãe e sorri: pela primeira vez desde que chegou à Califórnia, sente que a nova vida tem raízes sólidas.

---

## Alterações de Estado Persistente no Final do EP03

1. **Relação Nathan / Luke:** Estabelecida organicamente através do incidente da bola e do adereço [CLUE-001]. Luke vê Nathan como vizinho amigo e acessível.
2. **Relação Nathan / Haley:** Primeiro contacto registado; dinâmica de "irmã mais velha distante" estabelecida sem forçar intimidade precoce.
3. **Relação Nathan / Alex:** Transição de curiosidade superficial para admiração intelectual consciente através do caderno de vetores [CLUE-002].
4. **Estado do Jogo:** Motor 2D e deteção de colisões concluídos e operacionais a 60 FPS no iPhone 3GS. Próxima etapa: otimização de RAM e preparação do processo de submissão à Apple no EP04.

---

## Cortes Editoriais e Quebras de Perspetiva (Director's POV Cuts)

1. **Corte Editorial 1 (22 de Outubro — Quintal dos Dunphy): Perspetiva de Luke Dunphy.**
   - Luke sobe à casa da árvore no quintal com a bússola de metal antiga [CLUE-001] que encontrou nos arbustos. Guarda-a numa caixa de sapatos com arames e pilhas gastas, convencido de que o vizinho Nathan é um agente secreto que corre à mesma velocidade para não acionar minas terrestres. O raciocínio caótico e carinhoso de Luke em pleno contraste com a lógica matemática de Nathan.
2. **Corte Editorial 2 (29 de Outubro — Quarto de Haley Dunphy): Perspetiva de Haley Dunphy.**
   - Haley fecha a porta após receber a chave devolvida por Nathan. Volta para a chamada ao telemóvel com a amiga e comenta casualmente: *"A Alex agora tem um rapaz do clube de nerds que vem cá a casa devolver parafusos com calças impecavelmente passadas a ferro. Ele parece saído de um filme clássico dos anos cinquenta."* O detalhe exterioriza como a família perceciona Nathan sem que ele saiba.
