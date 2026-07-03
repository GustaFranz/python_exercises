# EXERCICIO 62 - Acessar elementos da lista (contexto introdutorio)
#
# ENUNCIADO
# Dada a lista abaixo:
# animais = ["gato", "cachorro", "coelho", "peixe"]
# Exiba o primeiro e o ultimo elemento da lista.
#
# ORIENTACOES
## Use o indice 0 para acessar o primeiro elemento.
## Use o indice -1 para acessar o ultimo elemento.
#
# --- Implemente sua solucao abaixo ---
#
# =============================================================================
# # RESOLUCAO DO EXERCICIO
# =============================================================================
import easyansi
easyansi.activate()

animais = ["gato", "cachorro", "coelho", "peixe"]
print(f'//green/Primeiro elemento da lista:/green //yellow/{animais[0].capitalize()}/yellow')
print(f'//green/Último elemento da lista:/green //yellow/{animais[-1].capitalize()}/yellow')

# =============================================================================
# # APRENDIZADOS E CONSOLIDACAO DE CONCEITOS
# =============================================================================
#
# Acesso ao primeiro elemento da lista pelo indice 0
# Acesso ao ultimo elemento pelo indice -1
# Formatacao de saida com f-string e destaque no terminal
# Utilizacao da biblioteca EasyAnsi para melhoria visual do sistema
#
# Link do repositorio da biblioteca EasyAnsi: https://github.com/GustaFranz/easyansi
#
# OBRIGADO!
# FIQUE A VONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO
