# EXERCICIO 57 - Desempacotar tupla (contexto introdutorio)
#
# ENUNCIADO
# Dada a tupla abaixo:
# pessoa = ("Ana", 30, "Recife")
# Desempacote a tupla em tres variaveis (nome, idade, cidade) e exiba cada uma.
#
# ORIENTACOES
## Atribua a tupla a tres variaveis de uma so vez.
## Exiba cada variavel separadamente com print().
#
# --- Implemente sua solucao abaixo ---
#
# =============================================================================
# # RESOLUCAO DO EXERCICIO
# =============================================================================
import easyansi
easyansi.activate()

# pessoa = ("Ana", 30, "Recife")
# nome, idade, cidade = pessoa

# print(f"Nome: {nome}")
# print(f"Idade: {idade}")
# print(f"Cidade: {cidade}")

# Teste - Supondo uma lista maior:
# Lista de tuplas contendo (nome, idade, cidade)

usuarios = [
    ("Carlos", 28, "São Luís"),
    ("Beatriz", 34, "Fortaleza"),
    ("Renato", 22, "Recife"),
    ("Mariana", 31, "Salvador")
]

print("//yellow/" + "-" * 35 + " LISTA DE USUÁRIOS: " + "-" * 35 + "//yellow/")
for i, (nome, idade, cidade) in enumerate(usuarios):
    print(f"{i + 1} | Nome: {nome:.<30}  | Idade: {idade:<3}  | Cidade: {cidade}")


# Desempacote a tupla em tres variaveis (nome, idade, cidade) e exiba cada uma.
#
# ORIENTACOES
## Atribua a tupla a tres variaveis de uma so vez.
## Exiba cada variavel separadamente com print().

# =============================================================================
# # APRENDIZADOS E CONSOLIDACAO DE CONCEITOS
# =============================================================================
#
# Desempacotamento de tuplas dentro de laços for
# Lista de tuplas como estrutura para registros com multiplos campos
# Uso de enumerate para numerar a exibicao de cada registro
# Utilizacao da biblioteca EasyAnsi para melhoria visual do sistema
#
# Link do repositorio da biblioteca EasyAnsi: https://github.com/GustaFranz/easyansi
#
# OBRIGADO!
# FIQUE A VONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO
