# Avaliacao - Merge triplo e modulos src - Perguntas

> Responda antes de abrir gabarito.md
> Consulte o projeto real: `src/consolidacao.py`, `main.py` e os leitores em `src/`.

---

## Parte A — Merge triplo (8 perguntas)

### Pergunta 1

Por que `consolidacao.py` faz **dois merges seguidos** (simulados+provas, depois +projetos) em vez de juntar as tres tabelas de uma vez so?

---

### Pergunta 2

Quais sao as **tres chaves** usadas em todos os merges (`on=[...]`)? Por que essas colunas e nao apenas `aluno`?

---

### Pergunta 3

Antes do merge, cada leitor chama uma funcao `transformar_*_para_longo()`. O que o **melt** garante para o merge funcionar?

---

### Pergunta 4

Depois do **primeiro** merge (simulados + provas), quais colunas de nota existem na tabela? E depois do **segundo** merge (+ projetos)?

---

### Pergunta 5

Todos os merges usam `how="inner"`. Se Ana Silva tem Matematica em simulados e Ciencias em provas, mas **nao** tem Ciencias em simulados, o que acontece com a linha de Ciencias apos o primeiro merge?

---

### Pergunta 6 (cenario hipotetico)

Bruno Costa aparece em simulados (Matematica) e provas (Matematica), mas **nao** tem registro de projeto para Matematica. O que acontece com Bruno apos o merge triplo completo?

---

### Pergunta 7

A coluna `nota_simulado` chega em escala **0-1** (ex: 0,9). Por que a formula multiplica por 10 **depois** do merge, e nao antes nos leitores?

---

### Pergunta 8

Descreva a ordem completa das operacoes em `consolidar_notas()` **depois** dos merges: da conversao de tipos ate o retorno da tabela.

---

## Parte B — Imports e modulos src (7 perguntas)

### Pergunta 9

Explique a linha do `main.py`:

```python
from src.consolidacao import consolidar_notas, salvar_relatorio_final
```

O que `src` representa e por que o import nao e `from consolidacao import ...`?

---

### Pergunta 10

Em `consolidacao.py`, os imports sao:

```python
from src.leitor_simulados import ler_simulados, transformar_simulados_para_longo
```

Por que um arquivo **dentro** de `src/` tambem usa o prefixo `src.` no import?

---

### Pergunta 11

Qual a diferenca pratica entre executar `python main.py` na raiz do projeto e executar `python src/consolidacao.py` diretamente?

---

### Pergunta 12

`boletins.py` importa `consolidar_notas` e chama essa funcao de novo dentro de `gerar_boletins()`. O `main.py` ja chama `consolidar_notas()` antes de `gerar_boletins()`. Por que o boletim **nao** recebe a tabela ja consolidada como parametro?

---

### Pergunta 13

Cada leitor (`leitor_simulados.py`, `leitor_provas.py`, `leitor_projetos.py`) expoe duas funcoes publicas: `ler_*()` e `transformar_*_para_longo()`. Qual o beneficio de separar **leitura** de **transformacao**?

---

### Pergunta 14

O bloco `if __name__ == "__main__":` aparece em varios modulos de `src/`. Para que serve quando voce testa um leitor isoladamente?

---

### Pergunta 15

Trace o fluxo de **dados** (nao apenas de execucao) desde o CSV de simulado ate uma linha do boletim HTML de Ana Silva em Matematica. Cite modulos e funcoes envolvidos.

---
