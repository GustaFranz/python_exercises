#Analisador de Textos
#Essa atividade ensina a manipular strings em Python. O programa trabalha com formatação de texto, contagem de caracteres e extração de partes específicas de uma string. 
#Essas habilidades são fundamentais para o processamento de dados textuais, como nomes, mensagens e arquivos.

# Crie um programa que leia o nome completo de uma pessoa e mostre:
#o nome com todas as letras maiúsculas.
#o nome com todas as letras minúsculas.
# quantas letras tem sem considerar os espaços.
# quantas letras tem o primeiro nome

#OBSERVAÇÃO: Coloquei tudo como comentário porque há dois códigos aqui (2 formas de execução).

# PRIMEIRA FORMA:

#nome = input('Qual é o seu nome completo? ')
#maiuscula = nome.upper()
#minuscula = nome.lower()
#sem_espacos = nome.replace(' ', '')
#primeiro_nome = nome.split()

#print(maiuscula)
#print(minuscula)
#print('A quantidade de letras de seu nome é ', len(sem_espacos))
#separa = nome.split()
#print ('Seu primeiro nome é {} e possui {} letras'.format(separa[0], len(separa[0])))

# SEGUNDA FORMA

#nome = str(input('Qual é o seu nome completo? ')).strip()
#maiuscula = nome.upper()
#minuscula = nome.lower()

#print ('Seu nome apenas com letras maiúsculas é {}'.format(nome.upper()))
#print ('Seu nome apenas com letras minúsculas é {}'.format(nome.lower()))
#print ('A quantidade de letras de seu nome é {}'.format(len(nome) - nome.count(' ')))
#print ('Seu primeiro nome tem {} letras'.format(nome.find(' ')))


#Obrigado por dar uma olhada nos meus códigos.
#Fique a vontade para contribuir com a minha jornada de aprendizado!
