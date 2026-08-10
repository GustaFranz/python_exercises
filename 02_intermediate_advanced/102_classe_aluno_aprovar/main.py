# DEMANDA
# Empresa: Secretaria Digital
# Setor: Educacao / secretaria
# Solicitacao: Marcar alunos aprovados automaticamente apos fechamento de notas.

# EXERCICIO 102 - Classe Aluno: metodo aprovar (contexto corporativo)
#
# Classe Aluno:
## __init__(self, nome, nota): self.aprovado = False
## aprovar(self): se nota >= 7.0: self.aprovado = True
## __str__: inclui status Aprovado/Reprovado
# Teste aluno com nota 8.0 (aprovado) e 5.5 (reprovado).
#
# ORIENTACOES
## Metodo aprovar altera self.aprovado conforme regra.
## Chame aprovar() apos criar instancia e exiba resultado.

# --- Implemente sua solucao abaixo ---
#
# =============================================================================
# # RESOLUCAO DO EXERCICIO
# =============================================================================

class Aluno:

    def __init__(self, nome: str, nota: float):
        self.nome = nome
        self.nota = nota

    @property
    def status(self) -> str:
        # Retorna o texto do status diretamente com base na nota
        return 'Aprovado' if self.nota >= 7.0 else 'Reprovado'

    def __str__(self):
        # Acessa a property self.status dentro da f-string
        return f'Aluno: {self.nome}  |  Nota: {self.nota}  |  Status: {self.status}'


aluno1 = Aluno('Juliano', 8.5)
aluno2 = Aluno('Maressa', 6.5)

print()
print(aluno1)
print()
print(aluno2)
print()

# =============================================================================
# # APRENDIZADOS E CONSOLIDACAO DE CONCEITOS
# =============================================================================
#
# Metodos da classe alteram ou expoem o estado do objeto via self
# Regra de negocio: nota >= 7.0 define Aprovado; abaixo disso, Reprovado
# Expressao condicional (ternaria) resume a logica em uma linha
# __str__ monta a saida final usando os atributos do aluno
# Atraves de pesquisas aprendi @property e achei interessante ja utiliza-lo nesta fase de estudos
# @property transforma metodo em atributo de leitura: self.status sem parenteses
# status e calculado a partir da nota, sem precisar guardar self.aprovado separado
# Encaixou bem no __str__ e deixou a classe mais enxuta e legivel
#
# OBRIGADO!
# FIQUE A VONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO
