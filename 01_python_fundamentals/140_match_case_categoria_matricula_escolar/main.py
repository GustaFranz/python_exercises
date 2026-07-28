# EXERCICIO 140 - Categoria de matricula escolar com match/case (contexto educacional)
#
# PASSO A PASSO
## Passo 1: Crie MatriculaInvalidaError para turmas nao reconhecidas.
## Passo 2: Crie validar_turma(codigo) com match/case dentro da funcao.
##         Aceite: M (matutino), V (vespertino), N (noturno), I (integral).
##         Padronize com strip().upper() antes do match.
## Passo 3: Use case _ para lancar excecao quando o turno for invalido.
## Passo 4: Fora da funcao, leia o codigo em loop com try/except.
## Passo 5: Exiba o turno confirmado e encerre quando a entrada for valida.
#
# ENUNCIADO
# Crie um validador de turno para matricula escolar.
# O sistema deve:
## solicitar o codigo do turno (M, V, N ou I);
## exibir o nome completo do turno selecionado;
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
# M (matutino), V (vespertino), N (noturno), I (integral).

class MatriculaInvalidaError(Exception):
    """Lançada quando o codigo de matricula não for M (matutino), V (vespertino), N (noturno) ou I (integral)."""

def validar_turno_matricula(turno_bruto):
    turno = turno_bruto.strip().upper()
    match turno:
        case "M":
            return "Matutino"
        case "V":
            return "Vespertino"
        case "N":
            return "Noturno"
        case "I":
            return "Integral"
        case _:
            raise MatriculaInvalidaError("Digite uma dessas opções: M (Matutino), V (Vespertino), N (Noturno), I (Integral).")

while True:
    entrada = input("Digite o turno do aluno: ")
    turno_maiuscula = entrada.upper()

    try:
        turno = validar_turno_matricula(entrada)
        print(f"Turno registrado com sucesso. {turno_maiuscula}: {turno}")
        break

    except MatriculaInvalidaError as e:
        print(f'Turno inválido: {e}')



# =============================================================================
# # APRENDIZADOS E CONSOLIDACAO DE CONCEITOS
# =============================================================================
#
# strip().upper() garante que m, V e n caiam no mesmo padrao do match
# cada case retorna o nome completo do turno da matricula
# MatriculaInvalidaError no case _ impede turnos fora de M, V, N e I
# while True com break so encerra quando o turno fica valido
# Animado em reutilizar o padrao match/case + try/except em novo contexto
#
# OBRIGADO!
# FIQUE A VONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO
