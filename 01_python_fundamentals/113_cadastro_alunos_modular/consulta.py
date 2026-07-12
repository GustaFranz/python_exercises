

def buscar_aluno(alunos, matricula):
    """
    Busca um aluno na lista de alunos pelo número de matrícula.

    Args:
        alunos (list): Lista de alunos.
        matricula (str): Número de matrícula do aluno a ser buscado.

    Returns:
        dict or None: Retorna o dicionário do aluno encontrado ou None se não encontrado.
    """
    for aluno in alunos:
        if aluno['matricula'] == matricula:
            return aluno
    return None