#É um Triângulo?
#Aqui, exploramos a matemática por trás da formação de triângulos. 
Esse conceito é essencial em áreas como engenharia, design e física, mostrando a aplicação prática da geometria na programação.

# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar triângulo.


a = float(input('Qual é a medida da reta "a"? '))
b =  float(input('Qual é a medida da reta "b"? '))
c = float(input('Qual é a medida da reta "c"? '))

if (a+b) > c or (a+c) > b or (b+c) > a:
    print ('Essas retas podem formar um triângulo.')
else:
    print ('Essas retas NÃO podem formar um triângulo.')


#OBRIGADO!
#FIQUE A CONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO!
