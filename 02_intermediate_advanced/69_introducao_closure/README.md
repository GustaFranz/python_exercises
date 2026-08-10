# 69 - Introducao a closure

## Objetivo

Criar funcao interna que captura variavel do escopo externo.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | Loja Virtual Escolar |
| **Setor** | Varejo / precificacao |
| **Solicitacao** | Aplicar taxa fixa de embalagem em todos os pedidos escolares. |

## Visao do bloco (exercicios 69 a 73)

Topico **Closure**: funcao interna que lembra variaveis do escopo onde foi criada.

| # | Nivel | Foco |
|---|-------|------|
| 69 | Leve | Introducao + somador com taxa fixa |
| 70 | Leve | Multiplicador capturado |
| 71 | Ponte | Filtro com limite capturado |
| 72 | Entrevista | Fabrica de relatorio por turma + estatisticas |
| 73 | Entrevista | Fabrica de validadores criar_validador(min, max) |

## Enunciado

- Implemente criar_somador_com_taxa(taxa) retornando closure.
- Teste com taxa 5 e valores 10, 20 e 0.

## Passo a passo

1. Defina a funcao externa `criar_somador_com_taxa(taxa)`.
2. Dentro dela, defina a funcao interna `adicionar(valor)` que retorna `valor + taxa`. Repare que `adicionar` usa `taxa` sem receber como parametro — ela "enxerga" a variavel do escopo externo.
3. A funcao externa deve retornar `adicionar` (a funcao em si, SEM parenteses — nao e para chama-la, e para devolve-la).
4. No corpo principal, crie o closure: `somar = criar_somador_com_taxa(5)`. A partir daqui `somar` e uma funcao que lembra `taxa = 5`.
5. Chame `somar(10)`, `somar(20)` e `somar(0)` e exiba cada resultado (esperado: 15, 25 e 5).

## Como executar

```bash
cd "69_introducao_closure"
python main.py
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

```python
def criar_somador_com_taxa(taxa):
    # Funcao interna: usa a variavel taxa do escopo externo
    # sem receber por parametro — isso e o closure
    def adicionar(valor):
        return valor + taxa

    # Retorna a funcao (sem parenteses): quem chamou recebe
    # uma funcao pronta, com a taxa "gravada" dentro dela
    return adicionar


# Cria o closure com taxa fixa de 5 (taxa de embalagem)
somar = criar_somador_com_taxa(5)

# Cada chamada usa a taxa capturada, sem precisar repassa-la
print(somar(10))  # 10 + 5 -> 15
print(somar(20))  # 20 + 5 -> 25
print(somar(0))   # 0 + 5  -> 5
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

```python
"""Closure para aplicar taxa fixa de embalagem em pedidos.

No mercado, esse padrao (fabrica de funcoes configuradas) aparece em
callbacks, validadores e handlers. Para o caso especifico de "fixar um
argumento", um dev tambem usaria functools.partial (mostrado no final).
"""

from collections.abc import Callable


def criar_somador_com_taxa(taxa: float) -> Callable[[float], float]:
    """Retorna uma funcao que soma a taxa capturada ao valor recebido."""

    def adicionar(valor: float) -> float:
        # taxa vem do escopo de criar_somador_com_taxa e permanece
        # viva entre as chamadas — e o que define um closure
        return valor + taxa

    return adicionar


def main() -> None:
    somar = criar_somador_com_taxa(5)

    # O mesmo closure serve para qualquer pedido, sem repetir a taxa
    for valor in (10, 20, 0):
        print(f"{valor} + taxa = {somar(valor)}")

    # Alternativa de mercado com functools.partial (mesmo efeito):
    # from functools import partial
    # from operator import add
    # somar = partial(add, 5)


if __name__ == "__main__":
    main()
```

</details>
