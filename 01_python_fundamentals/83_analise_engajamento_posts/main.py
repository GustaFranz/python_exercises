# EXERCICIO 83 - Analise de engajamento de posts (contexto digital)
#
# ENUNCIADO
# Considere o seguinte dicionario de posts e curtidas:
# posts = {"post1": 120, "post2": 45, "post3": 300, "post4": 90, "post5": 15, "post6": 600}
# O programa deve:
## classificar cada post como baixo, medio ou alto engajamento;
## criar tres novos dicionarios com essas categorias;
## identificar o post mais engajado.
#
# ORIENTACOES
## Use condicoes dentro do loop com .items().
## Crie novos dicionarios.
## Utilize max().
#
# --- Implemente sua solucao abaixo ---
#
# =============================================================================
# # RESOLUCAO DO EXERCICIO
# =============================================================================

# Seguindo a classificação do exercício 72 que dizia:
# baixo desempenho: 0 a 100 
# médio desempenho 101 a 299
# alto desempenho: a partir de 300
import easyansi
easyansi.activate()

baixo_desempenho = {}
medio_desempenho = {}
alto_desempenho = {}

posts = {"post1": 120, "post2": 45, "post3": 300, "post4": 90, "post5": 15, "post6": 600}

for post, curtidas in posts.items():
    if posts[post] < 100:
        baixo_desempenho[post] = curtidas
    
    elif posts[post] < 300:
        medio_desempenho[post] = curtidas
    
    else:
        alto_desempenho[post] = curtidas
    
print(f'//green/O dicionário de posts com baixo engajamento é:/green //yellow/{baixo_desempenho}/yellow')
print(f'//green/O dicionário de posts com médio engajamento é:/green //yellow/{medio_desempenho}/yellow')
print(f'//green/O dicionário de posts com alto engajamento é:/green //yellow/{alto_desempenho}/yellow')
print("-"*105)
print(f'//green/O post com maior engajamento é:/green //yellow/{max(posts, key=posts.get)}/yellow')

print(f'O post com maior engajamento é: {max(posts, key=posts.get)}')


# =============================================================================
# # APRENDIZADOS E CONSOLIDACAO DE CONCEITOS
# =============================================================================

#
#
# OBRIGADO!
# FIQUE A VONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO
