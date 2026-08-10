# 40 - CSV: importar vendas com validacao e totais

## Objetivo

Importar CSV de vendas, validar linhas e calcular metricas comerciais.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | Mercado Bom Preco |
| **Setor** | Varejo / financeiro |
| **Solicitacao** | Importar vendas do caixa, rejeitar linhas invalidas e fechar o dia. |

## Enunciado

Crie `vendas.csv` (ou use dados embutidos e grave o arquivo) com cabecalho:
`produto,quantidade,preco_unitario`

Inclua linhas validas e invalidas, por exemplo:
```
produto,quantidade,preco_unitario
caneta,10,2.50
caderno,5,12.00
borracha,-2,1.00
lapis,3,abc
marcador,8,4.50
```

Regras:
- `quantidade` deve ser int > 0
- `preco_unitario` deve ser float > 0
- linha invalida vai para lista de rejeicoes (motivo claro)

Calcule para linhas validas: subtotal, itens vendidos, faturamento total,
ticket medio (faturamento / qtd de linhas validas).
Exiba tabela valida, rejeicoes e resumo do fechamento do dia.

## Passo a passo

1. Importe `csv` e crie a constante `CAMINHO = "vendas.csv"`.
2. Grave o arquivo de exemplo do enunciado (com as linhas invalidas) usando `with open(..., "w", encoding="utf-8", newline="")` e `arquivo.write(...)`.
3. Defina `def validar_linha(linha):` que:
   - converte `quantidade = int(linha["quantidade"])` e `preco = float(linha["preco_unitario"])` dentro de `try/except ValueError` — conversao que falha (ex.: `"abc"`) retorna motivo "valor nao numerico";
   - checa `quantidade > 0` e `preco > 0`, retornando o motivo especifico quando violado;
   - em caso de sucesso, retorna a linha convertida (dict com tipos corretos) e `None` como motivo.
4. Crie as listas `validas` e `rejeicoes`.
5. Leia o CSV com `csv.DictReader` e, para cada linha, chame `validar_linha`: valida vai para `validas` (com `subtotal = quantidade * preco` ja calculado); invalida vai para `rejeicoes` como `{"linha": ..., "motivo": ...}`.
6. Calcule os totais sobre `validas`: `itens = sum(...)` das quantidades, `faturamento = sum(...)` dos subtotais e `ticket_medio = faturamento / len(validas) if validas else 0`.
7. Exiba tres blocos: tabela de vendas validas (produto, quantidade, preco, subtotal), rejeicoes com motivo e resumo do dia (itens, faturamento e ticket medio com `:.2f`).

## Como executar

```bash
cd "40_csv_importar_vendas_totais"
python main.py
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

```python
import csv

CAMINHO = "vendas.csv"

# Etapa 0: grava o CSV de exemplo com linhas validas e invalidas.
CONTEUDO = """produto,quantidade,preco_unitario
caneta,10,2.50
caderno,5,12.00
borracha,-2,1.00
lapis,3,abc
marcador,8,4.50
"""
with open(CAMINHO, "w", encoding="utf-8", newline="") as arquivo:
    arquivo.write(CONTEUDO)


def validar_linha(linha):
    # Retorna (linha_convertida, None) se valida, ou (None, motivo) se nao.
    try:
        quantidade = int(linha["quantidade"])
        preco = float(linha["preco_unitario"])
    except ValueError:
        # int()/float() falham para texto como "abc".
        return None, "valor nao numerico"
    if quantidade <= 0:
        return None, f"quantidade invalida ({quantidade})"
    if preco <= 0:
        return None, f"preco invalido ({preco})"
    # Linha valida: devolve os campos ja convertidos e com subtotal.
    convertida = {
        "produto": linha["produto"],
        "quantidade": quantidade,
        "preco_unitario": preco,
        "subtotal": quantidade * preco,
    }
    return convertida, None


# Importacao: separa linhas validas das rejeicoes.
validas = []
rejeicoes = []
with open(CAMINHO, encoding="utf-8", newline="") as arquivo:
    for linha in csv.DictReader(arquivo):
        convertida, motivo = validar_linha(linha)
        if motivo:
            # Guarda a linha original e o motivo para auditoria.
            rejeicoes.append({"linha": dict(linha), "motivo": motivo})
        else:
            validas.append(convertida)

