#Sorteio de um Aluno para Apagar o Quadro
#Este programa auxilia professores no sorteio aleatório de um aluno para apagar o quadro. 
Ele garante imparcialidade e pode ser aplicado em diversas situações de sorteio no dia a dia.


#Exercício: Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

import random
# s = students
s1 = ('Mark')
s2 = ('Danny')
s3 = ('John')
s4 = ('Alanis')
s5 = ('Angelina')

lista = [s1, s2, s3, s4, s5]
escolhido = random.choice(lista)
#essa função choice seleciona aleatoriamente um dos itens da lista
print ('O aluno escolhido foi', escolhido)



#Obrigado por dar uma olhada nos meus exercícios.
#Se tiver algo a contribuir com minha jornada de aprendizado fique a vontade!
