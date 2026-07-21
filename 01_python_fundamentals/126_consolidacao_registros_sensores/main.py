# EXERCICIO 126 - Consolidacao de registros de sensores (contexto cientifico)
#
# ENUNCIADO
# Considere os dados de sensores:
# leituras = [10.5, 12.3, 11.8, 50.0, -5.0, 13.2, 14.1]
# O programa deve:
## remover valores invalidos (<= 0 ou acima de 40);
## calcular media dos valores validos;
## identificar tendencia (se media esta acima de 15 ou nao).
#
# ORIENTACOES
## Filtre dados com for.
## Crie nova lista limpa.
## Use media para analise final.
#
# --- Implemente sua solucao abaixo ---
#
# =============================================================================
# # RESOLUCAO DO EXERCICIO
# =============================================================================
import easyansi


easyansi.activate()

leituras = [10.5, 12.3, 11.8, 50.0, -5.0, 13.2, 14.1]


def filtrar_leituras_validas(leituras):
    """Mantem somente leituras maiores que zero e menores ou iguais a quarenta."""
    return [leitura for leitura in leituras if 0 < leitura <= 40]


def calcular_media(leituras):
    """Calcula a media das leituras ou retorna zero para uma lista vazia."""
    if not leituras:
        return 0.0
    return sum(leituras) / len(leituras)


def identificar_tendencia(media):
    """Informa se a media esta acima do limite de tendencia."""
    if media > 15:
        return "Acima de 15"
    return "Igual ou abaixo de 15"


def main():
    leituras_validas = filtrar_leituras_validas(leituras)
    media = calcular_media(leituras_validas)
    tendencia = identificar_tendencia(media)

    print("//bold-blue/CONSOLIDACAO DE SENSORES/bold-blue")
    print(f"//green/Leituras originais: //yellow/{leituras}/yellow")
    print(f"//green/Leituras validas: //yellow/{leituras_validas}/yellow")
    print(f"//green/Media das leituras: //magenta/{media:.2f}/magenta")
    print(f"//green/Tendencia: //magenta/{tendencia}/magenta")


if __name__ == "__main__":
    main()


# =============================================================================
# # APRENDIZADOS E CONSOLIDACAO DE CONCEITOS
# =============================================================================
#
# Filtro com condicao composta (0 < leitura <= 40) remove outliers e negativos
# List comprehension gera nova lista limpa sem alterar leituras originais
# Media com sum() / len() e retorno 0.0 quando a lista fica vazia
# Funcao de tendencia interpreta se a media esta acima ou abaixo de 15
# Fluxo completo: limpar dados, calcular media e classificar resultado
# Animado em consolidar leituras cientificas antes de tomar decisoes
# Utilizacao da biblioteca EasyAnsi para melhoria visual do sistema
#
# Link do repositorio da biblioteca EasyAnsi: https://github.com/GustaFranz/easyansi
#
# OBRIGADO!
# FIQUE A VONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO
