# DEMANDA
# Empresa: Secretaria Digital
# Setor: Educacao / secretaria
# Solicitacao: Ferramenta unica para listar ou exportar alunos por turma.

# EXERCICIO 78 - Argparse: subcomando simples (contexto corporativo)
#
# Subcomandos:
## listar --turma TURMA: exibe "Listando alunos da turma {turma}"
## exportar --turma TURMA --arquivo CAMINHO: exibe "Exportando turma {turma} para {arquivo}"
# Use subparsers = parser.add_subparsers(dest="comando")
#
# ORIENTACOES
## parser_listar = subparsers.add_parser("listar")
## parser_listar.add_argument("--turma", required=True)
## Teste: python main.py listar --turma 7B
## Teste: python main.py exportar --turma 8A --arquivo saida.csv

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
