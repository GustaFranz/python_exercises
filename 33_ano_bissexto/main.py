#Ano Bissexto: Sim ou Não?
#Aqui, trabalhamos com divisibilidade e regras lógicas para determinar se um ano é bissexto. 
Esse conhecimento é útil para validar calendários e sistemas de datas.


# Desenvolva um programa que leia um ano qualquer e mostre se ele é bissexto

print ('Você sabe o que é um ano bissexto?')
print('Um ano bissexto é um ano que tem um dia a mais. Em fevereiro temos normalmente 29 dias, mas nos anos bissextos esse mês tem 30 dias.')
print('~~'*60)
ano = int(input('Digite um ano qualquer e vamos descobrir juntos se esse é um ano bissexto: '))
print('~~'*60)
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print ('Sim, o ano {} é um ano bissexto'.format(ano))
else:
    print ('Esse ano não é bissexto, tente descobrir outros anos.')


    #OBRIGADO!
#FIQUE A CONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO!
