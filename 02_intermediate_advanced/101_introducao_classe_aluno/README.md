# 101 - Introducao a classe Aluno

## Objetivo

Criar classe Aluno com atributos e metodo __str__.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | Edutech Brasil |
| **Setor** | Educacao / cadastro |
| **Solicitacao** | Modelar cadastro de aluno em classe reutilizavel no sistema escolar. |

## Visao do bloco (exercicios 101 a 105)

Topico **Classe simples**: objetos com atributos, metodos e __str__.

| # | Foco |
|---|------|
| 101 | Introducao + classe Aluno |
| 102 | Metodo aprovar() |
| 103 | Classe Produto com estoque |
| 104 | Classe Pedido: itens, total, desconto e remocao |
| 105 | Simulador de caixa com 2 classes |

## Enunciado

Crie a classe `Aluno` com:

- `__init__(self, nome, turma, nota)` — armazena os atributos em `self`
- `__str__(self)` — retorna `"Aluno: {nome} | Turma: {turma} | Nota: {nota}"`

No `main`:

1) Instancie 2 alunos com dados diferentes (ex.: Ana/7A/8.5 e Bruno/8B/6.0).
2) Exiba cada instancia com `print()`.

Exemplo de saida:

```
Aluno: Ana | Turma: 7A | Nota: 8.5
Aluno: Bruno | Turma: 8B | Nota: 6.0
```

## Como executar

```bash
cd "101_introducao_classe_aluno"
python main.py
```
