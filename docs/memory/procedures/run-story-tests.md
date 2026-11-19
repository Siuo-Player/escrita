# Procedimento: Execução da Suite de Testes de História

Para assegurar a integridade do cânone, das datas, do paralelismo de tramas e do backpropagation de pistas:

## Execução

Executar a partir da raiz do repositório:

```powershell
python tests/run_story_tests.py
```

Ou através do módulo nativo `unittest`:

```powershell
python -m unittest discover -s tests -p "test_*.py"
```

## O que os testes verificam:

1. **`test_chronology.py`**:
   - Monotonicidade temporal de todos os acontecimentos (sem saltos temporais regressivos sem tag explícita).
   - Validação dos dias da semana em 2009/2010.
   - Presença das datas-âncora obrigatórias.

2. **`test_parallel_plots.py`**:
   - Mínimo de 3 linhas de trama por episódio (1 principal + $\ge 2$ secundárias).
   - Ausência de episódios fillers (cada episódio deve declarar mutação de estado persistente).

3. **`test_character_introductions.py`**:
   - Aparições iniciais graduais de cada elemento da família Dunphy/Pritchett e secundários.
   - Verificação de que não surgem todos no mesmo instante sem justificação.

4. **`test_backpropagation_clues.py`**:
   - Garantia de que adereços e pistas futuras têm registo prévio obrigatório de génese e presença.
