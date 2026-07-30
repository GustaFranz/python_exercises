# 72 - Closure: fabrica de relatorio por turma

## Objetivo

Criar geradores de relatorio via closure que capturam turma e professor e calculam estatisticas da lista de alunos.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | Secretaria Digital |
| **Setor** | Educacao / secretaria |
| **Solicitacao** | Padronizar relatorios de turma com cabecalho fixo e metricas (quantidade e media) para entrega ao coordenador. |

## Enunciado

- Implemente `criar_gerador_relatorio(turma, professor)`:
  - retorna funcao `gerar(lista_alunos)` (closure).
  - `lista_alunos` e lista de dicts `{nome, nota}`.
  - `gerar` retorna string formatada (nao precisa imprimir dentro da closure) com:
    - cabecalho: turma e professor capturados
    - quantidade de alunos
    - media das notas (1 casa decimal; 0 alunos -> media 0.0)
- Crie pelo menos 2 geradores (turmas diferentes) e teste com listas distintas.
- Exiba os relatorios retornados.

Exemplo de entrada:

```python
alunos_7a = [{"nome": "Ana", "nota": 7.5}, {"nome": "Pedro", "nota": 6.0}]
```

## Como executar

```bash
cd "72_closure_relatorio_turma"
python main.py
```
