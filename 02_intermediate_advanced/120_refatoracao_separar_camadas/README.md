# 120 - Refatoracao: separar camadas

## Objetivo

Separar leitura de dados, regra de negocio e apresentacao.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | FinEdu Carteira |
| **Setor** | Financeiro educacional |
| **Solicitacao** | Organizar script de cobranca de mensalidades em camadas claras. |

## Enunciado

Cada registro e um dict: `{"aluno": str, "valor": float, "pago": bool}`.

Implemente 3 funcoes separadas:

1) `carregar_dados() -> list[dict]` — retorna lista fixa de exemplo (I/O simulada). Exemplo:
   ```python
   [
       {"aluno": "Ana", "valor": 350.0, "pago": True},
       {"aluno": "Bruno", "valor": 350.0, "pago": False},
       {"aluno": "Carla", "valor": 400.0, "pago": False},
   ]
   ```
2) `calcular_pendentes(dados) -> list[dict]` — retorna apenas registros com `pago == False` (regra de negocio; sem `print`).
3) `exibir_relatorio(pendentes) -> None` — imprime relatorio formatado (apenas apresentacao).

Crie `main()` que orquestra as tres camadas na ordem: carregar → calcular → exibir.

Regras:
- `carregar_dados` nao calcula.
- `calcular_pendentes` nao imprime.
- Cada funcao tem uma unica responsabilidade.

Exemplo de saida:

```
Mensalidades pendentes:
- Bruno: R$ 350.00
- Carla: R$ 400.00
Total pendente: R$ 750.00
```

## Passo a passo

1. Implemente a camada de dados `carregar_dados() -> list[dict]`: apenas retorna a lista fixa do enunciado (Ana paga, Bruno e Carla pendentes) — nenhum calculo aqui.
2. Implemente a camada de regra `calcular_pendentes(dados) -> list[dict]`: filtre com list comprehension os registros em que `pago` e `False` e retorne a lista — nenhum `print` aqui.
3. Implemente a camada de apresentacao `exibir_relatorio(pendentes) -> None`:
   - Imprima o titulo `Mensalidades pendentes:`.
   - Para cada pendente, imprima `- {aluno}: R$ {valor:.2f}`.
   - Some os valores pendentes e imprima `Total pendente: R$ {total:.2f}`.
4. Crie `main()` orquestrando na ordem: `dados = carregar_dados()` → `pendentes = calcular_pendentes(dados)` → `exibir_relatorio(pendentes)`.
5. Chame `main()` e confira a saida do enunciado (Bruno 350.00, Carla 400.00, total 750.00).

## Como executar

```bash
cd "120_refatoracao_separar_camadas"
python main.py
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

```python
def carregar_dados():
    # CAMADA DE DADOS: so entrega os registros (I/O simulada).
    # Se amanha os dados vierem de JSON ou banco, so esta funcao muda
    return [
        {"aluno": "Ana", "valor": 350.0, "pago": True},
        {"aluno": "Bruno", "valor": 350.0, "pago": False},
        {"aluno": "Carla", "valor": 400.0, "pago": False},
    ]


def calcular_pendentes(dados):
    # CAMADA DE REGRA: decide o que e pendente, sem imprimir nada.
    # Funcao pura: mesma entrada -> mesma saida (facil de testar)
    return [registro for registro in dados if not registro["pago"]]


def exibir_relatorio(pendentes):
    # CAMADA DE APRESENTACAO: so formata e imprime
    print("Mensalidades pendentes:")
    for registro in pendentes:
        print(f"- {registro['aluno']}: R$ {registro['valor']:.2f}")
    # Total calculado sobre a lista ja filtrada pela camada de regra
    total = sum(registro["valor"] for registro in pendentes)
    print(f"Total pendente: R$ {total:.2f}")


def main():
    # Orquestracao: carregar -> calcular -> exibir
    dados = carregar_dados()
    pendentes = calcular_pendentes(dados)
    exibir_relatorio(pendentes)


main()
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

```python
def carregar_dados() -> list[dict]:
    """Camada de dados: fornece os registros de mensalidade (I/O simulada)."""
    return [
        {"aluno": "Ana", "valor": 350.0, "pago": True},
        {"aluno": "Bruno", "valor": 350.0, "pago": False},
        {"aluno": "Carla", "valor": 400.0, "pago": False},
    ]


def calcular_pendentes(dados: list[dict]) -> list[dict]:
    """Camada de regra: filtra registros nao pagos (funcao pura, sem print)."""
    return [registro for registro in dados if not registro["pago"]]


def total_pendente(pendentes: list[dict]) -> float:
    """Camada de regra: soma dos valores pendentes."""
    # O total tambem e regra de negocio — separado da apresentacao,
    # pode ser reutilizado por outros relatorios ou testado isolado
    return sum(registro["valor"] for registro in pendentes)


def exibir_relatorio(pendentes: list[dict]) -> None:
    """Camada de apresentacao: formata e imprime o relatorio."""
    print("Mensalidades pendentes:")
    for registro in pendentes:
        print(f"- {registro['aluno']}: R$ {registro['valor']:.2f}")
    print(f"Total pendente: R$ {total_pendente(pendentes):.2f}")


def main() -> None:
    # main() so conecta as camadas; nao contem logica propria
    dados = carregar_dados()
    pendentes = calcular_pendentes(dados)
    exibir_relatorio(pendentes)


if __name__ == "__main__":
    main()
```

</details>
