# Retorno em 30/07 — comparar com a versao do inicio dos estudos.

import random


def ler_alunos(quantidade: int = 4) -> list[str]:
    """Le nomes dos alunos e ignora entradas vazias."""
    alunos: list[str] = []
    for i in range(1, quantidade + 1):
        nome = input(f"Nome do aluno {i}: ").strip()
        if nome:
            alunos.append(nome)
    if not alunos:
        raise ValueError("Nenhum aluno cadastrado para o sorteio.")
    return alunos


def sortear_aluno(alunos: list[str]) -> str:
    """Retorna um aluno escolhido aleatoriamente."""
    return random.choice(alunos)


# =============================================================================
# RESOLUCAO
# =============================================================================

try:
    turma = ler_alunos()
    escolhido = sortear_aluno(turma)
    print(f"O aluno escolhido foi {escolhido}")
except ValueError as erro:
    print(f"Erro: {erro}")
