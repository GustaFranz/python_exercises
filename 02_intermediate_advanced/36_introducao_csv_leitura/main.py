# DEMANDA
# Empresa: NotasOnline Escolas
# Setor: Educacao / secretaria
# Solicitacao: Importar planilha CSV de notas exportada do sistema legado.

# EXERCICIO 36 - Introducao a leitura CSV (contexto corporativo)
#
# VISAO DO BLOCO — CSV leitura e escrita (exercicios 36 a 40)
# Este bloco treina:
## 36 — Introducao: ler CSV de notas
## 37 — Escrever relatorio CSV
## 38 — Delimitador ponto-e-virgula (padrao BR)
## 39 — Importar vendas e calcular totais
## 40 — Pipeline ler, limpar e exportar
#
# Conceitos basicos:
## import csv
## csv.reader para linhas como listas
## csv.DictReader quando ha cabecalho
## csv.writer / DictWriter para exportar
#
# Crie ou assuma notas.csv com cabecalho:
# aluno,nota,turma
# Ana,8.0,9A
# Bruno,6.5,9A
# Carla,9.0,9B
# Leia com csv.DictReader e exiba cada registro formatado.
# Calcule media geral das notas.
#
# ORIENTACOES
## with open("notas.csv", encoding="utf-8") as f:
##     leitor = csv.DictReader(f)
## Notas: float(linha["nota"]).
## Crie notas.csv no codigo se nao existir (write antes de read) ou documente no README.

# --- Implemente sua solucao abaixo ---
#
# =============================================================================
# # RESOLUCAO DO EXERCICIO
# =============================================================================


# =============================================================================
# # APRENDIZADOS E CONSOLIDACAO DE CONCEITOS
# =============================================================================

#
#
# OBRIGADO!
# FIQUE A VONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO
