# DEMANDA
# Empresa: Edutech Brasil
# Setor: Educacao / integracoes
# Solicitacao: Consumir API de matriculas com tratamento correto de falhas.

# EXERCICIO 86 - Introducao a tratamento HTTP (contexto corporativo)
#
# VISAO DO BLOCO — API com tratamento HTTP (exercicios 86 a 90)
# Este bloco treina:
## 86 — Introducao: tratar 200, 404 e timeout (simulado)
## 87 — Retry simples em falha
## 88 — Mensagem amigavel para o usuario final
## 89 — Consulta com fallback quando API falha
## 90 — Cache em dict + log de falhas
#
# Conceitos basicos:
## Resposta HTTP tem status (200 ok, 404 nao encontrado, 500 erro servidor)
## Timeout = servico nao respondeu a tempo
## Sempre tratar falhas — nunca assumir sucesso
## Neste bloco use respostas simuladas (sem depender de internet)
#
# Funcao simular_api(codigo) retorna dict:
## 200 -> {"status": 200, "dados": {"aluno": "Ana", "turma": "7B"}}
## 404 -> {"status": 404, "erro": "Matricula nao encontrada"}
## 0 ou "timeout" -> {"status": 0, "erro": "Timeout"}
# Implemente consultar_matricula(codigo):
## Chama simular_api e trata cada status com mensagem adequada
## 200: exibe dados do aluno
## 404: exibe erro amigavel
## timeout: exibe "Servico indisponivel, tente mais tarde"
# Teste codigos 200, 404 e "timeout".
#
# ORIENTACOES
## Simule HTTP com dict — sem bibliotecas externas nem rede obrigatoria.
## Use if/elif por status da resposta.

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
