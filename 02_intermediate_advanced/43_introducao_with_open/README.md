# 43 - Introducao ao with open

## Objetivo

Crie servidor.log com 4 linhas de log de exemplo.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | MonitoraTI |
| **Setor** | Infraestrutura / suporte |
| **Solicitacao** | Ler arquivo de log de servidor sem esquecer de fechar o arquivo. |

## Visao do bloco (exercicios 43 a 47)

Topico **Context manager `with open`**: abrir, ler, escrever e copiar arquivos com seguranca.

| # | Nivel | Foco |
|---|-------|------|
| 43 | Leve | Introducao + ler log com `with` |
| 44 | Leve | Escrever arquivo de texto |
| 45 | Ponte | Append seguro em arquivo |
| 46 | Entrevista | Copiar com verificacao de integridade + backup |
| 47 | Entrevista | Log em chunks + auditoria ERROR/INFO |

## Enunciado

1) Crie `servidor.log` no inicio do script com 4 linhas:
```
[INFO] Servidor iniciado
[INFO] Conexao aceita
[WARN] Memoria em 80%
[INFO] Backup concluido
```

2) Leia todo o conteudo com:
```python
with open("servidor.log", "r", encoding="utf-8") as f:
    ...
```

3) Exiba o conteudo na tela e a quantidade de linhas lidas.

Nao chame `.close()` manualmente — o `with` fecha automaticamente.

Exemplo de saida:

```
[INFO] Servidor iniciado
[INFO] Conexao aceita
[WARN] Memoria em 80%
[INFO] Backup concluido
Total de linhas: 4
```

## Passo a passo

1. Defina a constante `ARQUIVO = "servidor.log"` e a lista `LINHAS_LOG` com as 4 linhas do enunciado.
2. Crie o arquivo com `with open(ARQUIVO, "w", encoding="utf-8") as f:` e grave o conteudo com `f.write("\n".join(LINHAS_LOG) + "\n")`.
3. Abra o arquivo para leitura com `with open(ARQUIVO, "r", encoding="utf-8") as f:` e leia tudo com `conteudo = f.read()`.
4. Transforme o texto em lista de linhas com `linhas = conteudo.splitlines()`.
5. Exiba cada linha com um loop `for linha in linhas: print(linha)`.
6. Exiba o total com `print(f"Total de linhas: {len(linhas)}")`.
7. Nao chame `.close()` em nenhum momento — ao sair do bloco `with`, o Python fecha o arquivo sozinho.

## Como executar

```bash
cd "43_introducao_with_open"
python main.py
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

```python
# Nome do arquivo de log usado no exercicio
ARQUIVO = "servidor.log"

# Linhas de exemplo pedidas no enunciado
LINHAS_LOG = [
    "[INFO] Servidor iniciado",
    "[INFO] Conexao aceita",
    "[WARN] Memoria em 80%",
    "[INFO] Backup concluido",
]

# Modo "w" cria (ou sobrescreve) o arquivo; o with fecha sozinho ao sair do bloco
with open(ARQUIVO, "w", encoding="utf-8") as f:
    # join monta o texto com quebras de linha; o "\n" final fecha a ultima linha
    f.write("\n".join(LINHAS_LOG) + "\n")

# Modo "r" abre para leitura de texto
with open(ARQUIVO, "r", encoding="utf-8") as f:
    # read() traz o arquivo inteiro como uma unica string
    conteudo = f.read()

# splitlines separa o texto em lista de linhas, ja sem os "\n"
linhas = conteudo.splitlines()

# Exibe cada linha lida do arquivo
for linha in linhas:
    print(linha)

# Quantidade de linhas = tamanho da lista
print(f"Total de linhas: {len(linhas)}")
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

```python
"""Cria e le o log do servidor com context manager, contando as linhas."""

from pathlib import Path

# Path representa o arquivo e oferece metodos prontos de leitura/escrita
ARQUIVO_LOG = Path("servidor.log")

LINHAS_EXEMPLO = [
    "[INFO] Servidor iniciado",
    "[INFO] Conexao aceita",
    "[WARN] Memoria em 80%",
    "[INFO] Backup concluido",
]


def criar_log_exemplo(destino: Path) -> None:
    """Grava o log de exemplo; write_text usa with open internamente."""
    destino.write_text("\n".join(LINHAS_EXEMPLO) + "\n", encoding="utf-8")


def ler_linhas(origem: Path) -> list[str]:
    """Devolve as linhas do arquivo ja sem os caracteres de quebra."""
    # read_text tambem abre e fecha o arquivo com seguranca
    return origem.read_text(encoding="utf-8").splitlines()


def main() -> None:
    criar_log_exemplo(ARQUIVO_LOG)
    linhas = ler_linhas(ARQUIVO_LOG)

    # Imprime o conteudo e o total, como pede o enunciado
    print("\n".join(linhas))
    print(f"Total de linhas: {len(linhas)}")


# Permite importar as funcoes em testes sem executar o script
if __name__ == "__main__":
    main()
```

</details>
