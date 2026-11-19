# Episódio 1 — Antes e Depois

**Janela Temporal:** 07 a 30 de Setembro de 2009  
**Status:** RASCUNHO EM PROSA (Movimento I)  
**Linhas Ativas:** Trama A (Jogo C++ / Flow Field), Trama B (Família Callahan / Mudança), Trama C (Futebol / Despedida de Seattle), Trama D (Chegada à Califórnia e Alex).

---

## MOVIMENTO I: 7 A 13 DE SETEMBRO — A VIDA ANTES DA MUDANÇA

### Cena 1 — 7 de Setembro de 2009 (Segunda-feira, Labor Day): O Aniversário e a Grelha

O silêncio das segundas-feiras de feriado tinha um peso diferente no noroeste do Pacífico. Do lado de fora da janela do primeiro andar, a névoa matinal de Seattle descia lenta por entre as copas escuras dos abetos, humedecendo o asfalto limpo da rua residencial. Não havia autocarros amarelos a travar nas esquinas nem passos apressados nos passeios. Era o *Labor Day*.

No quarto, o único som contínuo vinha da ventoinha metálica do computador e do clique ritmado das teclas mecânicas.

Nathan Callahan fez hoje treze anos.

Não havia balões pendurados no teto nem música comemorativa. Sobre a mesa de mogno maciço, impecavelmente alinhada junto à tomada de terra, o ecrã brilhante do portátil novo de quinze polegadas em alumínio escovado — o MacBook Pro unibody que o pai pousara sobre a sua secretária naquela mesma manhã com um aperto de mão firme e pragmático — exibia duas janelas lado a lado no Mac OS X Snow Leopard. À esquerda, o editor de texto com centenas de linhas de C++ estritamente identadas; à direita, a janela de terminal do Unix e a vista de depuração gráfica do OpenGL.

Na janela gráfica, uma grelha bidimensional de sessenta por quarenta células verdes e cinzentas continha dois pontos brilhantes. Um quadrado azul estático e uma entidade vermelha que serpenteava cautelosamente pelos obstáculos cinzentos, calculando o nó seguinte de cada vez que o ponteiro do rato se deslocava.

Nathan pousou a chávena de água morna na base de cortiça e suspirou, esfregando a ponta do nariz.

O algoritmo A-estrela funcionava sem falhas para uma entidade. Mas no canto inferior esquerdo do ecrã, o monitor de desempenho do compilador não mentia: quando ele tentava aumentar a simulação para cinquenta agentes a calcularem a sua própria rota ao mesmo tempo, a utilização do processador subia para lá dos setenta por cento e a taxa de fotogramas descia para uns miseráveis vinte e dois por segundo.

— O espaço de procura explode — murmurou para si mesmo, com a voz ligeiramente áspera de quem ainda não tinha falado em voz alta naquele dia. — Se cada agente calcular o seu próprio caminho do zero, a fila de prioridades esgota os ciclos de relógio antes de a física começar a desenhar.

Ele não estava a desenhar um jogo para um computador com refrigeração líquida e fonte de quinhentos watts. Estava a pensar num ecrã táctil com menos de dez centímetros de diagonal, uma bateria de iões de lítio que cabia no bolso e um processador ARM de seiscentos megahertz que aquecia se lhe pedissem para calcular divisões em vírgula flutuante vezes demais.

Afastou a cadeira. Tinha tempo. O desenvolvimento de software, tal como o condicionamento físico, não se resolvia a forçar a máquina quando ela pedia reestruturação de raiz.

Vestiu a camisola de treino de algodão cinzento, calçou os ténis de sola rasa e desceu as escadas de madeira sem fazer ranger os degraus.

No piso inferior, o cheiro a café moído e a torrada com manteiga vinha da cozinha. A mãe, Heather, estava sentada à bancada de granito com uma pasta de couro aberta e um maço de documentos profissionais grampeados, uma caneta de feltro na mão direita e uma caneca branca na esquerda. Tinha o cabelo castanho apanhado numa mola prática e olhou por cima dos óculos finos de leitura no momento em que Nathan entrou na divisão.

— Parabéns outra vez, Nathan — disse ela, com um tom calmo e afetuoso, pousando a caneta sobre a margem de um relatório financeiro. — Dormiste o suficiente? Ou ficaste a ver números até às três da manhã?

— Dormi sete horas e vinte minutos — respondeu Nathan, encostando-se ao rebordo do balcão e servindo-se de um copo de sumo de laranja natural. — O portátil novo compila o código três vezes mais depressa do que a torre antiga. Obrigado, mãe. A sério.

