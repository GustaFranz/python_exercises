# Verificação de Nome de Cidade

# Este exercício treina a busca e comparação de strings. Ele verifica se uma cidade começa com "SANTO", demonstrando como manipular textos de forma eficiente. 

# Esse tipo de operação é comum em sistemas de busca e categorização de dados.


# Crie um prograna que leia o nome de uma cidade

# e diga se ela começa ou não com o nome "SANTO"

# PRIMEIRA FORMA (mais simples)

# cidade = str(input('Digite o nome de uma cidade: '))
# a = cidade.find('Santo')
# if a == 0:
#     print ("A cidade começa com o nome Santo")
# else:
#     print ('A cidade não começa com o nome Santo')

# SEGUNDA FORMA (MELHORADA)

cidade = str(input('Digite o nome de uma cidade: ')).strip()
print (cidade[:5].upper() == 'SANTO')
# Parte do raciocínio que se SANTO é a palavra inicial e tem 5 letras podemos pedir de [:5] é santo
# converte tudo para maiúscula para facilitar


# OBRIGADO!
# FIQUE A VONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO!
