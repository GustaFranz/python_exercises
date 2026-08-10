# 55 - Try except: arquivo opcional

## Objetivo

Implemente carregar_config(caminho) com try/except FileNotFoundError.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | MonitoraTI |
| **Setor** | Infraestrutura / suporte |
| **Solicitacao** | Ler configuracao local se existir; caso contrario usar padrao. |

## Enunciado

1) Crie o arquivo `config.txt` com uma linha:
```
modo=producao
```

2) Implemente:
```python
def carregar_config(caminho: str) -> str:
    try:
        with open(caminho, encoding="utf-8") as f:
            return f.read().strip()
    except FileNotFoundError:
        return "modo=padrao"
```

3) Teste:
   - `carregar_config("config.txt")` — arquivo existente.
   - `carregar_config("arquivo_inexistente.txt")` — fallback.

Exemplo de saida:

```
Config: modo=producao
Config: modo=padrao
```

## Passo a passo

1. Crie o arquivo `config.txt` no inicio do script: `with open("config.txt", "w", encoding="utf-8") as f:` gravando a linha `modo=producao`.
2. Defina `def carregar_config(caminho: str) -> str:`.
3. No `try:`, abra o arquivo com `with open(caminho, encoding="utf-8") as f:` e retorne `f.read().strip()` — o `.strip()` remove a quebra de linha final.
4. No `except FileNotFoundError:`, retorne a string padrao `"modo=padrao"` — esse e o fallback quando o arquivo nao existe.
5. Teste com `carregar_config("config.txt")` e exiba `f"Config: {...}"`.
6. Teste com `carregar_config("arquivo_inexistente.txt")` e exiba do mesmo jeito — deve aparecer o valor padrao.

## Como executar

```bash
cd "55_try_arquivo_opcional"
python main.py
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

```python
# Cria o arquivo de config local para o teste do caminho existente
with open("config.txt", "w", encoding="utf-8") as f:
    f.write("modo=producao\n")


def carregar_config(caminho):
    try:
        # Tenta ler a config local
        with open(caminho, encoding="utf-8") as f:
            # strip remove a quebra de linha final do arquivo
            return f.read().strip()
    except FileNotFoundError:
        # Arquivo nao existe: usa a configuracao padrao (fallback)
        return "modo=padrao"


# Teste 1: arquivo existe — retorna o conteudo gravado
print(f"Config: {carregar_config('config.txt')}")

# Teste 2: arquivo nao existe — cai no fallback
print(f"Config: {carregar_config('arquivo_inexistente.txt')}")
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

```python
"""Carrega configuracao local com fallback para valor padrao."""

from pathlib import Path

ARQUIVO_CONFIG = Path("config.txt")
CONFIG_PADRAO = "modo=padrao"


def preparar_config_exemplo() -> None:
    """Gera o config.txt local para o cenario de arquivo existente."""
    ARQUIVO_CONFIG.write_text("modo=producao\n", encoding="utf-8")


def carregar_config(caminho: Path) -> str:
    """Le a config do arquivo; devolve CONFIG_PADRAO se ele nao existir.

    Estilo EAFP (easier to ask forgiveness than permission): tenta ler
    direto e trata a ausencia, em vez de checar exists() antes — evita
    condicao de corrida entre a checagem e a leitura.
    """
    try:
        return caminho.read_text(encoding="utf-8").strip()
    except FileNotFoundError:
        return CONFIG_PADRAO


def main() -> None:
    preparar_config_exemplo()

    # Arquivo existente e arquivo ausente exercitam os dois caminhos
    for caminho in (ARQUIVO_CONFIG, Path("arquivo_inexistente.txt")):
        print(f"Config: {carregar_config(caminho)}")


if __name__ == "__main__":
    main()
```

</details>