— Agradece ao teu pai. Ele passou meia hora ontem à noite a certificar-se de que a memória RAM instalada vinha de um lote fiável — Heather sorriu de lado, um sorriso perspicaz que conhecia bem as manias dos dois homens da casa. — Ele está no escritório a fechar uns telefonemas da costa oeste. Disse que o jantar hoje é às sete e meia. Queres convidar algum dos rapazes da equipa para comer bolo?

Nathan hesitou um milésimo de segundo. A pergunta era natural, mas tocou precisamente na ferida habitual que ele preferia manter oculta sob a sua rotina impecável. Os colegas de equipa do clube de futebol respeitavam-no; ouviam-no em campo quando ele corrigia a linha defensiva e batiam-lhe nas costas nos balneários depois de uma vitória. Mas ele nunca sabia como transitar dessa camaradagem atlética para o espaço privado de uma casa sem sentir que estava a forçar uma intimidade que ninguém tinha pedido.

— Eles têm planos de família por causa do fim de semana prolongado — disse ele, com tom neutro e convincente. — O treino oficial só recomeça na quarta-feira com o primeiro dia de aulas. Vou para o jardim fazer uns toques antes do almoço.

Heather fitou-o durante um segundo a mais, como se quisesse desmontar a desculpa polida, mas limitou-se a acenar com a cabeça.

— Não fures os canteiros de hortênsias. E traz a camisola para dentro se começar a chuviscar.

---

### Cena 2 — O Jardim e a Bola de Treino

No quintal das traseiras, a relva cortada estava fria sob a sola dos ténis. Nathan pegou na sua bola de treino de couro sintético, uma clássica bola branca com gomos hexagonais pretos que exibia marcas visíveis de relvados enlameados [PROP-003].

Começou com toques curtos: pé esquerdo, pé direito, coxa, peito, pé esquerdo outra vez. O ritmo era constante, metronómico.

Enquanto a bola subia e descia a quarenta centímetros do solo sem tocar na relva, a mente de Nathan continuava a dissecar a falha da grelha algorítmica.

*Se cinquenta agentes querem chegar ao mesmo ponto final, porque é que cinquenta agentes calculam cinquenta caminhos independentes?*

A pergunta ecoou com a precisão de um clique de interruptor.

*O destino é fixo. Os obstáculos são fixos. Em vez de calcular do agente para o objetivo... calcula-se do objetivo para todo o mapa. Uma única passagem em largura. Cada célula guarda um vetor direcional que aponta para o nó de menor custo. Um campo de fluxo.*

A bola caiu suavemente na ponta da sapatilha direita de Nathan, que a amorteceu com um movimento fluido, prendendo-a contra o tornozelo.

— *Flow field* — sussurrou ele para o ar húmido.

Não eram cinquenta pesquisas A-estrela por fotograma. Era uma única tabela de vetores pré-calculada em memória. Para cada entidade no ecrã, o custo de movimento passava a ser uma simples leitura de índice numa matriz: `direção = campo[x][y]`. Custo algorítmico quase nulo por entidade.

Nathan soltou a bola, chutou-a contra a mureta de pedra da sebe e recolheu o ressalto de primeira com o peito do pé. Pela primeira vez em semanas, a arquitetura de navegação do jogo parecia matematicamente inevitável.

---

### Cena 3 — O Jantar de Aniversário e a Fratura Causal

Às sete e meia da tarde, a mesa da sala de jantar dos Callahan estava posta com a louça de cerâmica sóbria dos dias festivos. O cheiro a frango assado com alecrim e batatas douradas preenchia a divisão.

Clifford Callahan ocupou a cabeceira da mesa. Tinha quarenta e quatro anos, constituição atlética sem excessos, cabelo castanho-escuro cortado curto com algumas hastes cinzentas nas fontes e o olhar direto de alguém habituado a analisar diagramas de arquitetura de sistemas e folhas de balanço trimestrais.

— O ecrã tem bom contraste? — perguntou Clifford, servindo água mineral no copo de Nathan.

— A resolução é de 1440 por 900 — respondeu Nathan de pronto. — O compilador da Apple já vem com suporte completo para a biblioteca gráfica e a gestão de energia desliga o núcleo secundário quando estou só no terminal. É perfeito.

Clifford assentiu com uma ligeira inclinação de cabeça, visivelmente satisfeito por o rapaz valorizar especificações técnicas reais em vez do prestígio da marca.

— A escola confirmou os horários para quarta-feira? — perguntou Clifford a Heather, enquanto cortava o assado.

— Sim — respondeu Heather, pegando na saladeira. — Oitavo ano. O Nathan fica na turma avançada de ciências e no programa de honra de álgebra. O treinador Reynolds ligou de manhã a confirmar que a braçadeira de capitão da equipa de outono continua reservada para ele.

Nathan sentiu um calor discreto no peito. Aquele era o seu mundo construído passo a passo: a liderança desportiva conquistada pelo esforço e visão de jogo, as notas que não davam trabalho porque a sua mente absorvia os conceitos com naturalidade cirúrgica, e a previsibilidade confortável da cidade onde sabia exatamente onde tudo ficava.

