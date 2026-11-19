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
        print("  - Linearidade temporal validada.")
        print("  - Política anti-filler (>= 3 tramas) confirmada.")
        print("  - Introdução orgânica e continuidade preservadas.")
        print("  - Registo de adereços e pistas auditado.")
        print("=" * 70)
        return 0
    else:
        print(f"  RESULTADO: FALHA! {len(result.failures)} falhas, {len(result.errors)} erros.")
        print("=" * 70)
        return 1

if __name__ == '__main__':
    sys.exit(main())
