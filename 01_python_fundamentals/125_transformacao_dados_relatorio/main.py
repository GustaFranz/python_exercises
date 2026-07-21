# EXERCICIO 125 - Transformacao de dados para relatorio (contexto educacional)
#
# ENUNCIADO
# Considere a lista de notas abaixo:
# notas = [7.5, 3.2, 8.0, 6.5, 4.0, 9.1]
# O programa deve:
## criar uma nova lista com notas normalizadas (multiplicadas por 10);
## gerar lista de notas arredondadas com 1 casa decimal;
## identificar quantas notas estao acima de 70 (apos normalizacao).
#
# ORIENTACOES
## Use listas derivadas.
## Utilize round().
## Mantenha a lista original intacta.
#
# --- Implemente sua solucao abaixo ---
#
# =============================================================================
# # RESOLUCAO DO EXERCICIO
# =============================================================================
import easyansi
easyansi.activate()

notas = [7.5, 3.2, 8.0, 6.5, 4.0, 9.1]


def normalizar_notas(notas):
    """Multiplica cada nota por dez sem alterar a lista original."""
    return [nota * 10 for nota in notas]


def arredondar_notas(notas):
    """Retorna as notas arredondadas para uma casa decimal."""
    return [round(nota, 1) for nota in notas]


def contar_notas_acima_de_setenta(notas_normalizadas):
    """Conta quantas notas normalizadas sao maiores que setenta."""
    return sum(nota > 70 for nota in notas_normalizadas)


def main():
    notas_normalizadas = normalizar_notas(notas)
    notas_arredondadas = arredondar_notas(notas_normalizadas)
    quantidade_acima_de_setenta = contar_notas_acima_de_setenta(notas_normalizadas)

    print("//bold-blue/RELATORIO DE NOTAS/bold-blue")
    print(f"//green/Notas originais: //yellow/{notas}/yellow")
    print(f"//green/Notas normalizadas: //yellow/{notas_normalizadas}/yellow")
    print(f"//green/Notas arredondadas: //yellow/{notas_arredondadas}/yellow")
    print(
        "//green/Notas acima de 70: "
        f"//magenta/{quantidade_acima_de_setenta}/magenta"
    )


if __name__ == "__main__":
    main()


# =============================================================================
# # APRENDIZADOS E CONSOLIDACAO DE CONCEITOS
# =============================================================================
#
# List comprehension cria notas normalizadas (nota * 10) sem alterar a original
# round(nota, 1) arredonda cada valor para uma casa decimal
# sum(nota > 70 for nota in ...) conta quantas notas passam do limite
# Pipeline de transformacao: normalizar, arredondar e depois analisar
# Lista original intacta enquanto listas derivadas recebem as mudancas
# Animado em montar relatorios educacionais com dados transformados
# Utilizacao da biblioteca EasyAnsi para melhoria visual do sistema
#
# Link do repositorio da biblioteca EasyAnsi: https://github.com/GustaFranz/easyansi
#
# OBRIGADO!
# FIQUE A VONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO
