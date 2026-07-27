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


# =============================================================================
# # APRENDIZADOS E CONSOLIDACAO DE CONCEITOS
# =============================================================================

#
#
# OBRIGADO!
# FIQUE A VONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO
