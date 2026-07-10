# EXERCICIO 02 - Pathlib: raiz do projeto (parent.parent)
#
# DEMANDA
# O script esta em src/ e precisa achar a raiz do exercicio para acessar dados/.
#
# TAREFAS
# 1. pasta_projeto = Path(__file__).resolve().parent.parent
# 2. pasta_dados = pasta_projeto / "dados"
# 3. pasta_simulados = pasta_dados / "simulados"
# 4. Imprima pasta_projeto, pasta_dados e pasta_simulados
# 5. Imprima pasta_simulados.exists()
#
# CONCEITOS: __file__, resolve(), parent.parent, operador /
#
# --- Implemente sua solucao abaixo ---

from pathlib import Path

pasta_projeto = Path(__file__).resolve().parent.parent
pasta_dados = pasta_projeto / "dados"
pasta_simulados = pasta_dados / "simulados"

print(pasta_projeto)
print(pasta_dados)
print(pasta_simulados)
print(pasta_simulados.exists())

