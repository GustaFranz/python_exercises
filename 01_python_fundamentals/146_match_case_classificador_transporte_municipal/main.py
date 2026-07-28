# EXERCICIO 146 - Classificador de transporte municipal com match/case (contexto urbano)
#
# PASSO A PASSO
## Passo 1: Crie TransporteInvalidoError para linhas nao reconhecidas.
## Passo 2: Crie classificar_linha(codigo) com match/case dentro da funcao.
##         Aceite: 1 (urbana), 2 (interbairros), 3 (expressa), 4 (circular escolar).
##         Padronize com strip() antes do match (codigos numericos como texto).
## Passo 3: Use case _ para lancar excecao em codigos invalidos.
## Passo 4: Fora da funcao, leia o codigo em loop com try/except.
## Passo 5: Exiba o tipo de linha e encerre quando valido.
#
# ENUNCIADO
# Crie um classificador de linhas de transporte municipal para alunos.
# Codigos aceitos: 1 (urbana), 2 (interbairros), 3 (expressa), 4 (circular escolar).
# O sistema deve:
## solicitar o codigo da linha;
## exibir a classificacao do transporte;
## permitir nova tentativa em caso de codigo invalido.
#
# ORIENTACOES
## match/case na funcao; try/except no fluxo principal (SRP).
#
# --- Implemente sua solucao abaixo ---
#
# =============================================================================
# # RESOLUCAO DO EXERCICIO
# =============================================================================
import easyansi

easyansi.activate()


class TransporteInvalidoError(Exception):
    """Lançada quando o codigo da linha nao e 1, 2, 3 ou 4."""


def classificar_linha(codigo_bruto):
    codigo = codigo_bruto.strip()
    match codigo:
        case "1":
            return "Urbana"
        case "2":
            return "Interbairros"
        case "3":
            return "Expressa"
        case "4":
            return "Circular escolar"
        case _:
            raise TransporteInvalidoError(
                "Digite uma dessas opcoes: 1 (Urbana), 2 (Interbairros), 3 (Expressa), 4 (Circular escolar)."
            )


while True:
    entrada = input(
        "| 1 (Urbana)\n"
        "| 2 (Interbairros)\n"
        "| 3 (Expressa)\n"
        "| 4 (Circular escolar)\n"
        "| Digite o codigo da linha: "
    )
    try:
        linha = classificar_linha(entrada)
        print(
            f"\n//green/Linha classificada:/green "
            f"//yellow/{entrada.strip()}/yellow — //bold-green/{linha}/bold-green\n"
        )
        break
    except TransporteInvalidoError as e:
        print(f"\n//bold-red/Codigo invalido./bold-red //red/{e}/red\n")


# =============================================================================
# # APRENDIZADOS E CONSOLIDACAO DE CONCEITOS
# =============================================================================
#
# match/case com codigo numerico em texto classifica a linha de transporte
# strip() padroniza a entrada antes da comparacao
# try/except fora da funcao garante nova tentativa sem quebrar o programa
# Utilizacao da biblioteca EasyAnsi para melhoria visual do sistema
#
# Link do repositorio da biblioteca EasyAnsi: https://github.com/GustaFranz/easyansi
#
# OBRIGADO!
# FIQUE A VONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO
