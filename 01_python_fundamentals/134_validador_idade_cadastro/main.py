# EXERCICIO 134 - Validador de idade para cadastro (contexto educacional)
#
# ENUNCIADO
# Crie um sistema de cadastro onde o usuario informa sua idade.
# O sistema deve garantir que apenas valores validos sejam aceitos.
# O sistema deve:
## solicitar idade do usuario;
## aceitar apenas numeros inteiros positivos;
## impedir que o programa encerre com erro.
#
# ORIENTACOES
## Use try/except.
## Trate ValueError.
## Valide idade > 0.
## Peca nova entrada em caso de erro.
#
# --- Implemente sua solucao abaixo ---
#
# =============================================================================
# # RESOLUCAO DO EXERCICIO
# =============================================================================

class NotaInvalidaError(Exception):
    """lançado quando a nota for inválida"""


def validar_idade(entrada):

    if entrada.strip() == "":
        raise NotaInvalidaError("A entrada não pode estar vazia.")

    try:
        idade = int(entrada)

    except ValueError:
        raise NotaInvalidaError("Digite apenas números.")

    if idade <= 0:
        raise NotaInvalidaError("O valor precisa ser maior que zero.")
    
    return idade

while True:
    entrada = input("Digite a sua idade: ")
    if entrada.lower() == 'sair':
        break

    try:
        sua_idade = validar_idade(entrada)
        print(f"Idade salva com sucesso: {sua_idade}")
        break

    except NotaInvalidaError as e:
        print(f"Erro: {e}\n")





# =============================================================================
# # APRENDIZADOS E CONSOLIDACAO DE CONCEITOS
# =============================================================================
#
# Tive certa dificuldade em separar validacao de idade da leitura do input sem repetir codigo
# Reutilizei excecao customizada do exercicio anterior e adaptei para validar idade no cadastro
# validar_idade() concentra as regras: entrada vazia, texto invalido e valor menor ou igual a zero
# ValueError dentro do try trata quando int() nao consegue converter o texto digitado
# raise NotaInvalidaError transforma erros comuns em mensagens mais claras para o usuario
# entrada.strip() == "" evita aceitar espacos vazios como se fossem um valor valido
# while True com break permite pedir nova idade ate o dado ficar correto ou digitar sair
# Animado em juntar excecao customizada, validacao e loop de entrada segura no cadastro
#
# OBRIGADO!
# FIQUE A VONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO
