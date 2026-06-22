#ALUGUEL DE CARROS

#Escreva um programa que pergunte a quantidade de km percorridos por carro alugado e
#a quantidade de dias pelos quais ele foi alugado.
#Calcule o preço a pagar, sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km

dias = float(input("Por quantos dias o veículo foi alugado? "))
km = float(input("Quantos quilômetros o veículo rodou? "))
valor_pagar = (60*dias) + (0.15*km)

print("o valor a ser pago pelo aluguel do seu veículo é R${:.2f}".format(valor_pagar))

#OBSERVAÇÕES
# A função "{:.2f}".format(variavel) é usada em Python para formatar números decimais, controlando a quantidade de casas decimais exibidas no resultado.
# O que significa {:.2f}?
# {}:
# É um espaço reservado onde o valor da variável será inserido.
# : (dois pontos):
# Indica o início das especificações de formatação para o valor a ser exibido.
# .2f:
# . (ponto): Define que o número deve ser formatado como decimal.
# 2: Define que o número terá duas casas decimais.
# f: Significa que o número será formatado como um número de ponto flutuante (float).

#Obrigado por visualizar meus exercícios.
#Fique a vontade para contribuir com meu trabalho comentando e sugerindo mudanças.
