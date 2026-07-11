# EXERCICIO 102 - Ordenar disciplinas com lambda (contexto educacional)
#
# ENUNCIADO
# Dada a lista de disciplinas:
# disciplinas = ["Matematica", "Portugues", "Ciencias", "Historia", "Geografia"]
# Ordene do nome mais curto para o mais longo e exiba o resultado.
#
# ORIENTACOES
## Use sorted(disciplinas, key=lambda d: len(d)).
## A lambda retorna o tamanho de cada nome.
## Exiba a lista ordenada com print().
#
# --- Implemente sua solucao abaixo ---
#
# =============================================================================
# # RESOLUCAO DO EXERCICIO
# =============================================================================
import easyansi
easyansi.activate()

disciplinas = ["Matematica", "Portugues", "Ciencias", "Historia", "Geografia"]

disciplinas_ordenadas = sorted(disciplinas, key=lambda d: len(d))

print(f'//green/Disciplinas ordenadas do mais curto ao mais longo/green //yellow/{disciplinas_ordenadas}/yellow')

# =============================================================================
# # APRENDIZADOS E CONSOLIDACAO DE CONCEITOS
# =============================================================================
#
# sorted() com key=lambda d: len(d) ordena por tamanho
# Lambda devolve criterio sem precisar de def
# Lista original intacta apos sorted
# Animado em ordenar disciplinas por numero de letras
# Utilizacao da biblioteca EasyAnsi para melhoria visual do sistema
#
# Link do repositorio da biblioteca EasyAnsi: https://github.com/GustaFranz/easyansi
#
# OBRIGADO!
# FIQUE A VONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO
