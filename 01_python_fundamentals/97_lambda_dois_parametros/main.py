# EXERCICIO 97 - Lambda com dois parametros (contexto introdutorio)
#
# ENUNCIADO
# Crie duas funcoes lambda:
## soma: recebe dois numeros e retorna a soma;
## area: recebe base e altura e retorna a area do retangulo (base * altura).
# Use as duas lambdas com valores a sua escolha e exiba os resultados.
#
# ORIENTACOES
## Separe os parametros por virgula: soma = lambda a, b: a + b
## Chame cada lambda passando os dois argumentos.
#
# --- Implemente sua solucao abaixo ---
#
# =============================================================================
# # RESOLUCAO DO EXERCICIO
# =============================================================================

soma = lambda x, y: x + y
area_retangulo = lambda b, h: b * h

#CALCULAR SOMA 60 + 7 
print(f'A soma de 60 e 7 é {soma(60,7)}')

#CALCULAR SOMA -12 + 7
print(f'A soma de -12 e 7 é {soma(-12, 7)}')

# CALCULAR ÁREA DO RETANCULOS DE BASE = 10  E ALTURA = 6
print(f'A área do retangulo é {area_retangulo(10, 6)} cm')

# CALCULAR ÁREA DO RETANCULOS DE BASE = 23  E ALTURA = 16
print(f'A área do retangulo é {area_retangulo(23, 16)} cm')

# =============================================================================
# # APRENDIZADOS E CONSOLIDACAO DE CONCEITOS
# =============================================================================
#
# Lambda com dois parametros: lambda x, y: x + y
# area_retangulo reutiliza o mesmo padrao com b e h
# Animado em trocar def por lambda em calculos curtos
# Mesma chamada de funcao: soma(60, 7) e area_retangulo(10, 6)
#
# OBRIGADO!
# FIQUE A VONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO
