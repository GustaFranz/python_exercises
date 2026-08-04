# EXERCÍCIO 04: Ranking de Engajamento Editorial (EduConnect)
# Empresa: Rede Social EduConnect
# Setor: Mídia / Comunicação Escolar
# Demanda: Priorizar posts do backlog editorial pelo engajamento relativo ao total da página.

# Dados de Entrada:

# # posts = [
# #     {"titulo": "Feira de Ciencias", "curtidas": 120, "compartilhamentos": 15},
# #     {"titulo": "Aviso Prova", "curtidas": 45, "compartilhamentos": 2},
# #     {"titulo": "Projeto Leitura", "curtidas": 200, "compartilhamentos": 40},
# #     {"titulo": "Recesso", "curtidas": 30, "compartilhamentos": 1},
# #     {"titulo": "Hackathon", "curtidas": 90, "compartilhamentos": 12},
# # ]

# =========================================================================================================
# 📌 ORIENTAÇÕES E REGRAS DE NEGÓCIO (LEIA ANTES DE COMECAR)
# Peso do Engajamento (Score):
# Na EduConnect, 1 compartilhamento vale por 3 curtidas.
# Fórmula: score = curtidas + (compartilhamentos * 3)
# Taxa % de Engajamento:
# É a porcentagem do score de um post individual em relação à soma de todos os scores.
# Fórmula: taxa = (score_do_post / total_de_scores) * 100
# Tratamento de Erros:
# Ao calcular a taxa, previna erro de divisão por zero usando operador ternário: round(score / total * 100, 1) if total > 0 else 0.0.
# Estrutura do Dicionário:
# Ao criar novas listas via List Comprehension, mantenha a estrutura de dicionário em Python: {"titulo": ..., "score": ...}.

# # =========================================================================================================
# 🎯 SUAS TAREFAS DE IMPLEMENTAÇÃO
# Passo 1 (List Comprehension - Scores):
# Crie uma lista scores gerando um dicionário {"titulo": ..., "score": ...} para cada post da lista posts.
# Passo 2 (List Comprehension - Taxa %):
# Calcule o total geral dos scores (total_scores = sum(...)).
# Crie uma nova lista scores_com_taxa usando List Comprehension que adicione a chave "taxa" nos dicionários (com valor arredondado em 1 casa decimal).
# Passo 3 (Ordenação - Top 3):
# Crie a lista top_3 filtrando os 3 maiores scores usando sorted() com key=lambda e reverse=True.
# Passo 4 (Relatório):
# Imprima no console o total de posts analisados, o score médio da página e os dados do Top 3 (Título, Score e Taxa %).

# =============================================================================
# # RESOLUCAO DO EXERCICIO
# =============================================================================
import easyansi

easyansi.activate()

posts = [
    {"titulo": "Feira de Ciencias", "curtidas": 120, "compartilhamentos": 15},
    {"titulo": "Aviso Prova", "curtidas": 45, "compartilhamentos": 2},
    {"titulo": "Projeto Leitura", "curtidas": 200, "compartilhamentos": 40},
    {"titulo": "Recesso", "curtidas": 30, "compartilhamentos": 1},
    {"titulo": "Hackathon", "curtidas": 90, "compartilhamentos": 12},
]

scores = [{"titulo": post["titulo"], 
          "score": post["curtidas"] + (post["compartilhamentos"] * 3)}
        for post in posts]

total_scores = sum(item["score"] for item in scores)

scores_com_taxa = [{"titulo": item["titulo"], 
                   "score": item["score"], 
                   "taxa": round(item["score"] / total_scores * 100, 1) if total_scores > 0 else 0.0}
                   for item in scores]

top_3 = sorted(scores_com_taxa, key=lambda x: x["score"], reverse=True)[:3]

# prints temporarios para controle
# print(scores)
# print(scores_com_taxa)
total_posts = len(posts)
score_medio = round(total_scores / total_posts, 1) if total_posts > 0 else 0.0

# A questão pede: Imprima no console o total de posts analisados, o score médio da página e os dados do Top 3 (Título, Score e Taxa %).
print("\n//magenta/===========================================================================/magenta")
print("//green/     RELATÓRIO DE ENGAJAMENTO EDITORIAL     /green")
print("//magenta/===========================================================================/magenta")
print(f"//blue-underline/TOTAL DE POSTS ANALISADOS: //yellow/{total_posts}")
print(f"//green/Score total da página:     //yellow/{total_scores}")
print(f"//green/Score médio por post:      //yellow/{score_medio}")
print("//green/---------------------------------------------------------------------------/green")
print("//green/     TOP 3 POSTS CAMPEÕES:/green")
for posicao, post in enumerate(top_3, 1):
    print(
        f'//yellow/{posicao}º | //green/{post["titulo"]:<20} | '
        f'//green/Score: //yellow/{post["score"]} | //green/Taxa de engajamento: //yellow/{post["taxa"]}'
    )

print("//magenta/===========================================================================/magenta\n")


# =============================================================================
# # APRENDIZADOS E CONSOLIDACAO DE CONCEITOS
# =============================================================================
#
# List comprehension gera dicionarios novos: titulo + score a partir de cada post
# Score ponderado: curtidas + (compartilhamentos * 3) — compartilhar pesa mais
# Uma segunda comprehension acrescenta a taxa % com base no total_scores
# Operador ternario evita divisao por zero quando o total de scores e 0
# sorted(..., key=lambda, reverse=True)[:3] monta o ranking Top 3
# EasyAnsi colore o relatorio: = em magenta, Top 3 em amarelo, textos em verde
#
# Link do repositorio da biblioteca EasyAnsi: https://github.com/GustaFranz/easyansi
#
# OBRIGADO!
# FIQUE A VONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO
