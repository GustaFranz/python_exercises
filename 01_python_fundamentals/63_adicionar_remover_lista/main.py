# EXERCICIO 63 - Adicionar e remover itens da lista (contexto introdutorio)
#
# ENUNCIADO
# Dada a lista abaixo:
# compras = ["arroz", "feijao", "leite"]
# Adicione "cafe" no fim da lista e remova "leite".
# Depois exiba a lista final.
#
# ORIENTACOES
## Use append() para adicionar um item no fim.
## Use remove() para retirar um item pelo valor.
## Exiba a lista com print().
#
# --- Implemente sua solucao abaixo ---
#
# =============================================================================
# # RESOLUCAO DO EXERCICIO
# =============================================================================
import easyansi
easyansi.activate()

compras = ["arroz", "feijao", "leite"]
compras.append("cafe")
compras.remove("leite")
print(f'//green/Lista final de compras:/green //yellow/{compras}/yellow')

# =============================================================================
# # APRENDIZADOS E CONSOLIDACAO DE CONCEITOS
# =============================================================================
#
# Metodo append para adicionar item no fim da lista
# Metodo remove para retirar item pelo valor
# Exibicao da lista final apos as alteracoes
# Utilizacao da biblioteca EasyAnsi para melhoria visual do sistema
#
# Link do repositorio da biblioteca EasyAnsi: https://github.com/GustaFranz/easyansi
#
# OBRIGADO!
# FIQUE A VONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO
