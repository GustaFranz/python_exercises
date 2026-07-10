# EXERCICIO 01 - Pathlib: navegar pastas do projeto
#
# DEMANDA
# A TI precisa localizar automaticamente arquivos CSV de notas na pasta dados/.
#
# TAREFAS
# 1. Crie pasta_projeto com Path(__file__).resolve().parent
# 2. Crie pasta_dados = pasta_projeto / "dados"
# 3. Use pasta_dados.glob("*.csv") para listar arquivos
# 4. Imprima o caminho de cada arquivo
#
# CONCEITOS: Path, __file__, resolve(), parent, /, glob()
#
# --- Implemente sua solucao abaixo ---

from pathlib import Path

#----> Aqui, usaremos o Path(__file__) para encontrar o caminho da pasta .py a qual estamos. A partir dela é que 
#----> vamos voltar paras pastas "superiores" (pastas-mãe), para trabalhar ou encontrar os caminhos dos arquivos
pasta_main = Path(__file__).resolve()
#----> .resolve (encontrar caminho absoluto), .parent (retornar à pasta mãe)
pasta_projeto = Path(__file__).resolve().parent
#----> Retorna-se à pasta mãe (no caso a pasta "pathlib_navegar_pastas") para, então, encontra o arquivo "dados" 
pasta_dados = pasta_projeto / "dados"

# ------------------------------------
# ----------|      OBSERVAÇÃO>    A Pathlib é um builder, ou seja, No Python, os caminhos deixam de ser 
# ----------|      apenas "textos estáticos" e se transformam em variáveis vivas que guardam um objeto do tipo Path.
# ------------------------------------
print(pasta_main)
print(pasta_projeto)
print(pasta_dados)

# 3 e 4. Usa o glob para encontrar os arquivos CSV e imprime o caminho de cada um
for arquivo in pasta_dados.glob("*.csv"):
    print(arquivo)



