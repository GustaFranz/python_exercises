# 67 - Recursao: busca linear e contagem de ocorrencias

## Objetivo

Implementar busca recursiva em lista com duplicatas: indice da primeira ocorrencia e contagem total.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | Edutech Brasil |
| **Setor** | Educacao / plataforma |
| **Solicitacao** | Localizar matricula em export legado e contar quantas vezes ela aparece no backlog de registros. |

## Enunciado

- Use `matriculas = [101, 205, 308, 308, 412, 308, 519]` (lista com duplicatas).
- Implemente `buscar_indice(lista, alvo, indice=0)` recursiva:
  - retorna indice da **primeira** ocorrencia ou `-1` se nao existir.
- Implemente `contar_ocorrencias(lista, alvo, indice=0)` recursiva:
  - retorna quantas vezes `alvo` aparece na lista.
- Nao use `for`/`while` dentro dessas funcoes — apenas recursao.
- Teste com alvo `308` (indice 2, contagem 3) e alvo `999` (indice -1, contagem 0).

## Como executar

```bash
cd "67_recursao_busca_linear"
python main.py
```
