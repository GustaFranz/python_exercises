# DEMANDA
# Empresa: LimpezaDados Servicos
# Setor: Tratamento de dados
# Solicitacao: Normalizar JSON de funcionarios importado, ignorando registros incompletos com relatorio.

# EXERCICIO 116 - Dataclass: converter dicts com validacao (nivel entrevista junior)
#
# @dataclass Funcionario:
## nome: str
## cargo: str
## salario: float
## resumo(self) -> str
#
# Dados brutos (simulando exportacao JSON):
## [
##   {"nome": "Ana", "cargo": "Analista", "salario": 3500},
##   {"nome": "Bruno", "cargo": "Suporte", "salario": 2800},
##   {"cargo": "Dev", "salario": 4200},
##   {"nome": "Carla", "salario": 3100},
##   {"nome": "Diego", "cargo": "Estagiario", "salario": -500},
##   {"nome": "Elena", "cargo": "Coordenadora", "salario": "5200"},
## ]
#
# Funcoes:
## validar_linha(item: dict) -> bool
## converter(dados: list[dict]) -> tuple[list[Funcionario], list[dict]]
## relatorio_conversao(convertidos, rejeitados) -> None
#
# ORIENTACOES
## Campos obrigatorios: nome, cargo, salario.
## salario deve ser int ou float >= 0.
## Rejeitados: guarde dict original para auditoria.
## Funcionario(**item) so apos validacao.

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
