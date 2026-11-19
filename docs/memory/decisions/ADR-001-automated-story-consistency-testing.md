# ADR-001: Validação Automatizada de Consistência e Linearidade Narrativa

- **Data:** 2026-11-19
- **Status:** ACEITE / EM EXECUÇÃO
- **Contexto:** 
  O projeto de ficção *escrita* assenta em continuidade rigorosa, calendário gregoriano exato (ano letivo 2009–2010), progressão causal linear sem paradoxos, introdução faseada de personagens e presença obrigatória de múltiplas linhas de enredo paralelas por capítulo. A inspeção manual de ficheiros markdown de grande dimensão torna-se vulnerável a anacronismos, saltos de datas impercetíveis e episódios desprovidos de progressão persistente (*fillers*).
- **Decisão:**
  Implementar uma suite de testes automatizados em Python (`tests/`) executável via `unittest` ou CLI dedicado (`tests/run_story_tests.py`), que analisa estaticamente os ficheiros de cronologia, outlines e rascunhos de episódios para verificar:
  1. **Linearidade Temporal:** Sequência estritamente monótona de datas e conformidade com os dias de semana de 2009 (ex.: 07/09/2009 = Segunda-feira).
  2. **Estrutura Multi-Trama (Política Anti-Filler):** Todo o episódio deve declarar pelo menos 3 tramas ativas (1 principal + no mínimo 2 secundárias com outros personagens) e registar alteração de estado persistente.
  3. **Introdução Orgânica de Personagens:** Nenhum personagem canon é introduzido em bloco artificial; cada um deve ter primeiro contacto registado com contexto e data independentes.
  4. **Backpropagation de Pistas e Adereços:** Objetos cruciais ou mistérios com desfecho futuro devem ter proveniência explícita rastreável em cenas anteriores.
- **Consequências:**
  - Qualquer novo episódio ou alteração estrutural deve passar na suite de testes antes de ser consolidado.
  - O pipeline de escrita torna-se auditável de forma determinística por humanos e agentes de IA.