Foi nesse instante que Clifford pousou os talheres na borda do prato. Não com brusquidão, mas com aquele compasso de espera deliberado que os executivos usam antes de apresentar um memorando de reestruturação.

Olhou primeiro para Heather, que retribuiu o olhar com uma calma preparada de antemão — o sinal inequívoco de que a conversa já tinha acontecido entre os dois muito antes de chegar à mesa.

— Nathan — disse Clifford, com voz pausada e tranquila. — Lembras-te das reuniões de conselho de administração que tive em Los Angeles nas duas últimas semanas de agosto?

Nathan pestanejou, o copo de água suspenso a meio caminho da mesa.

— Sim. Disseste que a empresa estava a consolidar a divisão de infraestrutura e serviços de dados na costa sul.

— Exatamente — prosseguiu o pai. — A consolidação foi aprovada pelo conselho na sexta-feira à tarde. A direção executiva ofereceu-me a vice-presidência sénior de operações de engenharia na Califórnia.

Houve uma pausa de três segundos. O tique-taque do relógio de parede na sala de estar pareceu subitamente amplificado.

— Isso implica viagens frequentes? — perguntou Nathan, tentando manter o tom estritamente analítico que usava para problemas de lógica.

— Não, filho — respondeu Clifford, com os olhos fixos nos de Nathan, sem rodeios nem condescendência. — Implica mudarmos de residência. Toda a equipa executiva vai ficar baseada na área da Grande Los Angeles. Já temos o pacote de relocalização ativado pela empresa. Partimos na próxima semana.

O ar na sala de jantar pareceu arrefecer dois graus.

Nathan não gritou, não bateu na mesa nem deixou cair o copo. A sua mente, programada pela disciplina física e pela timidez interior, retraiu-se instantaneamente para dentro da sua couraça habitual de contenção.

Mas a cadeia causal que sustentava a sua vida desmoronou-se em silêncio.

O primeiro dia de aulas em Seattle era dali a quarenta e oito horas. A capitania da equipa de futebol. Os professores que já o conheciam e não lhe exigiam conversas fiadas nem exibições artificiais de simpatia. Os colegas de equipa com quem tinha um entendimento mudo e seguro no relvado.

Tudo isso tinha acabado de ser apagado por uma decisão corporativa tomada numa sala de reuniões com ar condicionado a dois mil quilómetros de distância.

— E a escola? — perguntou Nathan, a sua voz saindo mais baixa do que pretendia. — As aulas começam esta semana em todo o país.

— O calendário escolar na Califórnia é compatível — interveio Heather, estendendo a mão para pousá-la com suavidade sobre o antebraço de Nathan. — A empresa contratou uma consultora de relocalização familiar. Já foste aceite numa excelente escola pública na zona oeste de Los Angeles, uma das melhores do distrito. Entras na quarta-feira seguinte, dia dezasseis de setembro. Só perdes a primeira semana de aulas, e o teu pai e eu sabemos que apanhas a matéria em dois dias.

Nathan olhou para o prato. O frango assado tinha perdido o sabor.

— E o futebol?

— Há equipas locais e programas interescolares excelentes — disse Clifford, firme mas atento. — Um bom jogador afirma-se em qualquer relvado, Nathan. O que tu tens não depende do código postal do campo.

Nathan assentiu lentamente com a cabeça, porque sabia que contrapor argumentos de logística contra uma promoção corporativa de primeiro escalão era matematicamente fútil.

— Compreendo — disse ele, forçando um tom cortês. — Vou começar a arrumar os livros amanhã à tarde.

Naquela noite, depois de Heather ter cantado os parabéns com um pequeno bolo de limão e de as luzes do piso térreo se apagarem, Nathan ficou no escuro do seu quarto, sentado na beira da cama, com o ecrã do MacBook Pro aceso em modo de poupança de energia.

Los Angeles.

A palavra não trazia apenas sol, trânsito e palmeiras.

Para Nathan Callahan, trazia o conhecimento vívido e aterrorizador de uma série de televisão que ele vira e revira numa vida passada: *Modern Family*. As casas dos Dunphy, dos Pritchett, as ruas do subúrbio, as pessoas de carne e osso cujas vidas, dramas e falhas ele conhecia ao milímetro de cor.

Até agora, esse conhecimento fora uma memória estática, um arquivo de ficção arquivado no fundo da mente.

A partir de 16 de setembro, aquele arquivo deixaria de ser ficção. Passaria a ser a sua vizinhança.

E com a certeza perturbadora de quem compreende sistemas complexos, Nathan sabia que a sua simples respiração no mesmo ar iria alterar a trajetória de todos eles para sempre.
