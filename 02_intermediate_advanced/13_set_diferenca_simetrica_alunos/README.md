# 13 - Set: diferenca simetrica

## Objetivo

Comparar duas listas e achar exclusivos de cada lado.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | Clinica BemViver |
| **Setor** | Saude ocupacional escolar |
| **Solicitacao** | Comparar listas de vacinacao entre duas unidades. |

## Enunciado

unidade_a = {"Ana", "Bruno", "Carla", "Daniel"}
unidade_b = {"Bruno", "Elena", "Carla", "Felipe"}
Encontre alunos exclusivos de cada unidade (diferenca simetrica).
Exiba: somente em A, somente em B, e total de divergencias.

## Passo a passo

1. Crie os conjuntos `unidade_a` e `unidade_b` com os nomes do enunciado.
2. Calcule `somente_a` com a diferenca simples: `unidade_a - unidade_b` (quem esta em A mas nao em B).
3. Calcule `somente_b` com `unidade_b - unidade_a` (quem esta em B mas nao em A).
4. Calcule `divergencias` com a diferenca simetrica: `unidade_a ^ unidade_b` (uniao dos exclusivos dos dois lados). Confira que `len(divergencias) == len(somente_a) + len(somente_b)`.
5. Exiba: somente em A, somente em B (ambos com `sorted`) e o total de divergencias com `len(divergencias)`.

## Como executar

```bash
cd "13_set_diferenca_simetrica_alunos"
python main.py
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

```python
# Registros de vacinacao de cada unidade (enunciado)
unidade_a = {"Ana", "Bruno", "Carla", "Daniel"}
unidade_b = {"Bruno", "Elena", "Carla", "Felipe"}

# Diferenca simples: quem esta so de um lado
somente_a = unidade_a - unidade_b
somente_b = unidade_b - unidade_a

# Diferenca simetrica (^): todos os exclusivos, dos dois lados de uma vez
divergencias = unidade_a ^ unidade_b

# Relatorio de comparacao entre unidades
print("Somente na unidade A: ", sorted(somente_a))
print("Somente na unidade B: ", sorted(somente_b))
print("Total de divergencias:", len(divergencias))
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

```python
"""Comparacao das listas de vacinacao entre duas unidades."""


def comparar_unidades(a: set[str], b: set[str]) -> dict[str, set[str]]:
    """Devolve as tres visoes da comparacao em um unico dicionario.

    Agrupar os resultados evita que quem chama tenha que refazer
    as operacoes de conjunto — a comparacao vira uma unidade logica.
    """
    return {
        "somente_a": a - b,        # exclusivos da unidade A
        "somente_b": b - a,        # exclusivos da unidade B
        "divergencias": a ^ b,     # diferenca simetrica: todos os exclusivos
    }


def main() -> None:
    # Dados de entrada do enunciado
    unidade_a = {"Ana", "Bruno", "Carla", "Daniel"}
    unidade_b = {"Bruno", "Elena", "Carla", "Felipe"}

    # Executa a comparacao completa
    resultado = comparar_unidades(unidade_a, unidade_b)

    # Relatorio para a coordenacao da clinica
    print(f"Somente na unidade A:  {sorted(resultado['somente_a'])}")
    print(f"Somente na unidade B:  {sorted(resultado['somente_b'])}")
    print(f"Total de divergencias: {len(resultado['divergencias'])}")


if __name__ == "__main__":
    main()
```

</details>
