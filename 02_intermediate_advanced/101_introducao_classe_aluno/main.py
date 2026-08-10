# DEMANDA
# Empresa: Edutech Brasil
# Setor: Educacao / cadastro
# Solicitacao: Modelar cadastro de aluno em classe reutilizavel no sistema escolar.

# EXERCICIO 101 - Introducao a classe Aluno (contexto corporativo)
#
# VISAO DO BLOCO — Classe simples (exercicios 101 a 105)
# Este bloco treina:
## 101 — Introducao: classe Aluno com __str__
## 102 — Metodo aprovar() em Aluno
## 103 — Classe Produto com controle de estoque
## 104 — Classe Pedido com itens e total
## 105 — Simulador de caixa com Caixa + ItemVenda
#
# Conceitos basicos:
## class Nome: com __init__(self, ...) e self.atributo
## __str__(self) define impressao amigavel com print(obj)
## Metodos alteram estado do objeto (self)
## POO organiza dados e comportamento juntos
#
# Crie classe Aluno com:
## __init__(self, nome, turma, nota)
## __str__(self) retornando "Aluno: {nome} | Turma: {turma} | Nota: {nota}"
# Crie 2 instancias e exiba com print().
#
# ORIENTACOES
## class Aluno:
##     def __init__(self, nome, turma, nota):
##         self.nome = nome
## Use __str__ para representacao legivel (nao __repr__ neste exercicio).

# --- Implemente sua solucao abaixo ---
#
# =============================================================================
# # RESOLUCAO DO EXERCICIO
# =============================================================================

class Aluno:
    def __init__(self, nome: str, turma: str, nota: float):
        self.nome = nome
        self.turma = turma
        self.nota = nota

    def __str__(self):
        return f'Aluno: {self.nome}  |  Turma: {self.turma}  |  Nota: {self.nota}'

aluno1 = Aluno("Arthur", "8º ano", 8.5)
aluno2 = Aluno("Davi", "6º ano", 9.5)
print()
print(aluno1)
print()
print(aluno2)
print()
# =============================================================================
# # APRENDIZADOS E CONSOLIDACAO DE CONCEITOS
# =============================================================================
#
# class Aluno define o molde; cada instancia guarda seus proprios dados
# __init__(self, ...) inicializa atributos com self.nome, self.turma, self.nota
# self liga o metodo ao objeto criado (aluno1, aluno2)
# __str__ retorna texto legivel; print(aluno1) chama __str__ automaticamente
# Instanciar e criar objetos: Aluno("Arthur", "8º ano", 8.5)
# POO junta dados e comportamento no mesmo lugar (cadastro reutilizavel)
#
# OBRIGADO!
# FIQUE A VONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO
