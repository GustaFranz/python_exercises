# EXERCICIO 56B - Materiais escolares em tupla (contexto educacional)
#
# ENUNCIADO
# Crie um programa que:
## Tenha uma tupla com pelo menos 5 materiais escolares.
## Exiba o titulo: MATERIAIS DISPONIVEIS
## Mostre os itens numerados (igual ao exercicio 56A).
## Ao final, mostre a quantidade total de materiais.
#
# ORIENTACOES
## Colete os nomes em uma lista temporaria e converta para tupla com tuple().
## Use enumerate para numerar a exibicao.
## Encerre a entrada quando o usuario digitar "sair" ou "s".
#
# --- Implemente sua solucao abaixo ---
#
# =============================================================================
# # RESOLUCAO DO EXERCICIO
# =============================================================================

import easyansi
easyansi.activate()

materiais_temp = []
while True:
    material = input("Digite o nome de um material ou 'sair' (S) para encerrar: ").strip().capitalize()
    if material.lower() in ("sair", "s"):
        break
    materiais_temp.append(material)

materiais = tuple(materiais_temp)

print("\n" + "-" * 10 + "LISTA DE MATERIAIS" + "-" * 10)
print(f"//bold-green/{materiais}/bold-green")
print("\n" + "-" * 10 + "MATERIAIS DISPONIVEIS" + "-" * 10)
for i, item in enumerate(materiais):
    print(f"{i + 1} | //bold-green/{item}/bold-green")

print("-" * 30)
print(f"Total de materiais: //bold-green/{len(materiais)}/bold-green")
print("-" * 30)

# =============================================================================
# # APRENDIZADOS E CONSOLIDACAO DE CONCEITOS
# =============================================================================
#
# Complemento pratico do exercicio 56A com entrada dinamica de dados
# Conversao de lista para tupla apos coleta de itens
# Uso de enumerate para exibir materiais numerados
# Diferenca entre coleta mutavel (lista) e armazenamento final imutavel (tupla)
# Utilizacao da biblioteca EasyAnsi para melhoria visual do sistema
#
# Link do repositorio da biblioteca EasyAnsi: https://github.com/GustaFranz/easyansi
#
# OBRIGADO!
# FIQUE A VONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO
