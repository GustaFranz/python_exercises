#Controle de Velocidade
#Um programa essencial para simular sistemas de fiscalização de trânsito. 
Ele ensina a trabalhar com condições e cálculos simples, mostrando como automatizar verificações importantes do cotidiano.

# Escreva um programa que leia a velocidade de um carro
# se ele ultrapassar 80 km/h, mostre uma mensagem dizendo que ele foi multado:
# A multa vai custar R$7,00 por cada km a mais de velocidade

velocidade = float(input('Qual é a velocidade atual do seu veículo? '))
print (('-=-')*20)

multa = float((velocidade-80)*7)
if velocidade <= 80:
    print ('Sua velocidade atual é {} km/h. Continue tendo uma boa viagem.'.format(velocidade))
else:
    print ('MULTA: Você está acima da velocidade permitida. Sua multa é de R$ {} reais'.format(multa))


    #OBRIGADO!
#FIQUE A CONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO!
