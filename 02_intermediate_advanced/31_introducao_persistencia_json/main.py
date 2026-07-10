# DEMANDA
# Empresa: TaskFlow Produtividade
# Setor: Software / tarefas
# Solicitacao: Salvar lista de tarefas em arquivo JSON para retomar depois.

# EXERCICIO 31 - Introducao a persistencia JSON (contexto corporativo)
#
# VISAO DO BLOCO — Persistencia JSON (exercicios 31 a 35)
# Este bloco treina:
## 31 — Introducao: salvar lista de tarefas
## 32 — Carregar JSON
## 33 — Append em arquivo existente
## 34 — Backup incremental de cadastro
## 35 — Sincronizar memoria e arquivo com validacao
#
# Conceitos basicos:
## import json
## json.dump(obj, arquivo) para gravar
## json.load(arquivo) para ler
## ensure_ascii=False para acentos em PT-BR
#
# tarefas = [
#     {"id": 1, "titulo": "Revisar proposta", "concluida": False},
#     {"id": 2, "titulo": "Enviar relatorio", "concluida": True},
# ]
# Salve em "tarefas.json" usando json.dump com indent=2 e ensure_ascii=False.
# Confirme gravacao exibindo mensagem e caminho do arquivo.
#
# ORIENTACOES
## with open("tarefas.json", "w", encoding="utf-8") as arquivo:
##     json.dump(tarefas, arquivo, indent=2, ensure_ascii=False)
## Arquivo sera criado na pasta do exercicio ao executar.

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