# Metricas do fechamento, calculadas so sobre as linhas validas.
itens = sum(v["quantidade"] for v in validas)
faturamento = sum(v["subtotal"] for v in validas)
# Evita divisao por zero se nenhuma linha for valida.
ticket_medio = faturamento / len(validas) if validas else 0

# Bloco 1: tabela de vendas validas.
print("=== Vendas validas ===")
for v in validas:
    print(
        f"{v['produto']} | qtd {v['quantidade']} | "
        f"unit {v['preco_unitario']:.2f} | subtotal {v['subtotal']:.2f}"
    )

# Bloco 2: rejeicoes com motivo claro.
print("=== Rejeicoes ===")
for r in rejeicoes:
    print(f"{r['linha']['produto']} | motivo: {r['motivo']}")

# Bloco 3: resumo do fechamento do dia.
print("=== Fechamento do dia ===")
print(f"Itens vendidos: {itens}")
print(f"Faturamento: {faturamento:.2f}")
print(f"Ticket medio: {ticket_medio:.2f}")
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

```python
"""Importa vendas do caixa, valida linhas e fecha o dia com metricas."""

import csv
from dataclasses import dataclass
from pathlib import Path

CAMINHO = Path(__file__).parent / "vendas.csv"

CONTEUDO_EXEMPLO = """produto,quantidade,preco_unitario
caneta,10,2.50
caderno,5,12.00
borracha,-2,1.00
lapis,3,abc
marcador,8,4.50
"""


@dataclass
class Venda:
    """Linha valida do caixa, ja convertida e com subtotal derivado."""

    produto: str
    quantidade: int
    preco_unitario: float

    @property
    def subtotal(self) -> float:
        # Propriedade derivada: nao armazena valor que pode divergir.
        return self.quantidade * self.preco_unitario


@dataclass
class Rejeicao:
    """Linha invalida com o motivo da rejeicao."""

    linha: dict[str, str]
    motivo: str


def validar_linha(linha: dict[str, str]) -> Venda | Rejeicao:
    """Converte e valida uma linha; retorna Venda ou Rejeicao."""
    try:
        quantidade = int(linha["quantidade"])
        preco = float(linha["preco_unitario"])
    except ValueError:
        return Rejeicao(linha=linha, motivo="valor nao numerico")
    # Guard clauses: cada regra falha com motivo especifico.
    if quantidade <= 0:
        return Rejeicao(linha=linha, motivo=f"quantidade invalida ({quantidade})")
    if preco <= 0:
        return Rejeicao(linha=linha, motivo=f"preco invalido ({preco})")
    return Venda(produto=linha["produto"], quantidade=quantidade, preco_unitario=preco)


def importar(caminho: Path) -> tuple[list[Venda], list[Rejeicao]]:
    """Le o CSV separando vendas validas de rejeicoes."""
    vendas: list[Venda] = []
    rejeicoes: list[Rejeicao] = []
    with caminho.open(encoding="utf-8", newline="") as arquivo:
        for linha in csv.DictReader(arquivo):
            resultado = validar_linha(linha)
            # isinstance roteia o resultado para a lista certa.
            if isinstance(resultado, Venda):
                vendas.append(resultado)
            else:
                rejeicoes.append(resultado)
    return vendas, rejeicoes


def main() -> None:
    # Grava o arquivo de exemplo (script autossuficiente).
    CAMINHO.write_text(CONTEUDO_EXEMPLO, encoding="utf-8")

    vendas, rejeicoes = importar(CAMINHO)

    itens = sum(v.quantidade for v in vendas)
    faturamento = sum(v.subtotal for v in vendas)
    ticket_medio = faturamento / len(vendas) if vendas else 0

    print("=== Vendas validas ===")
    for v in vendas:
        print(
            f"{v.produto} | qtd {v.quantidade} | "
            f"unit {v.preco_unitario:.2f} | subtotal {v.subtotal:.2f}"
        )

    print("=== Rejeicoes ===")
    for r in rejeicoes:
        print(f"{r.linha['produto']} | motivo: {r.motivo}")

    print("=== Fechamento do dia ===")
    print(f"Itens vendidos: {itens}")
    print(f"Faturamento: {faturamento:.2f}")
    print(f"Ticket medio: {ticket_medio:.2f}")


if __name__ == "__main__":
    main()
```

</details>
