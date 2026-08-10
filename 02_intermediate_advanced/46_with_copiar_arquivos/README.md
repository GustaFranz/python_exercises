# 46 - With open: copiar arquivos com verificacao de integridade

## Objetivo

Implementar pipeline de backup local com verificacao de integridade apos a copia.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | Clinica BemViver |
| **Setor** | Saude / prontuario digital |
| **Solicitacao** | Copiar prontuario resumido para pasta backup antes de atualizacao do sistema, com auditoria de sucesso ou falha. |

## Enunciado

- Crie a pasta `backup/` (se ainda nao existir).
- Crie `prontuario_maria.txt` com pelo menos 4 linhas de resumo de consulta.
- Copie o arquivo para `backup/prontuario_maria.txt` usando apenas `with open`.
- Verifique integridade: conteudo identico **ou** mesma quantidade de linhas nos dois arquivos.
- Exiba relatorio final com status (`SUCESSO` ou `FALHA`), caminhos origem/destino e contagem de linhas.

## Passo a passo

1. Importe `os` e defina as constantes `ORIGEM = "prontuario_maria.txt"` e `DESTINO = os.path.join("backup", "prontuario_maria.txt")`.
2. Crie a lista `LINHAS_PRONTUARIO` com pelo menos 4 linhas de resumo (paciente, data, queixa, conduta).
3. Crie a pasta com `os.makedirs("backup", exist_ok=True)`.
4. Grave o arquivo de origem com `with open(ORIGEM, "w", encoding="utf-8")`.
5. Copie manualmente (sem `shutil`): abra a origem em `"r"`, leia com `f.read()`, depois abra o destino em `"w"` e grave o mesmo conteudo.
6. Verifique a integridade: rele o destino com outro `with open` e compare `conteudo_origem == conteudo_backup` (ou compare `len(...)` de `splitlines()` dos dois lados).
7. Defina `status = "SUCESSO"` se a verificacao passou; caso contrario `"FALHA"`.
8. Exiba o relatorio final: status, caminho de origem com contagem de linhas e caminho de destino com contagem de linhas.

## Como executar

```bash
cd "46_with_copiar_arquivos"
python main.py
```

## Propostas de resolucao

> Tente resolver sozinho antes de consultar. As propostas mostram como devs experientes resolveriam em empresas reais.

<details>
<summary><strong>Proposta 1 — Nivel intermediario (conteudos desta trilha)</strong></summary>

```python
import os

# Caminhos de origem e destino do backup
ORIGEM = "prontuario_maria.txt"
DESTINO = os.path.join("backup", "prontuario_maria.txt")

# Resumo de consulta com 4 linhas (dado de exemplo)
LINHAS_PRONTUARIO = [
    "Paciente: Maria Souza",
    "Data da consulta: 15/07/2026",
    "Queixa: dor de cabeca recorrente",
    "Conduta: hidratacao e retorno em 30 dias",
]

# 1) Garante que a pasta de backup existe (nao falha se ja existir)
os.makedirs("backup", exist_ok=True)

# 2) Cria o arquivo de origem com o resumo da consulta
with open(ORIGEM, "w", encoding="utf-8") as f:
    f.write("\n".join(LINHAS_PRONTUARIO) + "\n")

# 3) Copia manual: le tudo da origem...
with open(ORIGEM, "r", encoding="utf-8") as f:
    conteudo_origem = f.read()

# ...e grava exatamente o mesmo conteudo no destino
with open(DESTINO, "w", encoding="utf-8") as f:
    f.write(conteudo_origem)

# 4) Verificacao de integridade: rele o backup e compara com a origem
with open(DESTINO, "r", encoding="utf-8") as f:
    conteudo_backup = f.read()

# Comparar o conteudo inteiro ja cobre a checagem de linhas
integro = conteudo_origem == conteudo_backup
status = "SUCESSO" if integro else "FALHA"

# Contagem de linhas dos dois lados para o relatorio
linhas_origem = len(conteudo_origem.splitlines())
linhas_backup = len(conteudo_backup.splitlines())

# 5) Relatorio de auditoria do backup
print(f"Status:  {status}")
print(f"Origem:  {ORIGEM} ({linhas_origem} linhas)")
print(f"Destino: {DESTINO} ({linhas_backup} linhas)")
```

</details>

<details>
<summary><strong>Proposta 2 — Nivel profissional (mercado)</strong></summary>

```python
"""Backup de prontuario com copia manual e verificacao de integridade.

Em producao usariamos shutil.copy2; aqui a copia e manual porque o
objetivo do exercicio e praticar leitura e escrita com with open.
"""

from pathlib import Path

ORIGEM = Path("prontuario_maria.txt")
DESTINO = Path("backup") / "prontuario_maria.txt"

LINHAS_PRONTUARIO = [
    "Paciente: Maria Souza",
    "Data da consulta: 15/07/2026",
    "Queixa: dor de cabeca recorrente",
    "Conduta: hidratacao e retorno em 30 dias",
]


def criar_prontuario(destino: Path, linhas: list[str]) -> None:
    """Gera o arquivo de origem para o exercicio ser self-contained."""
    destino.write_text("\n".join(linhas) + "\n", encoding="utf-8")


def copiar(origem: Path, destino: Path) -> None:
    """Copia o conteudo da origem para o destino usando leitura/escrita manual."""
    # parents=True criaria pastas intermediarias; exist_ok evita erro se ja existir
    destino.parent.mkdir(parents=True, exist_ok=True)
    destino.write_text(origem.read_text(encoding="utf-8"), encoding="utf-8")


def verificar_integridade(origem: Path, destino: Path) -> bool:
    """Backup e integro quando o conteudo dos dois arquivos e identico."""
    return origem.read_text(encoding="utf-8") == destino.read_text(encoding="utf-8")


def main() -> None:
    criar_prontuario(ORIGEM, LINHAS_PRONTUARIO)
    copiar(ORIGEM, DESTINO)

    status = "SUCESSO" if verificar_integridade(ORIGEM, DESTINO) else "FALHA"

    # Contagens calculadas na hora do relatorio
    linhas_origem = len(ORIGEM.read_text(encoding="utf-8").splitlines())
    linhas_backup = len(DESTINO.read_text(encoding="utf-8").splitlines())

    print(f"Status:  {status}")
    print(f"Origem:  {ORIGEM} ({linhas_origem} linhas)")
    print(f"Destino: {DESTINO} ({linhas_backup} linhas)")


if __name__ == "__main__":
    main()
```

</details>
