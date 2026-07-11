# EXERCICIO 96 - Lambda simples (contexto introdutorio)
#
# ENUNCIADO
# Crie uma funcao lambda chamada dobro que recebe um numero e retorna o valor multiplicado por 2.
# Use a lambda para exibir o dobro de 5, 10 e 25.
#
# ORIENTACOES
## A sintaxe e: dobro = lambda x: x * 2
## Chame a lambda como uma funcao normal: dobro(5).
## Uma lambda ja retorna o resultado, sem precisar de return.
#
# --- Implemente sua solucao abaixo ---
#
# =============================================================================
# # RESOLUCAO DO EXERCICIO
# =============================================================================
import easyansi
easyansi.activate()

dobro = lambda x: x * 2

print(f'//green/ O dobro de 2 é/green //yellow/{dobro(2)}/yellow,\n '
      f'//green/O dobro de 5 é/green //yellow/{dobro(5)}/yellow,\n '
      f'//green/O dobro de 10 é/green //yellow/{dobro(10)}/yellow,\n '
      f'//green/O dobro de 25 é/green //yellow/{dobro(25)}/yellow')

# =============================================================================
# # APRENDIZADOS E CONSOLIDACAO DE CONCEITOS
# =============================================================================
#
# Primeiro contato com lambda: funcao anonima em uma linha
# Sintaxe lambda x: x * 2 substitui def para calculo simples
# Chamar dobro(5) igual a uma funcao normal
# Animado em ver retorno automatico sem usar return
# Utilizacao da biblioteca EasyAnsi para melhoria visual do sistema
#
# Link do repositorio da biblioteca EasyAnsi: https://github.com/GustaFranz/easyansi
#
# OBRIGADO!
# FIQUE A VONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO
