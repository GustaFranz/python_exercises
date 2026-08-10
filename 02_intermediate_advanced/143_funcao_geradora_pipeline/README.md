# 143 - Funcao geradora: pipeline de relatorio

## Objetivo

Encadear geradores para simular pipeline de dados (parse -> filtro -> metricas).

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | FinTech Escolar |
| **Setor** | Financeiro / analytics |
| **Solicitacao** | Processar transacoes do dia em pipeline lazy para relatorio executivo. |

## Enunciado

```python
transacoes_brutas = [
    "101;Ana;150.0;ok",
    "102;Bruno;-20.0;ok",
    "103;Carla;300.0;ok",
    "104;Diego;abc;ok",
    "105;Elena;80.0;cancelado",
    "106;Fabio;45.5;ok",
]
VALOR_MINIMO = 50.0
```

Implemente tres geradores:

1) `parse_transacoes(linhas)` — `yield` dict `{id, nome, valor, status}` (ignore linhas invalidas).
2) `filtrar_validas(transacoes)` — `yield` apenas status `"ok"` e valor numerico >= `VALOR_MINIMO`.
3) `gerar_resumo(transacoes)` — `yield` strings `"ID NOME: R$ VALOR"` formatadas.

No `main`:
- Encadeie: `resumo = gerar_resumo(filtrar_validas(parse_transacoes(transacoes_brutas)))`.
- Exiba cada linha do resumo.
- Calcule total aritmetico das transacoes validas (segundo filtro).
- Exiba quantidade processada vs quantidade no lote bruto.

## Passo a passo

1. Crie `transacoes_brutas` e `VALOR_MINIMO` conforme o enunciado.
2. Defina `parse_transacoes(linhas)`: para cada linha, faca `partes = linha.split(";")`; converta `partes[2]` com `float` dentro de `try/except ValueError` — se falhar (caso do `"abc"`), use `continue` para pular a linha sem `yield`; no sucesso, `yield {"id": partes[0], "nome": partes[1], "valor": valor, "status": partes[3]}`.
3. Defina `filtrar_validas(transacoes)`: `yield` apenas quando `t["status"] == "ok"` e `t["valor"] >= VALOR_MINIMO` (elimina Bruno com -20.0, Elena cancelada e Fabio abaixo do minimo).
4. Defina `gerar_resumo(transacoes)`: `yield f"{t['id']} {t['nome']}: R$ {t['valor']:.2f}"` para cada transacao recebida.
5. No fluxo principal, encadeie os tres geradores: `resumo = gerar_resumo(filtrar_validas(parse_transacoes(transacoes_brutas)))` — nada e processado ainda; o trabalho so acontece quando o `for` consome.
6. Percorra `resumo` exibindo cada linha (devem sobrar Ana e Carla).
7. Para o total e a contagem, crie um NOVO encadeamento `filtrar_validas(parse_transacoes(...))` (o primeiro ja foi esgotado) e acumule `valor` e quantidade num loop — total esperado: 450.00, processadas: 2.
8. Exiba `quantidade processada vs len(transacoes_brutas)` (2 vs 6).

## Como executar

```bash
cd "143_funcao_geradora_pipeline"
python main.py
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

```python
transacoes_brutas = [
    "101;Ana;150.0;ok",
    "102;Bruno;-20.0;ok",
    "103;Carla;300.0;ok",
    "104;Diego;abc;ok",
    "105;Elena;80.0;cancelado",
    "106;Fabio;45.5;ok",
]
VALOR_MINIMO = 50.0


def parse_transacoes(linhas):
    # Etapa 1 do pipeline: texto bruto -> dict estruturado
    for linha in linhas:
        partes = linha.split(";")
        try:
            valor = float(partes[2])
        except ValueError:
            continue  # linha invalida (ex.: "abc") e pulada SEM yield
        yield {"id": partes[0], "nome": partes[1], "valor": valor, "status": partes[3]}


def filtrar_validas(transacoes):
    # Etapa 2: so passa status ok E valor acima do minimo
    for t in transacoes:
        if t["status"] == "ok" and t["valor"] >= VALOR_MINIMO:
            yield t


def gerar_resumo(transacoes):
    # Etapa 3: dict -> string formatada para o relatorio
    for t in transacoes:
        yield f"{t['id']} {t['nome']}: R$ {t['valor']:.2f}"


# Encadeamento lazy: nenhuma linha e processada aqui —
# o trabalho so acontece quando o for abaixo pede cada item
resumo = gerar_resumo(filtrar_validas(parse_transacoes(transacoes_brutas)))

print("=== Relatorio de transacoes validas ===")
for linha in resumo:
    print(linha)

# O pipeline acima ja foi consumido; para somar, encadeia de novo
total = 0.0
processadas = 0
for t in filtrar_validas(parse_transacoes(transacoes_brutas)):
    total += t["valor"]
    processadas += 1

print(f"\nTotal das validas: R$ {total:.2f}")
print(f"Processadas: {processadas} de {len(transacoes_brutas)} no lote bruto")
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

```python
"""Pipeline lazy de transacoes: parse -> filtro -> formatacao.

Mesmo desenho usado em ETLs reais: cada etapa e um gerador tipado
que consome a anterior; nada e materializado ate o consumo final.
"""

from typing import Iterable, Iterator, TypedDict

TRANSACOES_BRUTAS = [
    "101;Ana;150.0;ok",
    "102;Bruno;-20.0;ok",
    "103;Carla;300.0;ok",
    "104;Diego;abc;ok",
    "105;Elena;80.0;cancelado",
    "106;Fabio;45.5;ok",
]
VALOR_MINIMO = 50.0
STATUS_VALIDO = "ok"


class Transacao(TypedDict):
    """Formato canonico de uma transacao apos o parse."""

    id: str
    nome: str
    valor: float
    status: str


def parse_transacoes(linhas: Iterable[str]) -> Iterator[Transacao]:
    """Converte linhas 'id;nome;valor;status' em dicts; descarta invalidas."""
    for linha in linhas:
        id_, nome, valor_texto, status = linha.split(";")
        try:
            valor = float(valor_texto)
        except ValueError:
            continue  # registro corrompido: descarta e segue o lote
        yield {"id": id_, "nome": nome, "valor": valor, "status": status}


def filtrar_validas(transacoes: Iterable[Transacao]) -> Iterator[Transacao]:
    """Mantem apenas transacoes com status ok e valor acima do minimo."""
    for transacao in transacoes:
        if transacao["status"] == STATUS_VALIDO and transacao["valor"] >= VALOR_MINIMO:
            yield transacao


def gerar_resumo(transacoes: Iterable[Transacao]) -> Iterator[str]:
    """Formata cada transacao como linha de relatorio."""
    for t in transacoes:
        yield f"{t['id']} {t['nome']}: R$ {t['valor']:.2f}"


def main() -> None:
    # Materializa as validas UMA vez: o dataset e pequeno e precisamos
    # de tres leituras (linhas, total, contagem) — evita reprocessar o parse
    validas = list(filtrar_validas(parse_transacoes(TRANSACOES_BRUTAS)))

    print("=== Relatorio de transacoes validas ===")
    for linha in gerar_resumo(validas):
        print(linha)

    total = sum(t["valor"] for t in validas)
    print(f"\nTotal das validas: R$ {total:.2f}")
    print(f"Processadas: {len(validas)} de {len(TRANSACOES_BRUTAS)} no lote bruto")


if __name__ == "__main__":
    main()
```

</details>
