# EXERCICIO 44 - Simulador de caixa de supermercado
#
# ENUNCIADO
# Um caixa registra valores de compras sucessivamente.
# O programa deve:
#Pedir o nome do produto
## pedir valores de produtos;
#criar lista de produtos
#criar lista de valores
# Criar dicionario com produtos e valores
## somar o total;
## parar quando o usuário digitar 0.
#
# ORIENTACOES
## Use while
## Use variável acumuladora (total)
## 0 deve encerrar o loop
## Ignore valores negativos
#
# --- Implemente sua solucao abaixo ---
#
# =============================================================================
# # RESOLUÇÃO DO EXERCÍCIO
# =============================================================================

import easyansi
easyansi.activate()

print("//magenta/=/magenta" * 95)
print("REGISTRO DE COMPRAS")
print("//magenta/=/magenta" * 95)

lista_produtos = []
lista_valores = []
produtos_dict = {}
valor_total = 0
quant_produtos = 0

while True:
    
    produto = input('Nome do produto [0 para encerrar]: ').strip().title()

    if produto == "0":
        break

    if produto == '':
        print('//red/Registo inválido! Certifique-se de escrever o nome de um produto ou SAIR [S] para finalizar/red') 
        continue
    
    while True:
        valor = float(input('Valor do produto: ').replace(',', '.'))
          
        if valor < 0: 
            print('Registre um valor positivo!')
            continue
        
        if valor == 0:
            print('Digite um valor diferente de zero.')
            continue
        break

    lista_produtos.append(produto)
    lista_valores.append(valor)
    produtos_dict[produto] = valor
    valor_total += valor
    quant_produtos += 1

print("//yellow/=/yellow" * 95)
print("//green/RELATÓRIO DE PRODUTOS E VALORES/green")
print("//yellow/=/yellow" * 95)

print("-" * 95)

for produto, valor in produtos_dict.items():
    print(f'Produto: {produto:<25} | Valor: {valor:>20.2f}')
    print("-" * 95)
linha1 = f"QUANT. TOTAL: {quant_produtos}"
linha2 = f"Valor: {valor_total:.2f}"
print(f'//yellow/{linha1:<35} | {linha2:>25}/yellow')

# =============================================================================
# # APRENDIZADOS E CONSOLIDAÇÃO DE CONCEITOS
# =============================================================================

# Aplicação de loops aninhados (while) para controle estruturado de entrada de dados
# Uso dos comandos break e continue para gerenciamento do fluxo e validação de dados
# Oportunidade de relembrar e aplicar listas (list) para armazenamento sequencial de informações
# Aplicação de dicionários (dict) para associação entre produtos e seus respectivos valores
# Uso de variável acumuladora para cálculo do total de compras
# Aplicação de formatação com f-strings, incluindo alinhamento (<, >) e controle de casas decimais (:.2f)
# Aplicação da biblioteca própria easyansi para estilização e organização visual da saída no terminal
# 
# LINK PARA O REPOSITÓRIO DA BIBLIOTECA EasyAnsi: https://github.com/GustaFranz/easyansi
#
# OBRIGADO!
# FIQUE A VONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO
