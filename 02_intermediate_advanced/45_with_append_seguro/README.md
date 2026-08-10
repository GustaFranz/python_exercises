# 45 - With open: append seguro

## Objetivo

Arquivo rotas_dia.txt com 2 rotas iniciais.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | LogiRapida |
| **Setor** | Logistica / rastreamento |
| **Solicitacao** | Registrar novas entregas no fim do arquivo de rotas do dia. |

## Enunciado

1) Crie `rotas_dia.txt` com 2 linhas iniciais:
```
Rota 01 — Centro
Rota 02 — Zona Norte
```

2) Adicione 2 novas linhas com modo `"a"` (append):
```
Rota 03 — Zona Sul
Rota 04 — Aeroporto
```

3) Leia e exiba o arquivo completo apos o append com um segundo `with open` em modo `"r"`.

Exemplo de saida:

```
Rota 01 — Centro
Rota 02 — Zona Norte
Rota 03 — Zona Sul
Rota 04 — Aeroporto
```

## Passo a passo

1. Defina a constante `ARQUIVO = "rotas_dia.txt"` e duas listas: `ROTAS_INICIAIS` (Rota 01 e 02) e `ROTAS_NOVAS` (Rota 03 e 04).
2. Crie o arquivo inicial com `with open(ARQUIVO, "w", encoding="utf-8") as f:` gravando as 2 rotas iniciais (uma por linha, com `"\n"` no final).
3. Abra de novo com `with open(ARQUIVO, "a", encoding="utf-8") as f:` — o modo `"a"` posiciona a escrita no fim do arquivo, sem apagar o que ja existe — e grave as 2 rotas novas.
4. Abra uma terceira vez com `with open(ARQUIVO, "r", encoding="utf-8") as f:` e leia tudo com `f.read()`.
5. Exiba o conteudo completo com `print` — devem aparecer as 4 rotas na ordem.

## Como executar

```bash
cd "45_with_append_seguro"
python main.py
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

```python
# Arquivo de rotas do dia
ARQUIVO = "rotas_dia.txt"

# Rotas que ja existiam no inicio do dia
ROTAS_INICIAIS = [
    "Rota 01 — Centro",
    "Rota 02 — Zona Norte",
]

# Novas entregas para registrar no fim do arquivo
ROTAS_NOVAS = [
    "Rota 03 — Zona Sul",
    "Rota 04 — Aeroporto",
]

# 1) Modo "w" cria o arquivo com o conteudo inicial
with open(ARQUIVO, "w", encoding="utf-8") as f:
    f.write("\n".join(ROTAS_INICIAIS) + "\n")

# 2) Modo "a" (append) escreve no FIM do arquivo, sem apagar nada
with open(ARQUIVO, "a", encoding="utf-8") as f:
    f.write("\n".join(ROTAS_NOVAS) + "\n")

# 3) Modo "r" le o resultado final para conferencia
with open(ARQUIVO, "r", encoding="utf-8") as f:
    conteudo = f.read()

# end="" evita linha em branco extra, pois o conteudo ja termina com "\n"
print(conteudo, end="")
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

```python
"""Registra novas entregas no fim do arquivo de rotas do dia."""

from pathlib import Path

ARQUIVO_ROTAS = Path("rotas_dia.txt")

ROTAS_INICIAIS = ["Rota 01 — Centro", "Rota 02 — Zona Norte"]
ROTAS_NOVAS = ["Rota 03 — Zona Sul", "Rota 04 — Aeroporto"]


def criar_arquivo_inicial(destino: Path, rotas: list[str]) -> None:
    """Cria o arquivo do dia com as rotas ja programadas."""
    destino.write_text("\n".join(rotas) + "\n", encoding="utf-8")


def registrar_rotas(destino: Path, rotas: list[str]) -> None:
    """Acrescenta rotas no fim do arquivo sem apagar o conteudo anterior."""
    # Path.open aceita os mesmos modos do open; "a" e append
    with destino.open("a", encoding="utf-8") as f:
        f.write("\n".join(rotas) + "\n")


def main() -> None:
    criar_arquivo_inicial(ARQUIVO_ROTAS, ROTAS_INICIAIS)
    registrar_rotas(ARQUIVO_ROTAS, ROTAS_NOVAS)

    # Le o resultado final e exibe para conferencia
    print(ARQUIVO_ROTAS.read_text(encoding="utf-8"), end="")


if __name__ == "__main__":
    main()
```

</details>
