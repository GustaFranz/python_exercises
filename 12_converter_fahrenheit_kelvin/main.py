#CONVERTER TEMPERATURA DE FAHRENHEIT PARA KELVIN
#Através das operações matemáticas básicas, elaborar um programa que converte temperatura Fahrenheit em Kelvin

#A conversão de temperatura é uma tarefa comum em diversas áreas, como ciências, engenharia, meteorologia e até no cotidiano.
#Um código que realiza essas conversões (entre Celsius, Fahrenheit e Kelvin) é útil para garantir precisão em cálculos, análises de dados e comunicação de resultados.
#Por exemplo, cientistas que trabalham em pesquisas internacionais podem precisar converter dados entre escalas diferentes dependendo do padrão adotado. 
#Da mesma forma, profissionais da área de climatologia ou estudantes podem usar esse tipo de programa para interpretar medições realizadas em diferentes regiões ou contextos.
#Ter um programa automatizado para essa conversão não só economiza tempo, mas também minimiza erros, 
#o que é essencial em aplicações onde a precisão é crítica, como na engenharia de processos industriais ou no planejamento de projetos térmicos.

#Solicita ao usuário a temperatura em graus Fahrenheit
ahrenheit = float(input("Digite a temperatura em graus Fahrenheit: "))

#Converte a temperatura para Kelvin
kelvin = ((fahrenheit - 32) / 1.8) + 273.15

#Exibe o resultado
print(f"A temperatura em Kelvin é {kelvin} K.")
