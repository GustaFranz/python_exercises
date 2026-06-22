#Analisador de Frase
#Aqui, o foco está na contagem e localização de caracteres dentro de um texto. 
O programa mostra quantas vezes a letra "A" aparece e em quais posições, um conceito fundamental para análise textual e processamento de linguagem natural.

Faça um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra a
# Em que posição ela aparece pela primeira vez
# em que posição ela aparece pela última vez

frase = str(input('Escreva uma frase: ')).upper().strip()
print ('a letra "a" apareceu na sua frase {} vezes'.format(frase.count('A')))
print ('a letra "a" apareceu na sua frase pela primeira vez na posição {} do texto'.format(frase.find('A')))
print ('a letra "a" apareceu na sua frase pela última vez na posição {} do texto'.format(frase.rfind('A')))


#OBRIGADO!
#FIQUE A VOONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO!
