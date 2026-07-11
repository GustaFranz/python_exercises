# EXERCICIO 98 - Lambda com condicao (contexto introdutorio)
#
# ENUNCIADO
# Crie uma funcao lambda chamada par_impar que recebe um numero
# e retorna o texto "par" se ele for par, ou "impar" caso contrario.
# Teste a lambda com os numeros 4, 7 e 10.
#
# ORIENTACOES
## Use a expressao condicional em uma linha: valor_se_verdadeiro if condicao else valor_se_falso.
## Um numero e par quando numero % 2 == 0.
## Exemplo: par_impar = lambda n: "par" if n % 2 == 0 else "impar"
#
# --- Implemente sua solucao abaixo ---
#
# =============================================================================
# # RESOLUCAO DO EXERCICIO
# =============================================================================
import easyansi
easyansi.activate()

par_impar = lambda x: "par" if x % 2 == 0 else "impar"
print(f'//green/O número 4 é/green //yellow/{par_impar(4)}/yellow')
print(f'//green/O número 7 é/green //yellow/{par_impar(7)}/yellow')
print(f'//green/O número 10 é/green //yellow/{par_impar(10)}/yellow')



# =============================================================================
# # APRENDIZADOS E CONSOLIDACAO DE CONCEITOS
# =============================================================================
#
# Primeira lambda com condicao: if/else em uma linha
# Par ou impar com operador % 2 == 0
# Expressao ternaria dentro da lambda evita bloco def
# Animado em classificar numeros com poucas palavras
# Utilizacao da biblioteca EasyAnsi para melhoria visual do sistema
#
# Link do repositorio da biblioteca EasyAnsi: https://github.com/GustaFranz/easyansi
#
# OBRIGADO!
# FIQUE A VONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO
