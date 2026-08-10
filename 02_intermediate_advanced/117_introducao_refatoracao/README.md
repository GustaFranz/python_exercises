# 117 - Introducao a refatoracao

## Objetivo

Identificar problemas em codigo monolitico e planejar separacao em funcoes.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | DevEscola Labs |
| **Setor** | Educacao / formacao dev |
| **Solicitacao** | Reorganizar script legado de notas antes de integrar ao sistema novo. |

## Visao do bloco (exercicios 117 a 121)

Topico **Refatoracao**: melhorar estrutura sem mudar comportamento.

| # | Foco |
|---|------|
| 117 | Introducao + identificar codigo monolitico |
| 118 | Extrair funcoes |
| 119 | Renomear variaveis confusas |
| 120 | Separar I/O, regra e apresentacao |
| 121 | Refatorar script longo (~70 linhas) em funcoes + menu |

## Enunciado

Estude o codigo monolitico abaixo (nao execute — refatore):

```python
notas = [7, 8, 5, 9, 6]
s = 0
for n in notas:
    s = s + n
m = s / len(notas)
if m >= 7:
    print("Turma aprovada com media", m)
else:
    print("Turma reprovada com media", m)
for n in notas:
    if n < 7:
        print("Recuperacao:", n)
```

Tarefas:

1) Em comentarios, liste **3 problemas** desse codigo (ex.: nomes confusos, tudo no fluxo principal).
2) Implemente as funcoes:
   - `calcular_media(notas) -> float`
   - `turma_aprovada(media, corte=7) -> bool`
   - `listar_recuperacao(notas, corte=7)` — imprime notas abaixo do corte
3) Monte `main()` limpo que reproduz **exatamente** o mesmo resultado do script original.

## Como executar

```bash
cd "117_introducao_refatoracao"
python main.py
```
