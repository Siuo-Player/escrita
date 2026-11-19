"""
Runner principal para a suite de testes narrativos do projeto escrita.
Executa os testes de cronologia, múltiplos enredos, introdução de personagens e backpropagation.
"""

import sys
import unittest
from pathlib import Path

# Adiciona o repositório ao sys.path
REPO_ROOT = Path(__file__).resolve().parent.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

def main():
    print("=" * 70)
    print("  SUITE DE TESTES AUTOMÁTICOS DE INTEGRIDADE NARRATIVA — escrita")
    print("=" * 70)
    print(f"Diretoria base: {REPO_ROOT}\n")
    
    loader = unittest.TestLoader()
    suite = loader.discover(start_dir=str(REPO_ROOT / "tests"), pattern="test_*.py")
    
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    print("\n" + "=" * 70)
    if result.wasSuccessful():
        print(f"  RESULTADO: SUCESSO! Todos os {result.testsRun} testes passaram.")
        print("  - Datas, dias da semana e ordem cronológica passaram as verificações determinísticas.")
        print("  - EVENT_REGISTRY: IDs, intervalos, story windows e referências documentais alinhados.")
        print("  - Estreias de personagens derivadas do registo; verificações de contacto prematuro por padrões.")
        print("  - Tramas e consequências: apenas estrutura declarada/indicadores textuais são verificados.")
        print("  - Prosa: verificações mecânicas; qualidade literária, naturalidade e causalidade semântica exigem revisão humana.")
        print("  - Props/pistas: verificações estruturais e temporais, não compreensão narrativa automática.")
        print("=" * 70)
        return 0
    else:
        print(f"  RESULTADO: FALHA! {len(result.failures)} falhas, {len(result.errors)} erros.")
        print("=" * 70)
        return 1

if __name__ == '__main__':
    sys.exit(main())
