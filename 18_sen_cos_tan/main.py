#Cálculo de Seno, Cosseno e Tangente de um Ângulo
#O programa recebe um ângulo em graus e exibe seus valores de seno, cosseno e tangente. 
Isso é essencial para cálculos trigonométricos aplicados na navegação, construção e análise de ondas.

# Faça um programa que leia um angulo qualquer e mostre na tela o valor do seno,
# cosseno a tangente dessa ângulo.

from math import sin, cos, tan, radians
angle = float(input ('What is the value of the angle? ' ))
angle_radians = radians(angle)
print ('the sine of you angle is {:.2f}'.format(sin(angle_radians)))
print('the cosine of your angle is {:.2f}'.format (cos (angle_radians)))
print('the tangente of your angle is {:.2f}'.format (tan(angle_radians)))



#Obrigado por dar uma olhada nos meus exercícios.
#Se tiver algo a contribuir com minha jornada de aprendizado fique a vontade!
