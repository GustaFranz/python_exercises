# 44 - With open: escrever arquivo

## Objetivo

Escreva aviso_reuniao.txt com 3 linhas sobre reuniao de pais.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | Edutech Brasil |
| **Setor** | Educacao / comunicados |
| **Solicitacao** | Gerar arquivo de aviso para pais sobre reuniao de pais. |

## Enunciado

1) Escreva `aviso_reuniao.txt` com `with open` em modo `"w"` e `encoding="utf-8"`.
2) Conteudo obrigatorio (3 linhas):
```
Reuniao de pais — Turma 7B
Data: 15/08/2026 as 19h
Local: auditorio da escola
```
3) Ao final, exiba mensagem confirmando o caminho do arquivo criado.

Exemplo de saida:

```
Arquivo criado: aviso_reuniao.txt
```

## Passo a passo

1. Defina a constante `ARQUIVO = "aviso_reuniao.txt"`.
2. Crie a lista `LINHAS_AVISO` com as 3 linhas obrigatorias do enunciado.
3. Abra o arquivo com `with open(ARQUIVO, "w", encoding="utf-8") as f:` — o modo `"w"` cria o arquivo (ou sobrescreve se ja existir).
4. Grave o conteudo: use `f.write("\n".join(LINHAS_AVISO) + "\n")` ou um `f.write(linha + "\n")` por linha.
5. Fora do bloco `with`, exiba a confirmacao com `print(f"Arquivo criado: {ARQUIVO}")`.

## Como executar

```bash
cd "44_with_escrever_arquivo"
python main.py
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

```python
# Nome do arquivo de saida
ARQUIVO = "aviso_reuniao.txt"

# As 3 linhas obrigatorias do comunicado
LINHAS_AVISO = [
    "Reuniao de pais — Turma 7B",
    "Data: 15/08/2026 as 19h",
    "Local: auditorio da escola",
]

# Modo "w" cria o arquivo (ou sobrescreve); encoding="utf-8" garante acentos corretos
with open(ARQUIVO, "w", encoding="utf-8") as f:
    # join junta as linhas com "\n"; o "\n" final fecha a ultima linha
    f.write("\n".join(LINHAS_AVISO) + "\n")

# Confirmacao para o usuario saber onde o arquivo foi gravado
print(f"Arquivo criado: {ARQUIVO}")
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

```python
"""Gera o arquivo de aviso da reuniao de pais."""

from pathlib import Path

# Path deixa claro que a constante e um caminho de arquivo
ARQUIVO_AVISO = Path("aviso_reuniao.txt")

# Conteudo do comunicado definido em um unico lugar
LINHAS_AVISO = [
    "Reuniao de pais — Turma 7B",
    "Data: 15/08/2026 as 19h",
    "Local: auditorio da escola",
]


def gerar_aviso(destino: Path, linhas: list[str]) -> None:
    """Grava o aviso no destino; write_text abre e fecha o arquivo com seguranca."""
    destino.write_text("\n".join(linhas) + "\n", encoding="utf-8")


def main() -> None:
    gerar_aviso(ARQUIVO_AVISO, LINHAS_AVISO)
    # Confirmacao com o caminho gravado
    print(f"Arquivo criado: {ARQUIVO_AVISO}")


# Evita efeito colateral ao importar este modulo em testes
if __name__ == "__main__":
    main()
```

</details>
