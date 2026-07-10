# DEMANDA
# Empresa: FinEdu Carteira
# Setor: Financeiro educacional
# Solicitacao: Bloquear saque quando saldo da carteira digital for insuficiente.

# EXERCICIO 46 - Introducao a excecao customizada (contexto corporativo)
#
# VISAO DO BLOCO — raise e excecao customizada (exercicios 46 a 50)
# Este bloco treina:
## 46 — Introducao: classe de excecao + raise
## 47 — Validar idade com excecao customizada
## 48 — Nota fora do intervalo permitido
## 49 — Cadastro com multiplas excecoes especificas
## 50 — Fluxo de pedido que propaga erros com mensagens claras
#
# Conceitos basicos:
## class MinhaErro(Exception): pass
## raise MinhaErro("mensagem") interrompe o fluxo
## Excecoes customizadas deixam regras de negocio explicitas
## Capturar com except MinhaErro as e: para tratar
#
# Crie a excecao SaldoInsuficienteError(Exception).
# Implemente sacar(saldo, valor) que:
## retorna saldo - valor se valor <= saldo
## levanta SaldoInsuficienteError com mensagem clara se valor > saldo
# Teste com saldo=100, saque 30 (ok) e saque 80 (erro).
# Trate o erro com try/except e exiba mensagem amigavel ao usuario.
#
# ORIENTACOES
## class SaldoInsuficienteError(Exception): ...
## raise SaldoInsuficienteError(f"Saldo {saldo} insuficiente para sacar {valor}")
## No except, use str(e) ou e.args[0] na mensagem.

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
