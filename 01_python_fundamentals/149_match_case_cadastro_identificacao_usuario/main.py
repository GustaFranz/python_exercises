# EXERCICIO 149 - Cadastro de identificacao de usuario com match/case (contexto administrativo)
#
# PASSO A PASSO
## Passo 1: Crie IdentificacaoInvalidaError para perfis nao permitidos.
## Passo 2: Crie validar_perfil(codigo) com match/case dentro da funcao.
##         Aceite: E (estudante), F (funcionario), R (responsavel), X (externo).
##         Padronize com strip().upper().
## Passo 3: Use case _ para lancar excecao quando o perfil for invalido.
## Passo 4: Fora da funcao, leia o codigo em loop com try/except.
## Passo 5: Exiba o perfil cadastrado e encerre quando a entrada for valida.
#
# ENUNCIADO
# Crie um cadastro de identificacao de usuarios na biblioteca escolar.
# Codigos aceitos: E (estudante), F (funcionario), R (responsavel), X (externo).
# O sistema deve:
## solicitar o codigo do perfil;
## exibir a categoria do usuario cadastrado;
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
