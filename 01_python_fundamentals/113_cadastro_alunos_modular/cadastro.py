

def cadastrar_aluno(alunos, nome, idade, matricula):
    """
    Cadastra um novo aluno na lista de alunos.

    Args:
        alunos (list): Lista de alunos.
        nome (str): Nome do aluno.
        idade (int): Idade do aluno.
        matricula (str): Matrícula do aluno.

    Returns:
        None
    """
    aluno = {
        'nome': nome,
        'idade': idade,
        'matricula': matricula
    }
    alunos.append(aluno)

