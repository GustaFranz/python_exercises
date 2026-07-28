# EXERCICIO 137 - Classificador de rendimento do aluno com match/case (contexto educacional)
#
# PASSO A PASSO
## Passo 1: Crie a excecao RendimentoInvalidoError para siglas nao permitidas.
## Passo 2: Crie a funcao classificar_rendimento(sigla) com match/case dentro da funcao.
##         Padronize a entrada com strip().upper() antes do match.
##         Aceite apenas: MB (muito bom), B (bom), R (regular), I (insuficiente).
##         Use case _ para lancar excecao quando a sigla for invalida.
## Passo 3: Fora da funcao, leia a sigla do usuario em um loop.
## Passo 4: Use try/except para capturar RendimentoInvalidoError e pedir nova entrada.
## Passo 5: Exiba a classificacao quando a sigla for valida e encerre o loop.
#
# ENUNCIADO
# Crie um classificador de rendimento escolar baseado em siglas.
# O sistema deve:
## solicitar a sigla de rendimento (MB, B, R ou I);
## exibir a descricao correspondente ao rendimento;
## impedir siglas invalidas sem encerrar o programa.
#
# ORIENTACOES
## match/case dentro da funcao; try/except fora da funcao.
## Respeite o principio SRP.
#
# --- Implemente sua solucao abaixo ---
#
# =============================================================================
# # RESOLUCAO DO EXERCICIO
# =============================================================================
class ConceitoInvalidoError(Exception):
    """Lançada quando o conceito de rendimento não for MB, B, R ou I"""

def validar_rendimento(conceito):
    rendimento = conceito.strip().upper()
    match rendimento:
        case "MB":
            return "muito bom"
        case "B":
            return "bom"
        case "R":
            return "regular"
        case "I":
            return "insuficiente"
        case _:
            raise ConceitoInvalidoError("Conceito inválido. Use uma dessas opções: MB (muito bom), B (bom), R (regular), I (insuficiente).")

while True:
    entrada = input("Digite o rendimento do aluno (MB, B, R ou I): ")
    entrada_padronizada = entrada.upper()

    try:
        resultado = validar_rendimento(entrada)
        print(f'Conceito registrado com sucesso. {entrada_padronizada}: {resultado}')
        break

    except ConceitoInvalidoError as e:
        print(f"Erro: {e}")
    


# =============================================================================
# # APRENDIZADOS E CONSOLIDACAO DE CONCEITOS
# =============================================================================
#
# Reaproveitei a estrutura do exercicio anterior mudando so o contexto
# match/case classifica MB, B, R e I com mensagens claras
# Excecao customizada no case _ impede siglas invalidas
# while True com try/except pede nova entrada ate o rendimento ficar valido
# Animado em consolidar match/case na validacao de dados escolares
#
# OBRIGADO!
# FIQUE A VONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO
