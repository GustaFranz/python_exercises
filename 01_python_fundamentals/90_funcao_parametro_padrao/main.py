# EXERCICIO 90 - Funcao com parametro padrao (contexto de comercio)
#
# ENUNCIADO
# Crie uma funcao chamada preco_final que recebe:
## preco (obrigatorio)
## desconto (opcional, valor padrao 10)
# A funcao deve retornar o preco com o desconto aplicado (em porcentagem).
# Chame a funcao uma vez usando o desconto padrao e outra vez informando 25.
#
# ORIENTACOES
## Defina o valor padrao no proprio parametro: def preco_final(preco, desconto=10).
## Calcule: preco - (preco * desconto / 100).
## Chame a funcao das duas formas para ver a diferenca.
#
# --- Implemente sua solucao abaixo ---
#
# =============================================================================
# # RESOLUCAO DO EXERCICIO
# =============================================================================
def preco_final(preco, desconto=10):
    final = preco - ((desconto/100)*preco)
    print(f'Com o desconto de {desconto}%, o valor final é {final}')
    
preco_final(200) #como ja foi definido desconto padrão de 10%, então não precisa colocar

preco_final(200, 5)  #Quando colocar valor no lugar do valor padrão, substitue
# =============================================================================
# # APRENDIZADOS E CONSOLIDACAO DE CONCEITOS
# =============================================================================

#
#
# OBRIGADO!
# FIQUE A VONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO
