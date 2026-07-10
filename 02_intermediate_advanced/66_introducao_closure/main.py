# DEMANDA
# Empresa: Loja Virtual Escolar
# Setor: Varejo / precificacao
# Solicitacao: Aplicar taxa fixa de embalagem em todos os pedidos escolares.

# EXERCICIO 66 - Introducao a closure (contexto corporativo)
#
# VISAO DO BLOCO — Closure (exercicios 66 a 70)
# Este bloco treina:
## 66 — Introducao: funcao que retorna somador com taxa
## 67 — Multiplicador com fator capturado
## 68 — Filtro com limite minimo capturado
## 69 — Gerador de relatorios por turma
## 70 — Fabrica criar_validador(min, max)
#
# Conceitos basicos:
## Funcao interna pode usar variaveis da funcao externa
## A funcao externa retorna a interna — isso e closure
## O valor capturado permanece entre chamadas da funcao retornada
## Padrao util para configurar comportamento sem classes
#
# Implemente criar_somador_com_taxa(taxa):
## Retorna funcao interna adicionar(valor) que retorna valor + taxa
# Exemplo:
## somar = criar_somador_com_taxa(5)
## somar(10) -> 15
## somar(20) -> 25
# Teste com taxa 5 e valores 10, 20, 0.
#
# ORIENTACOES
## def criar_somador_com_taxa(taxa):
##     def adicionar(valor):
##         return valor + taxa
##     return adicionar

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
