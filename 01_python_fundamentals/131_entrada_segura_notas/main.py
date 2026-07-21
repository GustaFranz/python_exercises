# EXERCICIO 131 - Entrada segura de notas (contexto educacional)
#
# ENUNCIADO
# Crie um sistema que receba notas de alunos e calcule a media da turma.
# O programa deve estar protegido contra entradas invalidas.
# O sistema deve:
## solicitar 5 notas do usuario;
## calcular a media final;
## impedir que o programa quebre com entradas invalidas (texto ou valores fora do padrao).
#
# ORIENTACOES
## Use try/except.
## Trate ValueError.
## Valide se a nota esta entre 0 e 10.
## Peca nova entrada em caso de erro.
#
# --- Implemente sua solucao abaixo ---
#
# =============================================================================
# # RESOLUCAO DO EXERCICIO
# =============================================================================
# import easyansi
# easyansi.activate()

class NomeObrigatorioError(Exception):
    '''Lançada quando o nome do aluno não é fornecido.'''

class NotaInvalidaError(Exception):
    '''Lançada quando a nota do aluno não está entre 0 e 10.'''


def calcular_media(notas):
    return sum(notas) / len(notas)

def validar_nome():
    nome = input("Digite o nome do aluno: ")
    if nome.strip() == "":
        raise NomeObrigatorioError("O nome não pode estar vazio")
    return nome
    
def validar_nota(numero_nota):
    entrada = input(f"Digite a nota do aluno: ")
    if entrada.strip() == "":
        raise NotaInvalidaError("Nota invalida. Por favor, digite uma nota entre 0 e 10.")

    entrada_corrigida = entrada.replace(",", ".")
    nota = float(entrada_corrigida)

    if nota < 0 or nota > 10:
        raise NotaInvalidaError("Nota invalida. Por favor, digite uma nota entre 0 e 10.")

    return nota

while True:
    try:
        nome_aluno = validar_nome()
        break
    except NomeObrigatorioError as e:
        print(f'Erro: {e}\n')

notas_aluno = []

while len(notas_aluno) < 3:
    try:
        numero_nota = len(notas_aluno) + 1
        nota_valida = validar_nota(numero_nota)
        notas_aluno.append(nota_valida)


    except NotaInvalidaError as e:
        print(f"Erro: {e}")

media = calcular_media(notas_aluno)


print(f'{nome_aluno} | Notas: {notas_aluno} | Média: {media:.2f}')


# =============================================================================
# # APRENDIZADOS E CONSOLIDACAO DE CONCEITOS
# =============================================================================
#
# Tive certa dificuldade para concluir este exercicio, principalmente na organizacao
# das validacoes sem deixar o programa quebrar
# Gostei de conhecer e aplicar o uso de classes para criar excecoes customizadas
# NomeObrigatorioError e NotaInvalidaError herdam de Exception e deixam o erro mais claro
# try/except com while True e break permite pedir nova entrada ate o dado ficar valido
# replace(',', '.') ajuda a aceitar nota digitada com virgula antes do float()
# Funcoes validar_nome() e validar_nota() separam regras e facilitam reler o codigo
# Animado em juntar classes, excecoes e loop de validacao no mesmo fluxo
#
# OBRIGADO!
# FIQUE A VONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO
