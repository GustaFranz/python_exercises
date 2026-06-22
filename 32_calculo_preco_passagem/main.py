#Cálculo de Passagem
#Este exercício ensina a estruturar condições para cálculos diferenciados, como preços progressivos. 
Esse conceito é aplicado em diversas áreas, como transporte e economia.


# Desenvolva um programa que pergunte a distância de uma viagem em km.
# Calcule o preço da passagem cobrando R$0,50 por km para viagens de até 200km
# e R$ 0,45 para viagens mais longas:


print ('Vamos calcular o preço da sua passagem.')
print (('-=-')*20)
viagem = float(input('A cidade que você quer ir está a quantos quilômetros de distância? '))
print (('-=-')*20)
viagem_curta = float(viagem * 0.50)
viagem_longa = float(viagem * 0.45)
if viagem <= 200:
    print ('O valor da sua viagem é de R$ {}'.format(viagem_curta))
else:
    print ('O valor da sua viagem é de R$ {}'.format(viagem_longa))
print (('~~~'*20))
print ('Obrigado por viajar conosco!')
print ('Dirija-se ao caixa para realizar o seu pagamento.')


#OBRIGADO!
#FIQUE A CONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO!
