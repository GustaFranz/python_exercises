# EXERCICIO 03 - Pathlib: montar caminhos do pipeline
#
# DEMANDA
# Definir todas as pastas usadas no projeto de boletim a partir da raiz.
#
# TAREFAS
# 1. pasta_projeto = Path(__file__).resolve().parent
# 2. Monte caminhos para: simulados, provas, projetos, relatorios, boletins, prints
# 3. pasta_downloads = Path.home() / "Downloads"
# 4. Imprima cada caminho com rotulo
# 5. (Extra) portal_login = pasta_projeto / "portal_simulado" / "login.html"
#    Imprima portal_login.as_uri()
#
# CONCEITOS: operador /, Path.home(), .as_uri()
#
# --- Implemente sua solucao abaixo ---

from pathlib import Path

pasta_projeto = Path(__file__).resolve().parent
pasta_dados = pasta_projeto / "dados" 
pasta_simulados = pasta_dados / "simulados"
pasta_provas = pasta_dados / "provas"
pasta_saidas = pasta_dados / "saidas"
pasta_relatorios = pasta_saidas / "relatorios"
pasta_boletins = pasta_saidas / "boletins"
pasta_prints = pasta_saidas / "prints"
pasta_portal_login = pasta_projeto / "portal_simulado" / "login.html"
pasta_downloads = Path.home() / "Downloads"


print(f'Pasta do projeto: {pasta_projeto}')
print(f'Pasta dos dados: {pasta_dados}')
print(f'Pasta dos simulados: {pasta_simulados}')
print(f'Pasta das provas: {pasta_provas}')
print(f'Pasta das saidas: {pasta_saidas}')
print(f'Pasta dos relatorios: {pasta_relatorios}')
print(f'Pasta dos boletins: {pasta_boletins}')
print(f'Pasta dos prints: {pasta_prints}')
print(f'Pasta do portal de login: {pasta_portal_login.as_uri()}')
print(f'Pasta dos downloads: {pasta_downloads}')
