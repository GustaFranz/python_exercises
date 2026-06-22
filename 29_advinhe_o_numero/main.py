#Adivinhe o Número!
#Este programa explora conceitos fundamentais de lógica e aleatoriedade. 
Ele desafia o usuário a adivinhar um número gerado pelo computador, ajudando a compreender a interação entre entrada de dados e processamento de informações.


# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça
# para o usuário tentar descobrir qual foi o número escolhido pelo computador:
# O programa deverá escrever na tela se o usuário venceu ou perdeu:


print ("Vou pensar em um número e você vai tentar advinhar qual número eu pensei ok?")
print ("Então vamos começar...")
print ('-=-' * 20)
from random import randint
computador = randint(0, 5) #Fazer o computador pensar
numero = int(input("Ok, já pensei... Que número você acha que eu pensei? "))
print ('-=-' * 20)

if numero == computador:
    print('Parabéns, você acertou')
else:
    print ('Que pena, tente novamente')


    #OBRIGADO!
#FIQUE A CONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO!
