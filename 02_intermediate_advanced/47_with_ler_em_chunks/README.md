# 47 - With open: ler log em chunks e auditar tokens

## Objetivo

Processar arquivo de log grande em blocos e gerar relatorio de auditoria sem carregar tudo na memoria.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | MonitoraTI |
| **Setor** | Infraestrutura / observabilidade |
| **Solicitacao** | Auditar arquivo de acesso simulado em chunks para contagem de linhas e tokens ERROR/INFO dentro do SLA de processamento. |

## Enunciado

- Crie `acesso.log` com pelo menos 30 linhas simulando access log (mix de `INFO` e `ERROR`).
- Leia o arquivo em chunks de 128 caracteres com `read(128)` dentro de um loop (nao use `.read()` sem tamanho).
- Conte total de linhas e ocorrencias dos tokens `ERROR` e `INFO` no arquivo inteiro.
- Exiba relatorio: chunks lidos, caracteres totais, linhas, ERROR, INFO e proporcao ERROR (%).

## Passo a passo

1. Defina as constantes `CHUNK_SIZE = 128` e `ARQUIVO = "acesso.log"`.
2. Gere o log com um `for i in range(1, 31)` dentro de `with open(ARQUIVO, "w", encoding="utf-8")`: escreva linhas como `f"2026-07-30 {nivel} usuario=user{i:02d} acao=login\n"`, alternando o nivel (ex.: `"ERROR"` quando `i % 5 == 0`, senao `"INFO"`).
3. Abra o arquivo em `"r"` e leia em blocos com um loop: `while True:` -> `bloco = f.read(CHUNK_SIZE)` -> `if not bloco: break`.
4. A cada bloco, incremente um contador `chunks` e acumule o texto em uma variavel `texto` (ou some as metricas bloco a bloco).
5. Apos o loop, calcule: `linhas = texto.splitlines()`, `total_error = texto.count("ERROR")` e `total_info = texto.count("INFO")`.
6. Calcule a proporcao: `pct_error = round(total_error / len(linhas) * 100, 1)`.
7. Exiba o relatorio com 6 linhas de `print`: chunks lidos, caracteres totais (`len(texto)`), linhas, ERROR, INFO e proporcao ERROR (%).

## Como executar

```bash
cd "47_with_ler_em_chunks"
python main.py
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

```python
# Tamanho de cada bloco de leitura, em caracteres
CHUNK_SIZE = 128
ARQUIVO = "acesso.log"
TOTAL_LINHAS = 30

# Gera o access log simulado: 1 ERROR a cada 5 linhas, o resto INFO
with open(ARQUIVO, "w", encoding="utf-8") as f:
    for i in range(1, TOTAL_LINHAS + 1):
        nivel = "ERROR" if i % 5 == 0 else "INFO"
        # {i:02d} gera 01, 02, ... para nomes de usuario diferentes
        f.write(f"2026-07-30 {nivel} usuario=user{i:02d} acao=login\n")

# Leitura em chunks: nunca chama read() sem tamanho
texto = ""
chunks = 0
with open(ARQUIVO, "r", encoding="utf-8") as f:
    while True:
        # Le no maximo CHUNK_SIZE caracteres por vez
        bloco = f.read(CHUNK_SIZE)
        # String vazia significa fim do arquivo
        if not bloco:
            break
        chunks += 1
        # Acumula para calcular as metricas do arquivo inteiro
        texto += bloco

# Metricas calculadas sobre o texto acumulado
linhas = texto.splitlines()
total_error = texto.count("ERROR")
total_info = texto.count("INFO")
# Proporcao de linhas com ERROR sobre o total, arredondada a 1 casa
pct_error = round(total_error / len(linhas) * 100, 1)

# Relatorio de auditoria
print(f"Chunks lidos: {chunks}")
print(f"Caracteres totais: {len(texto)}")
print(f"Linhas: {len(linhas)}")
print(f"ERROR: {total_error}")
print(f"INFO: {total_info}")
print(f"Proporcao ERROR: {pct_error}%")
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

```python
"""Auditoria de access log lendo em chunks, sem carregar o arquivo inteiro.

Diferente da versao intermediaria, aqui as metricas sao somadas bloco a
bloco: a memoria usada nao cresce com o tamanho do arquivo.
"""

from collections import Counter
from functools import partial
from pathlib import Path

CHUNK_SIZE = 128
ARQUIVO = Path("acesso.log")
TOTAL_LINHAS_EXEMPLO = 30


def gerar_log_exemplo(destino: Path, total: int) -> None:
    """Gera o access log simulado com mix de INFO e ERROR."""
    linhas = (
        f"2026-07-30 {'ERROR' if i % 5 == 0 else 'INFO'} usuario=user{i:02d} acao=login"
        for i in range(1, total + 1)
    )
    destino.write_text("\n".join(linhas) + "\n", encoding="utf-8")


def auditar_em_chunks(origem: Path, tamanho: int) -> dict[str, float]:
    """Le o arquivo em blocos e soma as metricas incrementalmente."""
    contagem: Counter[str] = Counter()
    caracteres = 0
    chunks = 0
    # Guarda o pedaco de linha que ficou cortado entre dois chunks
    resto = ""

    with origem.open(encoding="utf-8") as f:
        # iter com sentinela: chama f.read(tamanho) ate devolver "" (fim do arquivo)
        for bloco in iter(partial(f.read, tamanho), ""):
            chunks += 1
            caracteres += len(bloco)
            # Junta o resto anterior e separa apenas as linhas completas
            linhas = (resto + bloco).split("\n")
            # A ultima parte pode estar incompleta: volta para o buffer
            resto = linhas.pop()
            for linha in linhas:
                contagem["linhas"] += 1
                # Contagem por token, sem risco de cortar "ERROR" ao meio
                if "ERROR" in linha:
                    contagem["ERROR"] += 1
                elif "INFO" in linha:
                    contagem["INFO"] += 1

    # Arquivo sem "\n" final deixaria uma linha no buffer; processa aqui
    if resto:
        contagem["linhas"] += 1
        if "ERROR" in resto:
            contagem["ERROR"] += 1
        elif "INFO" in resto:
            contagem["INFO"] += 1

    pct_error = round(contagem["ERROR"] / contagem["linhas"] * 100, 1)
    return {
        "chunks": chunks,
        "caracteres": caracteres,
        "linhas": contagem["linhas"],
        "ERROR": contagem["ERROR"],
        "INFO": contagem["INFO"],
        "pct_error": pct_error,
    }


def main() -> None:
    gerar_log_exemplo(ARQUIVO, TOTAL_LINHAS_EXEMPLO)
    metricas = auditar_em_chunks(ARQUIVO, CHUNK_SIZE)

    print(f"Chunks lidos: {metricas['chunks']}")
    print(f"Caracteres totais: {metricas['caracteres']}")
    print(f"Linhas: {metricas['linhas']}")
    print(f"ERROR: {metricas['ERROR']}")
    print(f"INFO: {metricas['INFO']}")
    print(f"Proporcao ERROR: {metricas['pct_error']}%")


if __name__ == "__main__":
    main()
```

</details>
