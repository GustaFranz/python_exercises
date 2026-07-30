# DEMANDA
# Empresa: Secretaria Digital
# Setor: Educacao / atendimento
# Solicitacao: Painel CLI para cadastro rapido de alunos com tratamento de erro e auditoria de encerramento.

# EXERCICIO 57 - Try except: menu CLI robusto com log de sessao (contexto corporativo)
#
# cadastros = []
#
# Loop principal (while True):
#   Exibir menu: 1 Listar | 2 Cadastrar nome | 0 Sair
#   try:
#     opcao = int(input("Opcao: ").strip())
#   except ValueError:
#     print("Opcao invalida — digite um numero.")
#     continue
#
#   if opcao == 0: break
#   elif opcao == 1: listar cadastros
#   elif opcao == 2:
#     nome = input("Nome: ").strip()
#     if not nome: print("Nome vazio nao permitido."); continue
#     cadastros.append(nome)
#   else: print("Opcao inexistente.")
#
# Envolver o loop em try/finally (ou finally no fim do main):
#   finally -> with open("sessao.log", "a") escreve "Sessao encerrada"
#
# ORIENTACOES
## Menu real com loop — nao basta uma unica pergunta.
## .strip() ajuda a tratar espacos; vazio apos strip deve ser rejeitado.
## finally garante log mesmo se houver erro inesperado durante a sessao.
## Teste: opcao "abc", Enter vazio, cadastro valido, listar, sair.

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
