# AVALIAR SE OS CRROS PODEM PASSAR DE ACORDO COM O PESO DO VEÍCULO.
#Elaborar um programa que pergunta o peso do veículo.
#Se esse peso for abaixo de 0.9 kg, esse veículo é muito leve e não pode passar
#Se esse peso for acima de 1.8 kg, esse veículo é pesado demais para passar.
#Apresentar a informação do peso desse veículo para o usuário e informar se o carro pode passar.
#Se não puder avisar para fazer o retorno.


peso = float(input("Qual é o peso do seu veículo? "))
print ("seu veículo possui", peso, "kg")
if  peso >= 0.9 and peso <= 1.8:
    print ("Acesso de veículo permitido")
elif peso < 0.9:
    print ("Veículo abaixo do peso permitido. Faça o retorno.")
elif peso > 1.8:
    print ("veículo com peso acima do perimito. Faça o retorno.")


#Obrigado por vir aqui visualizar meus exercícios.
#Fique a vontade para sugerir melhorias no meu aprendizado!
