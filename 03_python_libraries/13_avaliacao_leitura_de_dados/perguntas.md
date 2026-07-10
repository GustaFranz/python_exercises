# Avaliacao - Leitura de dados (Fase 1) - Perguntas

> Responda antes de abrir gabarito.md

## Pergunta 1

Explique o que `Path(__file__).resolve().parent` representa, quando o projeto de boletim usa `.parent.parent`, e por que isso e preferivel a um caminho fixo como `C:/Users/nome/projeto`.

---

## Pergunta 2

Por que `pd.concat(tabelas, ignore_index=True)` e necessario ao juntar varios CSVs? O que aconteceria sem `ignore_index=True`?

---

## Pergunta 3

Qual a diferenca entre formato largo e formato longo? Por que o projeto de boletim usa `melt` antes do merge?

---

## Pergunta 4

O que acontece se voce passar `sheet_name='Notas'` mas a aba real se chama `'Notas das Provas'`?

---

## Pergunta 5

Descreva o fluxo completo de extracao de tabela de um PDF com pdfplumber ate virar DataFrame.

---

## Pergunta 6

Por que e importante renomear `'Turma'` para `'turma'` antes de fazer merge com outras fontes?

---

## Pergunta 7

Em que situacao faz sentido lancar `raise FileNotFoundError(...)` em vez de retornar um DataFrame vazio?

---

## Pergunta 8 (leitura de codigo)

O codigo abaixo tem um erro. Identifique e explique:
```python
tabela = pd.read_csv('simulado.csv')  # formato largo
provas = pd.read_csv('provas.csv')    # formato longo
resultado = tabela.merge(provas, on='disciplina')
```

---
