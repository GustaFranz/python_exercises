# EXERCICIO 122 - Limpeza de base de dados de alunos (contexto educacional)
#
# ENUNCIADO
# Considere a seguinte base com nomes e notas, onde alguns registros estao
# inconsistentes.
# dados = [
#     {"nome": "Ana", "nota": 7.5}, {"nome": "Bruno", "nota": -3},
#     {"nome": "Carlos", "nota": 8.0}, {"nome": "Daniela", "nota": None},
#     {"nome": "Eduardo", "nota": 9.1}, {"nome": "", "nota": 5.5},
# ]
# O programa deve:
# remover registros invalidos (nota negativa, None ou nome vazio);
# criar uma nova lista limpa;
# calcular media das notas validas.
#
# ORIENTACOES
# Percorra a lista de dicionarios.
# Valide campos antes de adicionar na nova lista.
# Utilize sum() e len().
#
# --- Implemente sua solucao abaixo ---
#
# =============================================================================
# # RESOLUCAO DO EXERCICIO
# =============================================================================
import easyansi
easyansi.activate()

dados = [{"nome": "Ana", "nota": 7.5}, {"nome": "Bruno", "nota": -3},
         {"nome": "Carlos", "nota": 8.0}, {"nome": "Daniela", "nota": None},
         {"nome": "Eduardo", "nota": 9.1}, {"nome": "", "nota": 5.5}]


SEPARADOR = "---------------------------------------------------------------"


def limpar_dados(dados):
    """Remove registros invalidos e retorna uma nova lista limpa"""
    dados_limpos = []
    for registro in dados:
        nome = registro.get("nome")
        nota = registro.get("nota")
        if nome and nota is not None and nota >= 0:
            dados_limpos.append(registro)
    return dados_limpos


def calcular_media(dados):
    """Calcula a media das notas validas"""
    if not dados:
        return 0.0
    soma_notas = sum(registro["nota"] for registro in dados)
    return soma_notas / len(dados)


def exibir_registros(titulo, registros):
    """Exibe cada dicionario da lista em uma linha separada."""
    print(f"//green/{titulo}")
    for registro in registros:
        print(f"//yellow/{registro}")
    print(SEPARADOR)


def main():
    exibir_registros("Dados originais:", dados)

    dados_limpos = limpar_dados(dados)
    exibir_registros("Dados limpos:", dados_limpos)

    media = calcular_media(dados_limpos)
    print(f"//green/Media das notas validas: //magenta/{media:.2f}\n")


if __name__ == "__main__":
    main()


# =============================================================================
# # APRENDIZADOS E CONSOLIDACAO DE CONCEITOS
# =============================================================================
#
# Validacao de registros antes de incluir na lista limpa
# registro.get() acessa campos com seguranca em dicionarios
# Regras combinadas: nome nao vazio, nota nao None e nota >= 0
# Nova lista limpa preserva os dados originais intactos
# sum() e len() calculam media das notas validas
# exibir_registros reutiliza a exibicao para dados originais e limpos
# Utilizacao da biblioteca EasyAnsi para melhoria visual do sistema
#
# Link do repositorio da biblioteca EasyAnsi: https://github.com/GustaFranz/easyansi
#
# OBRIGADO!
# FIQUE A VONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO
