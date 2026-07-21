# EXERCICIO 124 - Agrupamento de usuarios por idade (contexto digital)
#
# ENUNCIADO
# Considere a lista de usuarios abaixo:
# usuarios = [{"nome": "Ana", "idade": 17}, {"nome": "Bruno", "idade": 22}, {"nome": "Carlos", "idade": 15}, {"nome": "Daniela", "idade": 30}, {"nome": "Eduardo", "idade": 19}]
# O programa deve:
## separar usuarios em menores de idade e adultos;
## criar duas listas diferentes;
## contar quantos usuarios existem em cada grupo.
#
# ORIENTACOES
## Use listas separadas.
## Percorra com for.
## Use condicoes com idade >= 18.
#
# --- Implemente sua solucao abaixo ---
#
# =============================================================================
# # RESOLUCAO DO EXERCICIO
# =============================================================================
import easyansi

easyansi.activate()

usuarios = [
    {"nome": "Ana", "idade": 17},
    {"nome": "Bruno", "idade": 22},
    {"nome": "Carlos", "idade": 15},
    {"nome": "Daniela", "idade": 30},
    {"nome": "Eduardo", "idade": 19},
]


def agrupar_por_idade(usuarios):
    """Separa usuarios menores de idade e adultos."""
    menores = []
    adultos = []

    for usuario in usuarios:
        if usuario["idade"] >= 18:
            adultos.append(usuario)
        else:
            menores.append(usuario)

    return menores, adultos


def exibir_grupo(titulo, usuarios):
    """Exibe os usuarios de um grupo e sua quantidade."""
    print(f"//green/{titulo}/green")
    for usuario in usuarios:
        print(f"//yellow/{usuario['nome']} - {usuario['idade']} anos/yellow")
    print(f"//magenta/Quantidade: {len(usuarios)}/magenta")


def main():
    menores, adultos = agrupar_por_idade(usuarios)

    print("//bold-blue/AGRUPAMENTO DE USUARIOS/bold-blue")
    exibir_grupo("Menores de idade:", menores)
    exibir_grupo("Adultos:", adultos)


if __name__ == "__main__":
    main()


# =============================================================================
# # APRENDIZADOS E CONSOLIDACAO DE CONCEITOS
# =============================================================================
#
# for percorre usuarios e if/else separa menores e adultos
# Duas listas com append organizam cada grupo sem misturar dados
# len() conta quantos usuarios existem em cada categoria
# Funcao retorna tupla (menores, adultos) para desempacotar no main
# exibir_grupo reutiliza a mesma logica de exibicao nos dois grupos
# Animado em classificar cadastros digitais por faixa etaria
# Utilizacao da biblioteca EasyAnsi para melhoria visual do sistema
#
# Link do repositorio da biblioteca EasyAnsi: https://github.com/GustaFranz/easyansi
#
# OBRIGADO!
# FIQUE A VONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO
