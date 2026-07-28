# EXERCICIO 149 - Classificador de dia da semana com match/case e | (contexto educacional)
#
# PASSO A PASSO
## Passo 1: Crie DiaInvalidoError para abreviações nao reconhecidas.
## Passo 2: Crie classificar_dia(abreviacao) com match/case e | dentro da funcao.
##         Padronize com strip().upper() antes do match.
##         Agrupe dias uteis no mesmo case:
##         case "SEG" | "TER" | "QUA" | "QUI" | "SEX":
##             return "Dia util — aulas e atividades regulares"
##         Agrupe fim de semana:
##         case "SAB" | "DOM":
##             return "Fim de semana — sem aula regular"
## Passo 3: Use case _ para lancar DiaInvalidoError.
## Passo 4: Fora da funcao, leia a abreviação em loop com try/except.
## Passo 5: Exiba a classificacao quando a entrada for valida e encerre o loop.
#
# ENUNCIADO
# Crie um classificador de dias para o calendario escolar.
# O sistema deve:
## solicitar a abreviação do dia (SEG, TER, QUA, QUI, SEX, SAB ou DOM);
## classificar como dia util ou fim de semana usando match/case com |;
## recusar abreviações invalidas sem encerrar o programa.
#
# ORIENTACOES
## match/case com | dentro da funcao; try/except fora da funcao (SRP).
## Agrupe valores equivalentes no mesmo case com o operador |.
#
# --- Implemente sua solucao abaixo ---
#
# =============================================================================
# # RESOLUCAO DO EXERCICIO
# =============================================================================
import easyansi

easyansi.activate()


class DiaInvalidoError(Exception):
    """Lançada quando a abreviacao do dia nao e reconhecida."""


def classificar_dia(abreviacao_bruta):
    dia = abreviacao_bruta.strip().upper()
    match dia:
        case "SEG" | "TER" | "QUA" | "QUI" | "SEX":
            return "Dia util — aulas e atividades regulares"
        case "SAB" | "DOM":
            return "Fim de semana — sem aula regular"
        case _:
            raise DiaInvalidoError(
                "Digite SEG, TER, QUA, QUI, SEX, SAB ou DOM."
            )


while True:
    entrada = input(
        "| SEG TER QUA QUI SEX (dia util)\n"
        "| SAB DOM (fim de semana)\n"
        "| Digite a abreviacao do dia: "
    )
    entrada_maiuscula = entrada.strip().upper()
    try:
        classificacao = classificar_dia(entrada)
        print(
            f"\n//green/Dia classificado:/green "
            f"//yellow/{entrada_maiuscula}/yellow — //bold-green/{classificacao}/bold-green\n"
        )
        break
    except DiaInvalidoError as e:
        print(f"\n//bold-red/Dia invalido./bold-red //red/{e}/red\n")


# =============================================================================
# # APRENDIZADOS E CONSOLIDACAO DE CONCEITOS
# =============================================================================
#
# O operador | agrupa varios dias uteis no mesmo case sem repetir codigo
# SAB | DOM concentra o tratamento de fim de semana em um unico bloco
# strip().upper() padroniza a abreviacao antes do match
# try/except fora da funcao mantem o SRP e permite nova tentativa
# Utilizacao da biblioteca EasyAnsi para melhoria visual do sistema
#
# Link do repositorio da biblioteca EasyAnsi: https://github.com/GustaFranz/easyansi
#
# OBRIGADO!
# FIQUE A VONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO
