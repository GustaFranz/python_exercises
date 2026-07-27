# EXERCICIO 143 - Confirmador de venda na cantina com match/case (contexto comercial)
#
# PASSO A PASSO
## Passo 1: Crie VendaInvalidaError para tipos de item nao permitidos.
## Passo 2: Crie confirmar_item(codigo) com match/case dentro da funcao.
##         Aceite: S (salgado), B (bebida), D (doce), L (lanche).
##         Padronize a entrada com strip().upper().
## Passo 3: No case _, lance VendaInvalidaError com mensagem clara.
## Passo 4: Fora da funcao, use while True com try/except para nova entrada.
## Passo 5: Exiba a confirmacao da venda quando o codigo for valido.
#
# ENUNCIADO
# Crie um confirmador de vendas para a cantina escolar.
# O sistema deve:
## solicitar o codigo do item (S, B, D ou L);
## exibir a confirmacao do tipo de produto vendido;
## impedir codigos invalidos sem quebrar o programa.
#
# ORIENTACOES
## match/case na funcao; try/except no fluxo principal (SRP).
#
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
