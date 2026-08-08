# 140 - Introducao a funcao geradora

## Objetivo

Conhecer funcoes geradoras com `yield` e entender iteracao preguicosa (lazy).

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | StreamData Escolar |
| **Setor** | Tecnologia / dados |
| **Solicitacao** | Gerar sequencia de eventos de acesso sem carregar tudo na memoria. |

## Visao do bloco (exercicios 140 a 143)

Topico **Funcoes geradoras**: produzir valores sob demanda com `yield`.

| # | Nivel | Foco |
|---|-------|------|
| 140 | Leve | Introducao: yield e iteracao |
| 141 | Leve | Gerador de lotes (chunks) |
| 142 | Ponte | Filtrar registros com gerador |
| 143 | Entrevista | Pipeline de relatorio com geradores |

## Enunciado

Implemente `gerar_eventos(quantidade)` que:
- recebe quantidade de eventos a produzir;
- usa `yield` para entregar strings `"evento_1"`, `"evento_2"`, ...;
- nao usa lista intermediaria para armazenar todos os eventos.

No `main`:
1) Consuma o gerador com loop `for` e exiba os 5 primeiros eventos.
2) Crie outro gerador com 3 eventos e converta com `list()` para comparar abordagens.
3) Exiba quantos eventos foram consumidos em cada caso.

## Como executar

```bash
cd "140_introducao_funcao_geradora"
python main.py
```
