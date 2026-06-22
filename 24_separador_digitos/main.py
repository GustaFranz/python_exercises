#SEPARADOR DE DÍGITOS
#Aqui, você aprenderá a decompor um número em suas unidades, dezenas, centenas e milhares. 
Esse conceito é útil para operações matemáticas, validação de dados e até mesmo em aplicações de sistemas numéricos, como leitura de CEPs ou códigos identificadores.

Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados
# Ex.: Digite um número: 1834
# Unidade: 4
# Dezena: 3
# Centena: 8
# Unidade de milhar: 1

numero = int(input('Digite um número inteiro de 0 a 9999: '))
unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
unidade_de_milhar = numero // 1000 % 10

print ('A unidade desse núnero é {}'.format(unidade))
print ('A dezena desse núnero é {}'.format(dezena))
print ('A centena desse núnero é {}'.format(centena))
print ('A unidade de milhar desse núnero é {}'.format(unidade_de_milhar))


#OBRIGADO!
#fIQUE A VONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO!
