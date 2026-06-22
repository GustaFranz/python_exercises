# Cálculo do IMC (Índice de Massa Corporal)
# O programa recebe peso e altura do usuário e calcula seu IMC, indicando se está abaixo, dentro ou acima do peso ideal. 
# Ferramenta útil para controle da saúde e avaliação nutricional.


# Exercício 1: Cálculo de IMC(Índice de Massa Corporal)
# Enunciado: Crie um programa que leia o peso
# e a altura de uma pessoa e calcule o IMC(Índice de Massa Corporal) com a seguinte fórmula:
# 𝐼𝑀𝐶 = massa/altura**2
# 
# O programa deve:
# Ler o peso e a altura da pessoa.
# Calcular o IMC.
# Exibir o IMC com 2 casas decimais.
# Classificar a pessoa de acordo com o IMC:
# Abaixo do peso: IMC abaixo de 18,5
# Peso normal: IMC entre 18, 5 e 24,9
# Sobrepeso: IMC entre 25 e 29,9
# Obesidade: IMC acima de 30


massa = float(input('Qual é a sua massa em kg? '))
altura = float(input('Qual é a sua altura em m? '))
imc = float(massa/(altura**2))
print('Seu Índice de Massa Corporal é {:.2f}'.format(imc))

if imc < 18.5:
     print('Você está abaixo da sua massa corporal ideal')
elif 18.5 <= imc <= 24.9:
     print ('Sua massa corporal está dentro dos parâmetros normais. Parabéns!')
elif 24.9 < imc <= 29.9:
     print ('SOBREPESO - Você está acima da sua massa corporal ideal')
else:
     print ('OBESIDADE - Você está muito acima da sua massa corporal ideal')



# Obrigado por dar uma olhada nos meus exercícios.
# Se tiver algo a contribuir com minha jornada de aprendizado fique a vontade!

