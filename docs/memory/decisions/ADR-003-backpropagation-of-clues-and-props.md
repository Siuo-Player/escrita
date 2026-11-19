# ADR-003: Protocolo de Backpropagation de Pistas e Adereços (*Causa e Efeito Invertida*)

- **Data:** 2026-11-19
- **Status:** ACEITE
- **Contexto:**
  Quando a meio do desenvolvimento (ex: Episódio 8 ou Episódio 4) surge a necessidade de um objeto perdido, um conflito latente, uma revelação ou uma dinâmica entre personagens, não é permitido simplesmente "fazer aparecer" o objeto ou detalhe do nada no momento exato em que a cena precisa dele.
- **Decisão:**
  1. **Auditoria Regressiva:** Ao definir um elemento no capítulo $N$, recuar aos capítulos $N-1, N-2, \dots$ para inserir a génese do elemento.
  2. **Camadas de Presença:**
     - *Nível 1 (Aquisição/Origem):* Mostrar a compra, oferta, desembalamento ou posse inicial como detalhe casual ou rotineiro.
     - *Nível 2 (Fundo de Cena/Utilização Natural):* Mostrar personagens a interagir ou passar pelo elemento sem foco ostensivo da câmara (ex: objeto na bancada, comentário de passagem).
     - *Nível 3 (Evento Causal):* Mostrar o momento em que o objeto é esquecido, perdido, danificado ou o segredo é quase descoberto.
     - *Nível 4 (Ponto Focal/Resolução no Cap $N$):* A busca ou consequência ocorre com plena naturalidade e satisfação retroativa para o leitor.
  3. **Registo Centralizado:** Manter e auditar a tabela de pistas e proveniência de adereços no canon e na suite de testes automáticos.
- **Consequências:**
  - Elimina *deus ex machina* e conveniências artificiais de argumento.
  - Estimula re-leituras recompensadoras.
