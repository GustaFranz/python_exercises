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

## Passo a passo

1. Crie a lista `matriculas = [101, 205, 308, 308, 412, 308, 519]`.
2. Defina `buscar_indice(lista, alvo, indice=0)` — o parametro `indice` com default `0` marca a posicao atual da busca:
   - caso base 1 (fim da lista): `if indice >= len(lista): return -1` — percorreu tudo e nao achou;
   - caso base 2 (achou): `if lista[indice] == alvo: return indice` — como avancamos da esquerda para a direita, esse e o indice da PRIMEIRA ocorrencia;
   - caso recursivo: `return buscar_indice(lista, alvo, indice + 1)` — avanca uma posicao.
3. Defina `contar_ocorrencias(lista, alvo, indice=0)`:
   - caso base: `if indice >= len(lista): return 0` — fim da lista, nada mais a contar;
   - calcule `achou = 1 if lista[indice] == alvo else 0` (a posicao atual vale 1 ou 0);
   - caso recursivo: `return achou + contar_ocorrencias(lista, alvo, indice + 1)` — soma a posicao atual com a contagem do resto.
4. Nao use `for` nem `while` dentro das duas funcoes.
5. No corpo principal, teste com alvo `308` e alvo `999` e exiba os 4 resultados formatados (esperado: indice 2 / contagem 3 e indice -1 / contagem 0).

## Como executar

```bash
cd "67_recursao_busca_linear"
python main.py
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

```python
# Export legado com matriculas duplicadas
matriculas = [101, 205, 308, 308, 412, 308, 519]


def buscar_indice(lista, alvo, indice=0):
    # Caso base 1: passou do fim da lista sem encontrar -> -1
    if indice >= len(lista):
        return -1

    # Caso base 2: achou o alvo na posicao atual
    # Como andamos da esquerda para a direita, e a primeira ocorrencia
    if lista[indice] == alvo:
        return indice

    # Caso recursivo: tenta de novo na proxima posicao
    return buscar_indice(lista, alvo, indice + 1)


def contar_ocorrencias(lista, alvo, indice=0):
    # Caso base: fim da lista, nao ha mais nada para contar
    if indice >= len(lista):
        return 0

    # A posicao atual contribui com 1 (se for o alvo) ou 0
    achou = 1 if lista[indice] == alvo else 0

    # Soma a contribuicao atual com a contagem do restante da lista
    return achou + contar_ocorrencias(lista, alvo, indice + 1)


# Testes com alvo existente (duplicado) e alvo inexistente
for alvo in [308, 999]:
    print(f"buscar_indice(matriculas, {alvo}) = {buscar_indice(matriculas, alvo)}")
    print(f"contar_ocorrencias(matriculas, {alvo}) = {contar_ocorrencias(matriculas, alvo)}")
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

```python
"""Busca e contagem recursivas em lista de matriculas.

Em producao, um dev usaria os recursos prontos da linguagem:
    lista.index(alvo)   -> indice da primeira ocorrencia (ValueError se nao existir)
    lista.count(alvo)   -> total de ocorrencias
As versoes recursivas abaixo treinam o raciocinio de reducao do problema.
"""


def buscar_indice(lista: list[int], alvo: int, indice: int = 0) -> int:
    """Retorna o indice da primeira ocorrencia de alvo, ou -1 se ausente."""
    # Guard clause / caso base: esgotou a lista
    if indice >= len(lista):
        return -1

    # Encontrou: devolve a posicao atual (primeira ocorrencia garantida)
    if lista[indice] == alvo:
        return indice

    # Reduz o problema: mesma busca comecando uma posicao a frente
    return buscar_indice(lista, alvo, indice + 1)


def contar_ocorrencias(lista: list[int], alvo: int, indice: int = 0) -> int:
    """Retorna quantas vezes alvo aparece na lista."""
    # Caso base: fim da lista encerra a soma
    if indice >= len(lista):
        return 0

    # bool vira int em soma: True == 1, False == 0
    achou = int(lista[indice] == alvo)
    return achou + contar_ocorrencias(lista, alvo, indice + 1)


def main() -> None:
    matriculas = [101, 205, 308, 308, 412, 308, 519]

    for alvo in (308, 999):
        indice = buscar_indice(matriculas, alvo)
        total = contar_ocorrencias(matriculas, alvo)
        print(f"Matricula {alvo}: primeiro indice = {indice}, ocorrencias = {total}")


if __name__ == "__main__":
    main()
```

</details>
