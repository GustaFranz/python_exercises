# 118 - Refatoracao: extrair funcoes

## Objetivo

Extrair funcoes de script procedural repetitivo.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | CalcEscolar |
| **Setor** | Educacao / matematica |
| **Solicitacao** | Eliminar duplicacao no calculo de medias por turma. |

## Enunciado

Codigo repetitivo a refatorar:

```python
notas_7b = [8, 7, 9]
s1 = 0
for n in notas_7b:
    s1 += n
media_7b = s1 / len(notas_7b)

notas_8a = [6, 8, 7, 9]
s2 = 0
for n in notas_8a:
    s2 += n
media_8a = s2 / len(notas_8a)
```

Tarefas:

1) Extraia `calcular_media(notas) -> float` eliminando a duplicacao.
2) Use a funcao para calcular a media das turmas **7B** e **8A**.
3) Exiba: `Media 7B: ...` e `Media 8A: ...`.

## Como executar

```bash
cd "118_refatoracao_extrair_funcoes"
python main.py
```
