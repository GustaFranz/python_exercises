# DEMANDA
# Empresa: BancoSim Educacao
# Setor: Financeiro / simulacoes
# Solicitacao: Demonstrar fluxo completo de tratamento de erros em operacao sensivel.

# EXERCICIO 51 - Introducao a try except finally (contexto corporativo)
#
# VISAO DO BLOCO — try except else finally (exercicios 51 a 55)
# Este bloco treina:
## 51 — Introducao: fluxo try/except/else/finally
## 52 — Divisao segura sem quebrar programa
## 53 — Ler arquivo que pode nao existir
## 54 — Transacao simulada com log no finally
## 55 — Menu robusto que sempre registra saida
#
# Conceitos basicos:
## try: codigo que pode falhar
## except TipoErro: trata o erro
## else: executa se try nao levantou excecao
## finally: sempre executa (limpeza, log, fechar recurso)
#
# Implemente operacao_segura(a, b) que divide a por b.
# Estrutura obrigatoria:
## try: resultado = a / b
## except ZeroDivisionError: mensagem de erro
## else: exiba "Resultado: {resultado}"
## finally: exiba "Operacao finalizada."
# Teste com (10, 2) e (10, 0).
#
# ORIENTACOES
## else so roda quando nao houve excecao.
## finally roda em ambos os casos — use para mensagem de encerramento.

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
