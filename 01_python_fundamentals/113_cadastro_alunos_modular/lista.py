import easyansi
easyansi.activate()

def listar_alunos(alunos):
    """
    Lista todos os alunos cadastrados.

    Args:
        alunos (list): Lista de alunos.

    Returns:
        None
    """
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return

    print("\n//magenta/============/magenta LISTA DE ALUNOS: //magenta/============/magenta")
    for aluno in alunos:
        print(f"//green/Nome:/green //yellow/{aluno['nome']}/yellow, //green/Idade:/green //yellow/{aluno['idade']}/yellow, //green/Matrícula:/green //yellow/{aluno['matricula']}/yellow")