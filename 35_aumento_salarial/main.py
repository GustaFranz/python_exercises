#Cálculo de Aumento Salarial
#Um exemplo prático do uso de condições para definir reajustes salariais. 
Ele ajuda a entender como sistemas de pagamento e benefícios são calculados automaticamente.


# Desenvolva um programa que pergunte o salário de um funcionpario e calcule o valor
# do seu aumento.
# Para salários superiores a R$1.250,00, calcule um aumento de 10%
# Para salários inferiores ou igual, calcule aumento de 15%.

print('Parabéns colaborador, você foi contemplado em nosso programa especial de desenvolvimento de carreira')
print('Vamos agora calcular o seu aumento salarial')
salario = float(input('Qual é o valor em reais (R$) do seu salário atual? '))

s10 = float(salario + (salario * 0.1))
s15 = float(salario + (salario * 0.15))

if salario <= 1250:
    print ('Seu novo salário será R$ {}'.format(s15))
else:
    print ('Seu novo salário será R$ {}'.format(s10))

    #OBRIGADO!
#FIQUE A CONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO!
