# EXERCICIO 136 - Validador de conceito escolar com match/case (contexto educacional)
#
# OBJETIVO
# Aprender a usar match/case para validar e classificar dados de forma organizada.
#
# CONCEITO - MATCH/CASE NA VALIDACAO DE DADOS
## O match/case (disponivel desde Python 3.10) substitui longos if/elif quando
## comparamos um valor contra varios padroes fixos.
## Estrutura basica:
##   match valor:
##       case padrao1:
##           bloco
##       case padrao2 | padrao3:
##           bloco
##       case _:
##           padrao padrao (equivalente ao else)
## Ferramentas principais:
## - case com literal: case "A": aceita exatamente "A"
## - case com alternativas (|): case "A" | "B": aceita A ou B
## - case _: captura qualquer valor nao listado (validacao de erro)
## - case com guarda (if): case n: if 0 <= n <= 10: para intervalos numericos
## Principio SRP (Separacao de Responsabilidades):
## - DENTRO da funcao: match/case define regras e retorna resultado valido
##   ou lanca excecao customizada para dados invalidos
## - FORA da funcao: try/except trata erros, exibe mensagens e permite nova entrada
#
# PASSO A PASSO DETALHADO
## Passo 1: Crie uma excecao customizada para dados invalidos:
##     class ConceitoInvalidoError(Exception):
##         """Lancada quando o conceito nao e A, B, C, D ou E."""
## Passo 2: Crie a funcao validar_conceito(conceito) com match/case DENTRO:
##     def validar_conceito(conceito):
##         conceito_limpo = conceito.strip().upper()
##         match conceito_limpo:
##             case "A":
##                 return "Excelente desempenho"
##             case "B":
##                 return "Bom desempenho"
##             case "C":
##                 return "Desempenho regular"
##             case "D":
##                 return "Desempenho insatisfatorio"
##             case "E":
##                 return "Desempenho critico"
##             case _:
##                 raise ConceitoInvalidoError(
##                     "Conceito invalido. Use A, B, C, D ou E."
##                 )
## Explicacao do codigo:
## - strip().upper() padroniza a entrada antes da comparacao
## - cada case valida um conceito permitido e retorna mensagem pedagogica
## - case _ agrupa todos os valores invalidos e lanca excecao (validacao)
## Passo 3: No fluxo principal (FORA da funcao), use try/except:
##     while True:
##         entrada = input("Digite o conceito do aluno (A a E): ")
##         try:
##             resultado = validar_conceito(entrada)
##             print(resultado)
##             break
##         except ConceitoInvalidoError as e:
##             print(f"Erro: {e}")
#
# ENUNCIADO
# Crie um validador de conceito escolar que aceita apenas A, B, C, D ou E.
# O sistema deve:
## solicitar o conceito do aluno;
## classificar o conceito com mensagem clara;
## recusar qualquer outro valor sem quebrar o programa.
#
# ORIENTACOES
## Use match/case dentro de uma funcao validar_conceito().
## Lance excecao customizada no case _.
## Trate o erro com try/except fora da funcao.
#
# --- Implemente sua solucao abaixo ---
#
# =============================================================================
# # RESOLUCAO DO EXERCICIO
# =============================================================================


# =============================================================================
# # APRENDIZADOS E CONSOLIDACAO DE CONCEITOS
# =============================================================================

#
#
# OBRIGADO!
# FIQUE A VONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO
