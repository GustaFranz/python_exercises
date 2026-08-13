# DEMANDA
# Empresa: Edutech Brasil
# Setor: Educacao / cadastro
# Solicitacao: Unificar cadastro de pessoas com tipos especificos aluno e professor.

# EXERCICIO 107 - Introducao a heranca (contexto corporativo)
#
# VISAO DO BLOCO — Heranca simples (exercicios 107 a 111)
# Este bloco treina:
## 101 — Introducao: Pessoa -> Aluno / Professor
## 102 — Sobrescrever metodo da classe pai
## 103 — super() para reutilizar __init__ da pai
## 104 — Hierarquia de descontos por tipo
## 105 — Sistema RH com 3 classes relacionadas
#
# Conceitos basicos:
## class Filho(Pai): herda atributos e metodos
## super().__init__(...) chama construtor da classe pai
## Sobrescrever metodo: definir mesmo nome na filha
## "E um" (Aluno e uma Pessoa) — reutilizacao de codigo
#
# Classe Pessoa: __init__(self, nome, cpf); __str__ com nome e cpf
# Classe Aluno(Pessoa): adiciona turma; __str__ inclui turma
# Classe Professor(Pessoa): adiciona disciplina; __str__ inclui disciplina
# Crie 1 aluno e 1 professor e exiba com print().
#
# ORIENTACOES
## class Aluno(Pessoa): chame super().__init__(nome, cpf) no __init__
## Atributos especificos: self.turma, self.disciplina

# --- Implemente sua solucao abaixo ---
#
# =============================================================================
# # RESOLUCAO DO EXERCICIO
# =============================================================================

class Pessoa:

    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

    def __str__(self):
        return f'Pessoa: {self.nome}  |  CPF: {self.cpf}'


class Aluno(Pessoa):

    def __init__(self, nome, cpf, turma: str):
        super().__init__(nome, cpf)
        self.turma = turma

    def __str__(self):
        return f"Aluno: {self.nome} | CPF: {self.cpf} | Turma: {self.turma}" 


class Professor(Pessoa):

    def __init__(self, nome, cpf, disciplina: str):
        super().__init__(nome, cpf)
        self.disciplina = disciplina

    def __str__(self):
        return (f'Professor:{self.nome}  | '
                f'CPF: {self.cpf}  | '
                f'Disciplina: {self.disciplina}')

aluno_Ana = Aluno("Ana", "111", "7A")
aluno_Heitor = Aluno("Heitor", "222", "7A")
professor_Jeferson = Professor("Jeferson", "444", "40")

print(aluno_Ana)
print()
print(aluno_Heitor)
print()
print(professor_Jeferson)
print()


# =============================================================================
# # APRENDIZADOS E CONSOLIDACAO DE CONCEITOS
# =============================================================================
#
# class Filho(Pai): herda atributos e metodos da classe base
# Pessoa concentra o comum: nome e cpf (reutilizacao sem duplicar codigo)
# Aluno e Professor "sao" Pessoa — relacao "e um" (is-a)
# super().__init__(nome, cpf) chama o construtor da pai e inicializa o herdado
# Atributos especificos ficam na filha: self.turma, self.disciplina
# Sobrescrever __str__ na filha personaliza a impressao sem mudar a pai
# print(aluno) usa o __str__ da classe concreta (Aluno ou Professor)
# Heranca organiza tipos relacionados e evita repetir o mesmo __init__ base
#
# OBRIGADO!
# FIQUE A VONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO
