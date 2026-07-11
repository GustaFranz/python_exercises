# EXERCICIO 82 - Controle de estoque de loja (contexto de comercio)
#
# ENUNCIADO
# Considere o estoque inicial de uma loja:
# estoque = {"camiseta": 20, "calca": 15, "tenis": 10, "bone": 30, "meia": 50}
# O programa deve reduzir o estoque conforme as vendas abaixo e atualizar o dicionario original:
# vendas = {"camiseta": 3, "calca": 5, "tenis": 2, "bone": 10, "meia": 20}
#
# ORIENTACOES
## Percorra o dicionario de vendas.
## Atualize o estoque correspondente.
## Evite valores negativos.
#
# --- Implemente sua solucao abaixo ---
#
# =============================================================================
# # RESOLUCAO DO EXERCICIO
# =============================================================================
import easyansi
easyansi.activate()

estoque = {"camiseta": 20, "calca": 15, "tenis": 10, "bone": 30, "meia": 50}
vendas = {"camiseta": 3, "calca": 5, "tenis": 2, "bone": 10, "meia": 20}

for mercadoria, quantidade in vendas.items():
    if mercadoria in estoque:
        estoque[mercadoria] -= quantidade
        if estoque[mercadoria] < 0:
            estoque[mercadoria] = 0

print(f'//green/estoque atualizado:/green //yellow/{estoque}/yellow')
# =============================================================================
# # APRENDIZADOS E CONSOLIDACAO DE CONCEITOS
# =============================================================================
#
# Cruzar vendas e estoque pelo mesmo nome de chave
# Atualizar quantidade e impedir estoque negativo
# Dict como tabela mutavel de produtos
# Utilizacao da biblioteca EasyAnsi para melhoria visual do sistema
#
# Link do repositorio da biblioteca EasyAnsi: https://github.com/GustaFranz/easyansi
#
# OBRIGADO!
# FIQUE A VONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO
