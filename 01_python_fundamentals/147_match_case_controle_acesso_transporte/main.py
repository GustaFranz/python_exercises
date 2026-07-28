# EXERCICIO 147 - Controle de acesso ao transporte escolar (contexto urbano)
#
# ENUNCIADO
# Crie um controle de acesso completo para o transporte escolar municipal.
# O programa deve solicitar e validar TRES informacoes, nesta ordem:
#
## 1) Perfil do usuario
##    Codigos aceitos: A (aluno), P (professor), M (monitor), V (visitante).
##    Exiba o tipo de usuario autorizado.
#
## 2) Linha de transporte
##    Codigos aceitos: 1 (urbana), 2 (interbairros), 3 (expressa), 4 (circular escolar).
##    Exiba a classificacao da linha.
#
## 3) Turno de embarque (caso levemente mais trabalhoso)
##    Codigos aceitos: MANHA, TARDE ou NOITE (aceite tambem abreviações M, T e N).
##    Alem de validar o turno, o sistema deve verificar a regra de permissao:
##    - aluno, professor e monitor: podem embarcar em qualquer turno valido;
##    - visitante: so pode embarcar no turno da MANHA;
##    - se o visitante informar TARDE ou NOITE, recuse com mensagem clara.
##    Dica: voce pode validar o turno com match/case e, em seguida, combinar
##    perfil + turno (outro match ou uma regra simples) para aplicar a restricao.
#
# O sistema deve:
## pedir cada dado ate ficar valido (nova tentativa em caso de erro);
## usar uma funcao com match/case para cada validacao (ou funcoes separadas);
## tratar erros com try/except fora das funcoes (SRP);
## ao final, exibir um resumo com perfil, linha e turno autorizados.
#
# ORIENTACOES
## Use match/case dentro das funcoes de validacao.
## Trate erros com try/except fora das funcoes (SRP).
## A terceira validacao exige mais de um criterio (turno valido + regra do visitante).
#
# --- Implemente sua solucao abaixo ---
#
# =============================================================================
# # RESOLUCAO DO EXERCICIO
# =============================================================================

import easyansi
easyansi.activate()

class UsuarioInvalidoError(Exception):
    """Lançada quando o usuario não registra uma opção válida para o perfil de usuário: A (aluno), P (professor), M (monitor), V (visitante)."""

class LinhaInvalidaError(Exception):
    """Lançada quando o usuário não registra uma opção de linha de transporte válida: 1 (urbana), 2 (interbairros), 3 (expressa), 4 (circular escolar)."""

class TurnoInvalidoError(Exception):
    """Lançada quando o usuário não registra uma opção valida para o turno: M/Manhã, T/Tarde e N/Noite."""


def validar_usuario(perfil):
    perfil_usuario = perfil.strip().upper()
        
    match perfil_usuario:
        case "A" | "ALUNO":
            return "Aluno"
        case "P" | "PROFESSOR":
            return "Professor"
        case "M" | "MONITOR":
            return "Monitor"
        case "V" | "VISITANTE":
            return "Visitante"
        case _:
            raise UsuarioInvalidoError("\nEscolha uma das opções: \n"
                                       "A | (aluno), \n"
                                       "P | (professor), \n"
                                       "M | (monitor), \n"
                                       "V | (visitante). \n")

def exibir_menu_usuario():
    print("""//blue/----------------------------------------------------------/blue
OPÇÕES DE USUÁRIO:  //blue/(A) | Aluno
                    (P) | Professor
                    (M) | Monitor
                    (V) | Visitante
----------------------------------------------------------/blue""")
    
def validar_tipo_de_linha(tipo_linha):
    linha = tipo_linha.strip()
    match linha:
        case "1":
            return "Urbana"
        case "2":
            return "Interbairros"
        case "3":
            return "Expressa"
        case "4":
            return "Circular Escolar"
        case _:
            raise LinhaInvalidaError("\nEscolha uma das opções:  \n"
                                     "1 | (Urbana), \n"
                                     "2 | (Interbairros), \n"
                                     "3 | (Expressa), \n"
                                     "4 | (Circular escolar).")

def exibir_menu_linha():
    print("""//blue/----------------------------------------------------------/blue
OPÇÕES DE LINHA:    //blue/(1) | Urbana
                    (2) | Interbairros
                    (3) | Expressa
                    (4) | Circular escolar
----------------------------------------------------------//blue/""")

def validar_turno(turno_embarque):
    turno = turno_embarque.strip().upper()
    match turno:
        case "M" | "MANHÃ":
            return "Manhã"
        case "T" | "TARDE":
            return "Tarde"
        case "N" | "NOITE":
            return "Noite"
        case _:
            raise TurnoInvalidoError("\nDigite uma das opções:\n"
                                     "M | Manhã \n"
                                     "T | Tarde \n"
                                     "N | Noite \n")


def exibir_menu_turno():
    print("""//blue/----------------------------------------------------------/blue
OPÇÕES DE TURNO:    //blue/(M) | Manhã
                    (T) | Tarde
                    (N) | Noite
----------------------------------------------------------//blue/""")


def validar_permissao(usuario_validado, turno_validado):
    """recebo os dados ja validados de usuario e turno e verifica se tem acesso."""
    match (usuario_validado, turno_validado):
        case ("Visitante", "Tarde" | "Noite"):
            raise PermissaoInvalidaError("Usuário só tem permissão para utilizar o transporte no turno da manhã")
        case _:
            return True

while True:
    try:
        exibir_menu_usuario()
        entrada_usuario = input("Selecione um tipo de usuário: ")
        
        usuario_padronizado = entrada_usuario.upper()
        usuario = validar_usuario(entrada_usuario)
        break

    except UsuarioInvalidoError as e:
        print(f'Usuário inválido: {e}')

while True:
    try:
        exibir_menu_linha()
        entrada_linha = input("Linha de transporte: ")
        linha = validar_tipo_de_linha(entrada_linha)
        break
    except LinhaInvalidaError as e:
        print(f'Linha inválida: {e}')

while True:
    try:
        exibir_menu_turno()
        entrada_turno = input("Turno: ")
        turno = validar_turno(entrada_turno)
        turno_padronizado = entrada_turno.upper()
        break
    except TurnoInvalidoError as e:
        print(f'Turno inválido: {e}')

while True:
    try:
        pernissao = validar_permissao(usuario, turno)
        print("\n//magenta/================================================================================/magenta")
        print("                      EMBARQUE AUTORIZADO COM SUCESSO!                            ")
        print(f'\n               //yellow/Usuário/yellow: {usuario} | //yellow/Linha:/yellow {linha} | //yellow/Turno:/yellow {turno}')
        print("//magenta/================================================================================/magenta \n")
        break

    except Exception:
        print("\n================================================================================")
        print('O usuário só tem permissão de acesso para o turno da manhã')
        print("================================================================================\n")
        break



# =============================================================================
# # APRENDIZADOS E CONSOLIDACAO DE CONCEITOS
# =============================================================================
#
# Tres validacoes em sequencia, cada uma com funcao e try/except proprio
# match/case com | aceita MANHA/M, TARDE/T e NOITE/N no mesmo tratamento
# segundo match combina perfil + turno para restringir visitante a Manha
# SRP: regras dentro das funcoes; tratamento de erro e interface fora
# Utilizacao da biblioteca EasyAnsi para melhoria visual do sistema
#
# Link do repositorio da biblioteca EasyAnsi: https://github.com/GustaFranz/easyansi
#
# OBRIGADO!
# FIQUE A VONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO
