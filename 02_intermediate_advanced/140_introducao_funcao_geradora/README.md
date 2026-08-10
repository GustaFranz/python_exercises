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

## Passo a passo

1. Defina `gerar_eventos(quantidade)` com um `for i in range(1, quantidade + 1)` e, dentro do loop, `yield f"evento_{i}"` — o `yield` transforma a funcao em geradora: ela pausa a cada valor entregue e continua de onde parou na proxima iteracao.
2. Nao use `append` nem `return lista`: o objetivo e exatamente NAO montar a lista inteira na memoria.
3. No fluxo principal, crie `eventos = gerar_eventos(5)` e consuma com `for evento in eventos:` exibindo cada um; conte os consumidos com um contador no loop.
4. Crie um segundo gerador com `gerar_eventos(3)` e materialize com `list(...)` — exiba a lista para comparar as duas abordagens (consumo item a item vs materializacao).
5. Exiba a quantidade consumida em cada caso (5 no loop, `len(lista)` = 3 na conversao).
6. Extra para fixar: tente consumir o primeiro gerador de novo apos o loop e observe que ele esta esgotado (geradores so podem ser percorridos uma vez).

## Como executar

```bash
cd "140_introducao_funcao_geradora"
python main.py
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

```python
def gerar_eventos(quantidade):
    # yield transforma a funcao em GERADORA: cada chamada de next()
    # executa ate o yield, entrega o valor e PAUSA ate o proximo pedido
    for i in range(1, quantidade + 1):
        yield f"evento_{i}"


# 1) Consumo item a item: nenhuma lista completa existe na memoria
print("=== Consumo com for (5 eventos) ===")
consumidos_loop = 0
for evento in gerar_eventos(5):
    print(evento)
    consumidos_loop += 1  # contador manual dentro do loop

# 2) Materializacao: list() consome o gerador inteiro de uma vez
eventos_lista = list(gerar_eventos(3))
print(f"\n=== Convertido com list() ===\n{eventos_lista}")

# 3) Comparacao das quantidades consumidas em cada abordagem
print(f"\nConsumidos no loop: {consumidos_loop}")
print(f"Consumidos via list(): {len(eventos_lista)}")
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

```python
"""Introducao a geradores: producao lazy de eventos de acesso."""

from typing import Iterator


def gerar_eventos(quantidade: int) -> Iterator[str]:
    """Produz eventos sob demanda, um por vez.

    O hint Iterator[str] documenta o contrato: quem chama recebe
    algo iteravel que entrega strings — sem custo de memoria
    proporcional a quantidade.
    """
    for i in range(1, quantidade + 1):
        yield f"evento_{i}"


def main() -> None:
    # Consumo lazy: cada evento so e criado quando o for pede
    print("=== Consumo com for (5 eventos) ===")
    consumidos_loop = 0
    for evento in gerar_eventos(5):
        print(evento)
        consumidos_loop += 1

    # Materializacao explicita: util quando precisamos de len(), indexacao ou reuso
    eventos_lista = list(gerar_eventos(3))
    print(f"\n=== Convertido com list() ===\n{eventos_lista}")

    print(f"\nConsumidos no loop: {consumidos_loop}")
    print(f"Consumidos via list(): {len(eventos_lista)}")

    # Geradores se esgotam: reiterar um gerador ja consumido nao produz nada
    esgotado = gerar_eventos(2)
    list(esgotado)  # primeiro consumo esvazia
    print(f"Segunda passada no mesmo gerador: {list(esgotado)}")  # []


if __name__ == "__main__":
    main()
```

</details>
