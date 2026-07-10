# DEMANDA
# Empresa: Edutech Brasil
# Setor: Educacao / desenvolvimento
# Solicitacao: Documentar tipos do modulo de cadastro para facilitar manutencao.

# EXERCICIO 121 - Introducao a type hints (contexto corporativo)
#
# VISAO DO BLOCO — Type hints basicos (exercicios 121 a 125)
# Este bloco treina:
## 121 — Introducao: anotar cadastro simples
## 122 — list[str], dict[str, float]
## 123 — Retorno opcional (float | None)
## 124 — Modulo com hints em todas funcoes publicas
## 125 — API tipada + docstrings + asserts
#
# Conceitos basicos:
## def funcao(nome: str, idade: int) -> str:
## Hints nao forcao tipo em runtime — documentam intencao
## Facilita leitura, IDE e ferramentas como mypy
## Python 3.10+: float | None; antes: Optional[float]
#
# Implemente com type hints:
## def criar_aluno(nome: str, matricula: int, turma: str) -> dict[str, str | int]:
## def exibir_aluno(aluno: dict[str, str | int]) -> str:
# Teste criando um aluno e exibindo string formatada.
#
# ORIENTACOES
## Anote todos os parametros e o retorno de cada funcao.
## dict[str, str | int] para aluno com campos mistos.

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
