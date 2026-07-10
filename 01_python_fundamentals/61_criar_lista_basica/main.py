# EXERCICIO 61 - Criar lista basica (contexto introdutorio)
#
# ENUNCIADO
# Crie uma lista com o nome de tres frutas a sua escolha.
# Em seguida, exiba a lista completa.
#
# ORIENTACOES
## Crie a lista usando colchetes [].
## Separe os itens por virgula.
## Exiba a lista com print().
#
# --- Implemente sua solucao abaixo ---
#
# =============================================================================
# # RESOLUCAO DO EXERCICIO
# =============================================================================
import easyansi
easyansi.activate()

list_frutas = []

while True:
    fruta = input('Digite de uma fruta ou "S" para sair: ')
    fruta = fruta.strip().capitalize()
    if fruta not in ["S", "Sair"]:
        list_frutas.append(fruta)
    else:
        break

print("//yellow/---------------- LISTA DE FRUTAS ----------------/yellow")
print(f'//green/{list_frutas}/green')

# =============================================================================
# # APRENDIZADOS E CONSOLIDACAO DE CONCEITOS
# =============================================================================
#
# Criacao de lista dinamica com coleta de itens via input
# Uso de append para inserir elementos durante o loop
# Controle de encerramento com parada manual do usuario
# Utilizacao da biblioteca EasyAnsi para melhoria visual do sistema
#
# Link do repositorio da biblioteca EasyAnsi: https://github.com/GustaFranz/easyansi
#
# OBRIGADO!
# FIQUE A VONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO
