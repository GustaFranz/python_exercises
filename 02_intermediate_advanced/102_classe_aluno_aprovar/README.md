# 102 - Classe Aluno: metodo aprovar

## Objetivo

Adicionar metodo aprovar() que altera status do aluno.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | Secretaria Digital |
| **Setor** | Educacao / secretaria |
| **Solicitacao** | Marcar alunos aprovados automaticamente apos fechamento de notas. |

## Enunciado

Estenda a classe `Aluno` com:

- `__init__(self, nome, nota)` — define `self.aprovado = False`
- `aprovar(self)` — se `nota >= 7.0`, define `self.aprovado = True`
- `__str__(self)` — inclui status `"Aprovado"` ou `"Reprovado"`

Teste no `main`:

1) Aluno com nota **8.0** — chame `aprovar()` e exiba (deve ficar Aprovado).
2) Aluno com nota **5.5** — chame `aprovar()` e exiba (deve ficar Reprovado).

## Como executar

```bash
cd "102_classe_aluno_aprovar"
python main.py
```
