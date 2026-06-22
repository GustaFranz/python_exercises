#Primeiro e Último Nome
#Esse exercício reforça a extração de partes de um texto. 
#Ele divide o nome completo e exibe apenas o primeiro e o último nome, uma habilidade útil em cadastros, autenticações e manipulação de dados de usuários.


Faça um programa que leia o nome completo de uma pessoa mostrando
#em seguida o primeiro e o último nome separadamente
#EX> Ana Maria de Souza
# Primeiro: Ana
# Último: Souza

nome = str(input('Digite o seu nome completo: ')).strip()
n = nome.split()
print ('seu primeiro nome é {} e seu último nome é {}'.format(n[0], n[len(n)-1]))

#Explicação:
#usei o .strip no começo para evitar possível erro do usuário em deixar espaços excedentes
#criei uma lista com a função .split
#na lista, 0 corresponde ao primeiro nome
#para o último nome, utilizei a contagem total de itens na lista menos 1, que dá o número do item que corresponde ao último nome.


#Obrigado!
#Fique a vontade para contribuir com o meu aprendizado!
