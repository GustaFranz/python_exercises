#CALCULANDO A CAPACIDADE DE UM RECIPIENTE, A PARTIR DA LARGURA, ALTURA E COMPRIMENTO.
# Solicita ao usuário a largura, altura e comprimento do recipiente em metros e responde qual a capacidade, em litros do recipiente

#Este código é uma ferramenta essencial para o cálculo do volume de recipientes retangulares, como caixas d'água, piscinas, tanques e outros reservatórios. 
#Saber a capacidade de armazenamento de água de um recipiente é fundamental em várias áreas, especialmente na engenharia civil e na construção, 
#onde o planejamento de sistemas de abastecimento e armazenamento de água deve ser preciso e eficiente.

#Usa-se primeiro o cálculo do volume em metros cúbicos, multiplicando-se as três medidas do recipiente (piscina, caixa d'água...)
#Em seguida, transforma esse volume de m3 para litros. 

recipiente = input("qual é o recipiente que você quer medir? ")
largura = float(input("Digite a largura da {} (em metros): ".format(recipiente)))
altura = float(input("Digite a altura da {} (em metros): ".format(recipiente)))
comprimento = float(input("Digite o comprimento da {} (em metros): ".format(recipiente)))

# Calcula o volume em metros cúbicos
volume_m3 = largura * altura * comprimento

# Converte o volume de metros cúbicos para litros (1 m³ = 1000 litros)
volume_litros = volume_m3 * 1000

# Exibe a quantidade de litros que o recipiente pode suportar
print("O volume da {} é {} litros.".format(recipiente, volume_litros))


#Conversão de Unidades de Medida
#Este código tem como objetivo converter um valor fornecido pelo usuário, em metros (m), para outras unidades de comprimento. As unidades de medida envolvidas na conversão são:

#Quilômetro (km), Hectômetro (hm), Decâmetro (dam), Decímetro (dm), Centímetro (cm), Milímetro (mm), 
#A conversão entre essas unidades é feita de forma simples, aplicando a lógica de multiplicação e divisão, com base na relação entre as unidades de medida no Sistema Internacional (SI).


#Obrigado por vir aqui. 
#Fique à vontade para comentar e contribuir com minha trilha de aprendizado!
