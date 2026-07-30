# DEMANDA
# Empresa: AgroEscola
# Setor: Educacao / campo
# Solicitacao: Reorganizar controle de estoque do viveiro escolar antes da safra de plantio.

# EXERCICIO 121 - Refatoracao: script longo em funcoes (nivel entrevista junior)
#
# O arquivo legado.py contem script monolitico (~70 linhas) — ESTUDE, nao copie cegamente.
# Refatore em main.py com separacao clara:
## carregar_estoque() -> list[dict]
## validar_movimentacao(estoque, nome, qtd, tipo) -> tuple[bool, str]
## calcular_estoque_atual(estoque, movimentos) -> list[dict]
## exibir_relatorio(estoque, alertas) -> None
## main() -> menu: 1 consultar | 2 movimentar | 3 relatorio | 0 sair
#
# Regras de negocio (preservar do legado):
## Saida bloqueada se qtd > estoque disponivel
## Entrada sempre positiva
## Item inexistente: mensagem de erro, sem alterar estoque
## Estoque < 10 unidades: incluir em lista de alertas do relatorio
#
# ORIENTACOES
## Pode simular movimentos em lista fixa para teste automatico (sem input()).
## Objetivo de entrevista: legibilidade, funcoes pequenas, mesmo comportamento.
## Compare saida do main.py refatorado com legado.py nos mesmos dados.

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
