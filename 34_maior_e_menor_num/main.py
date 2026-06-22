#Maior e Menor Número
#Comparar valores é uma habilidade essencial para programação. 
Este exercício ensina como analisar múltiplos números e identificar o maior e o menor, um conceito utilizado em estatísticas e ordenação de dados.


# Desenvolva um programa que leia três números e mostre qual é o maior e qual é o menor.

n1 = float(input('Digite um número qualquer: '))
n2 = float(input('Digite outro número qualquer: '))
n3 = float(input('Digite outro número qualquer: '))

if n1 > n2 and n1 > n3:
    print (f'Dentre os números que você digitou, {n1} é o maior')
elif n2 > n1 and n2 > n3:
    print (f'Dentre os números que você digitou, {n2} é o maior')
else:
    print (f'Dentre os números que você digitou, {n3} é o maior')

    #OBRIGADO!
#FIQUE A CONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO!
