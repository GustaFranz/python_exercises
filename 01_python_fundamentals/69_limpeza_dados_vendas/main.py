# EXERCICIO 69 - Limpeza de dados de vendas (contexto de comercio)
#
# ENUNCIADO
# Considere a lista de vendas abaixo. Alguns valores sao invalidos e devem ser removidos antes da analise:
# vendas = [120.50, 0, 340.90, -15.0, 89.99, 560.00, 0, 230.00, -50.0, 410.75]
# O programa deve:
## criar uma nova lista apenas com valores validos (> 0);
## calcular o total arrecadado;
## identificar maior e menor venda;
## calcular a media das vendas validas.
#
# ORIENTACOES
## Filtre os dados com for.
## Ignore valores invalidos.
## Armazene em nova lista.
## Depois aplique max(), min() e sum().
#
# --- Implemente sua solucao abaixo ---
#
# =============================================================================
# # RESOLUCAO DO EXERCICIO
# =============================================================================

import easyansi
easyansi.activate()

vendas_original = [120.50, 0, 340.90, -15.0, 89.99, 560.00, 0, 230.00, -50.0, 410.75]
vendas = []

for valor in vendas_original:
    if valor > 0:
        vendas.append(valor)
    
media = sum(vendas) / len(vendas)

linha = "//yellow/" + "-" * 95 + "//yellow/"

print(linha)
## criar uma nova lista apenas com valores validos (> 0);
print(f'A lista válida é //red/{vendas}/red')
print(linha)
print(f'Quantidade de itens vendidos: //bold-green/{len(vendas)}/bold-green')
print(linha)
## calcular o total arrecadado;
print(f'Total arrecadado: R$ //bold-green/{sum(vendas):.2f}/bold-green')
print(linha)
## identificar maior e menor venda;
print(f'Maior venda: R$ //bold-green/{max(vendas):.2f}/bold-green')
print(linha)
print(f'Menor venda: R$ //bold-green/{min(vendas):.2f}/bold-green')
print(linha)
## calcular a media das vendas validas.
print(f'Media de vendas: R$ //bold-green/{media:.2f}/bold-green')


# =============================================================================
# # APRENDIZADOS E CONSOLIDACAO DE CONCEITOS
# =============================================================================

# Aplicação de filtragem de dados em listas com base em condições (valor > 0)
# Uso de listas derivadas (nova lista a partir de outra, mantendo a original intacta)
# Reforço na utilização do laço for para percorrer e validar dados
# Aplicação de funções built-in (sum(), len(), max(), min()) para análise de dados
# Organização de um fluxo completo de limpeza → processamento → análise de dados
# Melhoria na formatação de saída com f-strings e exibição de valores monetários
# Aplicação prática da biblioteca easyansi para estilização visual no terminal

# Link do repositório da biblioteca EasyAnsi: https://github.com/GustaFranz/easyansi
#

# OBRIGADO!
# FIQUE A VONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO
