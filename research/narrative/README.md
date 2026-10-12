# Investigação narrativa

Esta pasta reúne investigação usada para orientar a escrita da fanfic. O objetivo não é transformar uma teoria de estrutura numa receita, mas dar à escrita um conjunto de modelos que possam ser escolhidos conforme a história.

## Princípio central

Uma estrutura narrativa deve **servir a história**, não obrigar a história a caber num molde.

Para este projeto, a unidade mais importante é:

**personagem com intenção → ação/escolha → obstáculo/conflito → mudança → consequência**

Uma boa estrutura de episódio ou arco deve também permitir identificar onde a situação muda de forma significativa, como a tensão sobe/desce e que estado fica estabelecido para o que vem depois.

## Papers principais

### 1. Riedl & Young — Narrative Planning: Balancing Plot and Character

Riedl e Young defendem dois requisitos centrais para uma narrativa compreensível: progressão causal do enredo e credibilidade das personagens. O modelo IPOCL procura explicar as ações através de intenções e objetivos das personagens, em vez de tratar os acontecimentos apenas como uma sequência que “tem de acontecer”.

Fonte: Riedl, M. O., & Young, R. M. (2010). *Narrative Planning: Balancing Plot and Character*. Journal of Artificial Intelligence Research, 39, 217–268. DOI: 10.1613/jair.2983.

Aplicação no projeto:
- Cada mudança importante deve ter uma causa identificável.
- Quando uma personagem faz algo relevante, deve ser possível explicar o que ela queria alcançar.
- Uma personagem não deve agir apenas para transportar o enredo para a próxima cena.
- Conflitos devem nascer de objetivos incompatíveis, informação incompleta, restrições ou consequências.

### 2. O'Neill & Riedl — Dramatis: A Computational Model of Suspense

O trabalho modela suspense a partir da capacidade do público de imaginar um plano para evitar um resultado negativo e da probabilidade percebida de esse plano funcionar. Isto torna o suspense mais concreto: não é simplesmente “algo mau vai acontecer”, mas “há um resultado em risco e existe incerteza sobre se a personagem conseguirá evitá-lo”.

Fonte: O'Neill, B., & Riedl, M. (2014). *Dramatis: A Computational Model of Suspense*. AAAI Conference on Artificial Intelligence, 28(1). DOI: 10.1609/aaai.v28i1.8836.

Aplicação no projeto:
- Dar às personagens algo que elas tentam conseguir ou evitar.
- Tornar visível o que pode ser perdido.
- Manter incerteza relevante sobre o resultado.
- Não confundir suspense com intensidade constante: pausas e alívio também fazem parte do ritmo.

### 3. Fan, Lewis & Dauphin — Strategies for Structuring Story Generation

Fan, Lewis e Dauphin mostram que geração narrativa pode beneficiar de uma representação hierárquica: primeiro estruturar ações e entidades, depois realizar o texto. Os resultados favorecem decomposições que melhoram coerência e diversidade.

Fonte: Fan, A., Lewis, M., & Dauphin, Y. (2019). *Strategies for Structuring Story Generation*. ACL 2019, 2650–2660. DOI: 10.18653/v1/P19-1254.

Aplicação no projeto:
- Separar decisões de história de decisões de frase.
- Para episódios longos, definir primeiro acontecimentos e relações; escrever a prosa depois.
- Evitar improvisar dezenas de cenas sem saber qual mudança cada uma produz.
- Tratar personagens e acontecimentos como entidades persistentes, não como objetos descartáveis de uma cena.

### 4. Yao et al. — Plan-and-Write: Towards Better Automatic Storytelling

Este trabalho compara geração com e sem um plano explícito da linha de acontecimentos. A inclusão do storyline planning melhora diversidade, coerência e aderência ao tema em avaliações humanas e automáticas.

Fonte: Yao, L., Peng, N., Weischedel, R., Knight, K., Zhao, D., & Yan, R. (2019). *Plan-and-Write: Towards Better Automatic Storytelling*. AAAI 2019, 7378–7385. DOI: 10.1609/aaai.v33i01.33017378.

Aplicação no projeto:
- Antes de escrever um episódio substancial, estabelecer o estado inicial, a trajetória de acontecimentos e o estado final pretendido.
- Rever o plano quando uma descoberta narrativa importante o tornar pior.
- Não assumir que planear significa fixar tudo: o plano é uma hipótese que pode ser refinada.

### 5. Boyd, Blackburn & Pennebaker — The Narrative Arc

A análise de cerca de 40.000 narrativas encontrou padrões consistentes em três processos: *staging*, progressão do enredo e tensão cognitiva. O trabalho dá suporte empírico à ideia de que histórias tendem a mudar não só por acontecimentos, mas também pela forma como tensão e informação são distribuídas.

Fonte: Boyd, R. L., Blackburn, K. G., & Pennebaker, J. W. (2020). *The narrative arc: Revealing core narrative structures through text analysis*. Science Advances, 6(32), eaba2196. DOI: 10.1126/sciadv.aba2196.

Aplicação no projeto:
- Não começar com o máximo de conflito; primeiro estabelecer contexto suficiente para o público saber o que importa.
- Pensar no posicionamento relativo de progressão e tensão.
- Verificar se a história tem momentos de subida, queda, transformação e recuperação em vez de uma linha emocional plana.
- Não tratar estes padrões como obrigação: o próprio estudo não encontrou relação simples entre aderir a uma estrutura normativa e popularidade.

### 6. Tian et al. — Are Large Language Models Capable of Generating Human-Level Narratives?

