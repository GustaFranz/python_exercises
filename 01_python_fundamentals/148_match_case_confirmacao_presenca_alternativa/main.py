# EXERCICIO 148 - Confirmacao de presenca com match/case e | (contexto educacional)
#
# OBJETIVO
# Aprender a usar o operador | no match/case para aceitar varias formas equivalentes
# de um mesmo dado (situacao comum em formularios e sistemas reais).
#
# CONCEITO - MATCH/CASE COM ALTERNATIVAS (|)
## Em sistemas reais, o usuario pode digitar a mesma resposta de formas diferentes:
## "S", "SIM", "Y" ou "YES" significam confirmacao; "N", "NAO" ou "NO" significam negacao.
## O operador | no case evita repetir o mesmo bloco varias vezes:
##   match resposta:
##       case "S" | "SIM" | "Y" | "YES":
##           return "Presenca confirmada"
##       case "N" | "NAO" | "NO":
##           return "Falta registrada"
##       case _:
##           raise RespostaInvalidaError("...")
## Antes do match, padronize a entrada:
##   resposta = entrada.strip().upper()
## Assim "sim", " Sim " e "SIM" caem no mesmo case.
## SRP (Separacao de Responsabilidades):
## - DENTRO da funcao: match/case com | valida e classifica a resposta
## - FORA da funcao: try/except trata erro e pede nova entrada
#
# PASSO A PASSO DETALHADO
## Passo 1: Crie a excecao customizada:
##     class RespostaInvalidaError(Exception):
##         """Lancada quando a resposta nao e de confirmacao nem de negacao."""
## Passo 2: Crie validar_presenca(resposta) com match/case e | DENTRO da funcao:
##     def validar_presenca(resposta):
##         resposta_limpa = resposta.strip().upper()
##         # Remove acento simples em "NAO" se quiser aceitar "NÃO"
##         resposta_limpa = resposta_limpa.replace("Ã", "A").replace("Ó", "O")
##         match resposta_limpa:
##             case "S" | "SIM" | "Y" | "YES":
##                 return "Presenca confirmada"
##             case "N" | "NAO" | "NO":
##                 return "Falta registrada"
##             case _:
##                 raise RespostaInvalidaError(
##                     "Resposta invalida. Use S/SIM/Y/YES ou N/NAO/NO."
##                 )
## Explicacao do codigo:
## - case "S" | "SIM" | "Y" | "YES": varias formas de "sim" no mesmo tratamento
## - case "N" | "NAO" | "NO": varias formas de "nao" no mesmo tratamento
## - case _: qualquer outra entrada e invalida (validacao)
## Passo 3: No fluxo principal (FORA da funcao), use try/except:
##     while True:
##         entrada = input("O aluno compareceu? (S/N): ")
##         try:
##             resultado = validar_presenca(entrada)
##             print(resultado)
##             break
##         except RespostaInvalidaError as e:
##             print(f"Erro: {e}")
#
# ENUNCIADO
# Crie um validador de confirmacao de presenca para a chamada escolar.
# O sistema deve:
## solicitar se o aluno compareceu;
## aceitar varias formas equivalentes de sim e de nao com match/case e |;
## recusar respostas invalidas sem quebrar o programa.
#
# ORIENTACOES
## Use match/case com | dentro de validar_presenca().
## Lance excecao customizada no case _.
## Trate o erro com try/except fora da funcao (SRP).
#
# --- Implemente sua solucao abaixo ---
#
# =============================================================================
# # RESOLUCAO DO EXERCICIO
# =============================================================================

class RespostaInvalidaError(Exception):
    """Lancada quando a resposta nao e de confirmacao nem de negacao."""


def validar_presenca(presenca_bruta):
    presenca = presenca_bruta.strip().upper().replace("Ã", "A").replace("Ó", "O")
    
    match presenca:
        case "S" | "SIM" | "Y" | "YES":
            return "PRESENCA"
        case "N" | "NAO" | "NO":
            return "FALTA"
        case _:
            raise RespostaInvalidaError("Digite uma resposta válida: S (SIM) ou N (NÂO)")

while True:
    entrada = input("O aluno compareceu? (S/N): ")
    entrada_maiuscula = entrada.upper()
    try:
        resultado = validar_presenca(entrada)
        if resultado == "PRESENCA":
            print("Presença registrada.")
        elif resultado == "FALTA":
            print("Ausencia registrada.")
        break
    except RespostaInvalidaError as e:
        print(f"Erro: {e}")




# =============================================================================
# # APRENDIZADOS E CONSOLIDACAO DE CONCEITOS
# =============================================================================
#
# O operador | aceita varias formas equivalentes de sim e de nao
# S|SIM|Y|YES e N|NAO|NO caem no mesmo tratamento sem repetir blocos
# replace ajuda a aceitar "NÃO" com acento apos upper()
# case _ com RespostaInvalidaError rejeita respostas fora do padrao
# Animado em usar match/case com | em formularios reais de chamada
#
# OBRIGADO!
# FIQUE A VONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO
