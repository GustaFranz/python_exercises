# 142 - Funcao geradora: filtrar registros validos

## Objetivo

Usar gerador para validar e entregar apenas registros aprovados, um por vez.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | RH Escolar Mais |
| **Setor** | Recursos humanos |
| **Solicitacao** | Liberar bonus apenas para colaboradores elegiveis sem montar lista completa. |

## Enunciado

```python
registros = [
    {"id": 1, "nome": "Ana", "nota": 8.5, "faltas": 2},
    {"id": 2, "nome": "Bruno", "nota": 5.0, "faltas": 1},
    {"id": 3, "nome": "Carla", "nota": 9.0, "faltas": 0},
    {"id": 4, "nome": "Diego", "nota": 7.0, "faltas": 6},
    {"id": 5, "nome": "Elena", "nota": 7.5, "faltas": 3},
]
NOTA_MINIMA = 7.0
FALTAS_MAXIMAS = 4
```

Implemente `gerar_elegiveis(registros)` que:
- percorre registros;
- usa `yield` apenas para quem atende `nota >= NOTA_MINIMA` e `faltas <= FALTAS_MAXIMAS`;
- retorna dict completo do colaborador elegivel.

No `main`:
1) Consuma o gerador e exiba nome + nota de cada elegivel.
2) Conte elegiveis sem converter tudo em lista (use contador no loop).
3) Compare com `sum(1 for _ in gerar_elegiveis(registros))` para validar.

## Passo a passo

1. Crie `registros`, `NOTA_MINIMA` e `FALTAS_MAXIMAS` conforme o enunciado.
2. Defina `gerar_elegiveis(registros)` com um `for r in registros:` e, dentro, um `if r["nota"] >= NOTA_MINIMA and r["faltas"] <= FALTAS_MAXIMAS:` seguido de `yield r` — o `yield` condicional e o filtro: registros reprovados simplesmente nao sao entregues.
3. No fluxo principal, consuma com `for colaborador in gerar_elegiveis(registros):`, exibindo `nome` e `nota` e incrementando um contador — Ana, Carla e Elena passam; Bruno cai pela nota e Diego pelas faltas.
4. Valide a contagem com `sum(1 for _ in gerar_elegiveis(registros))` — repare que e preciso chamar o gerador DE NOVO: o primeiro ja foi esgotado pelo loop.
5. Exiba o contador do loop, a contagem via `sum` e confirme que sao iguais (3).

## Como executar

```bash
cd "142_funcao_geradora_filtrar"
python main.py
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

```python
registros = [
    {"id": 1, "nome": "Ana", "nota": 8.5, "faltas": 2},
    {"id": 2, "nome": "Bruno", "nota": 5.0, "faltas": 1},
    {"id": 3, "nome": "Carla", "nota": 9.0, "faltas": 0},
    {"id": 4, "nome": "Diego", "nota": 7.0, "faltas": 6},
    {"id": 5, "nome": "Elena", "nota": 7.5, "faltas": 3},
]
NOTA_MINIMA = 7.0
FALTAS_MAXIMAS = 4


def gerar_elegiveis(registros):
    # Gerador com filtro: so faz yield de quem passa nas DUAS regras;
    # os reprovados sao simplesmente pulados (nunca entram na saida)
    for r in registros:
        if r["nota"] >= NOTA_MINIMA and r["faltas"] <= FALTAS_MAXIMAS:
            yield r


# 1) e 2) Consome o gerador exibindo e contando no mesmo loop
print("=== Elegiveis ao bonus ===")
contador = 0
for colaborador in gerar_elegiveis(registros):
    contador += 1
    print(f"{colaborador['nome']}: nota {colaborador['nota']}")

# 3) Validacao: novo gerador (o anterior ja foi esgotado pelo for);
# sum(1 for _) conta sem guardar nada na memoria
validacao = sum(1 for _ in gerar_elegiveis(registros))

print(f"\nContados no loop: {contador}")
print(f"Contados via sum: {validacao}")
assert contador == validacao, "as duas contagens devem bater"
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

```python
"""Filtro lazy de colaboradores elegiveis ao bonus."""

from typing import Iterator

REGISTROS = [
    {"id": 1, "nome": "Ana", "nota": 8.5, "faltas": 2},
    {"id": 2, "nome": "Bruno", "nota": 5.0, "faltas": 1},
    {"id": 3, "nome": "Carla", "nota": 9.0, "faltas": 0},
    {"id": 4, "nome": "Diego", "nota": 7.0, "faltas": 6},
    {"id": 5, "nome": "Elena", "nota": 7.5, "faltas": 3},
]
NOTA_MINIMA = 7.0
FALTAS_MAXIMAS = 4


def eh_elegivel(registro: dict) -> bool:
    """Regra de elegibilidade isolada: testavel e reutilizavel."""
    return registro["nota"] >= NOTA_MINIMA and registro["faltas"] <= FALTAS_MAXIMAS


def gerar_elegiveis(registros: list[dict]) -> Iterator[dict]:
    """Entrega um elegivel por vez, sem materializar a lista filtrada."""
    for registro in registros:
        if eh_elegivel(registro):
            yield registro


def main() -> None:
    print("=== Elegiveis ao bonus ===")
    contador = 0
    for colaborador in gerar_elegiveis(REGISTROS):
        contador += 1
        print(f"{colaborador['nome']}: nota {colaborador['nota']}")

    # Gerador novo para validar: o consumido pelo for ja esta vazio
    validacao = sum(1 for _ in gerar_elegiveis(REGISTROS))

    print(f"\nContados no loop: {contador}")
    print(f"Contados via sum: {validacao}")
    assert contador == validacao, "as duas contagens devem bater"


if __name__ == "__main__":
    main()
```

</details>