O estudo compara narrativas humanas e narrativas de LLMs usando arcos, turning points e dimensões afetivas como *arousal* e *valence*. Os autores encontram uma tendência dos LLMs para histórias excessivamente homogéneas e positivas, com menos tensão e diversidade estrutural. A integração explícita dessas dimensões melhora a diversidade, suspense e arousal no sistema estudado.

Fonte: Tian, Y., Huang, T., Liu, M., Jiang, D., Spangher, A., Chen, M., May, J., & Peng, N. (2024). *Are Large Language Models Capable of Generating Human-Level Narratives?* EMNLP 2024, 17659–17681. DOI: 10.18653/v1/2024.emnlp-main.978.

Aplicação no projeto:
- Não resolver automaticamente todo conflito com reconciliação ou sucesso.
- Variar o movimento emocional entre cenas.
- Procurar turning points reais, não apenas novas informações.
- Aceitar finais de episódio ambíguos, desconfortáveis ou parcialmente negativos quando forem mais coerentes.

### 7. Ma et al. — Text-to-Text Automatic Story Generation: A Survey

A revisão de 57 trabalhos recentes destaca que, apesar dos avanços dos LLMs, coerência narrativa, consistência das personagens, diversidade e controlo do enredo continuam a ser problemas centrais.

Fonte: Ma, Y., Susilo, R., Haslum, P., & Suominen, H. (2026). *Text-to-Text Automatic Story Generation: A Survey*. Proceedings of EACL 2026 Student Research Workshop, 514–527. DOI: 10.18653/v1/2026.eacl-srw.39.

Aplicação no projeto:
- Tratar coerência e continuidade como problemas permanentes, não como uma revisão final.
- Manter estado persistente das personagens e timeline.
- Avaliar a história em múltiplas dimensões: causalidade, consistência, estrutura, tensão e desenvolvimento de personagem.

## Estruturas narrativas como lentes

### Three-act / quatro atos / cinco atos

Podem ser usados para verificar distribuição geral de setup, complicação, mudança e resolução. Não devem ser usados para decidir automaticamente quantas cenas a história precisa.

### Hero's Journey

É particularmente útil quando a história é organizada em torno de transformação e retorno de uma personagem, mas é menos apropriada para histórias ensemble ou episódios centrados em relações.

### Save the Cat / beats

Pode funcionar como checklist de ritmo para determinados géneros, mas os *beats* são convenções de craft, não resultados científicos necessários para uma boa história.

### Freytag e formas de arco

Úteis para pensar em subida, clímax e queda, desde que não se confunda a curva abstrata com o significado causal da história.

### Kishōtenketsu

É uma alternativa útil para episódios cujo interesse depende mais de desenvolvimento, contraste ou revelação do que de conflito crescente. Não deve ser tratado como uma variante “obrigatória” de 4 atos.

### Emotional arcs

Os arcos emocionais podem ser acompanhados separadamente do enredo: uma personagem pode conseguir objetivamente o que quer enquanto emocionalmente piora, ou falhar externamente enquanto melhora numa relação.

## Regra operacional para episódios

Antes de escrever um episódio relevante, responder apenas ao necessário:

1. **Estado inicial:** o que está estável?
2. **Intenções:** o que cada personagem relevante quer agora?
3. **Pressão:** o que dificulta esses objetivos?
4. **Turning point:** que acontecimento muda materialmente a situação?
5. **Consequência:** o que passa a ser verdade depois?
6. **Trajetória emocional:** onde começa e termina a tensão/estado emocional?
7. **Continuidade:** que informação ou mudança precisa sobreviver ao episódio seguinte?

Não é necessário preencher todos os campos com a mesma profundidade. O objetivo é impedir que a estrutura substitua a história.

## Como esta investigação será usada

Quando a IA trabalhar na história, deve:
- preferir causalidade e intenção a coincidências convenientes;
- escolher uma estrutura apropriada ao episódio em vez de aplicar sempre a mesma;
- planear acontecimentos antes de gerar longos blocos de prosa;
- procurar turning points e consequências;
- variar tensão e estado emocional;
- manter continuidade e estado persistente;
- rejeitar a tendência de “tudo fica bem” quando o conflito narrativo exige um custo.

Estas regras são **orientação de escrita**, não canon da fanfic. Podem ser revistas à medida que o projeto encontra uma voz própria.


## Escrita com IA e diálogo natural

A estrutura narrativa não chega para produzir prosa convincente. Antes da redação, consulte também:

- [Natural Dialogue Standard](../../canon/narrative/DIALOGUE_NATURALNESS_STANDARD.md) — critérios operacionais para intenção, subtexto, voz, ritmo, idade e revisão de diálogos.
- [AI Writing Tool Selection and Evaluation](AI_WRITING_TOOL_SELECTION.md) — fontes sobre avaliação de escrita criativa, comparação cega de modelos e um fluxo de trabalho baseado no OpenWrite já configurado, sem comprar novas ferramentas antes de demonstrar necessidade.
- [Season 1 Relationship Pacing](../../canon/narrative/SEASON_1_RELATIONSHIP_PACING.md) — evolução gradual e friendship-first de Nathan e Alex.

- [Opening Calendar Audit](OPENING_CALENDAR_AUDIT.md) — dates verified against the archived Seattle Public Schools calendar, the LAUSD 2009–10 calendar, and the original *Modern Family* Season 1 air dates; distinguishes source-backed dates from assumptions.

- [Character Naming Standard](../../canon/narrative/CHARACTER_NAMING_STANDARD.md) — cohort/country-appropriate frequency sources, random name selection, duplicate avoidance and family-name continuity.
- [Character Name Registry](../../canon/characters/CHARACTER_NAME_REGISTRY.md) — author-locked names, retired names, random-draw audit and the pending protagonist surname choice.
