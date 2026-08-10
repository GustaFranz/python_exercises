# 82 - Argparse: subcomando simples

## Objetivo

Criar subcomandos listar e exportar na mesma CLI.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | Secretaria Digital |
| **Setor** | Educacao / secretaria |
| **Solicitacao** | Ferramenta unica para listar ou exportar alunos por turma. |

## Enunciado

Configure subcomandos com `subparsers = parser.add_subparsers(dest="comando")`:

**Subcomando `listar`**
- `--turma` (str, obrigatorio)
- Exibe: `"Listando alunos da turma {turma}"`

**Subcomando `exportar`**
- `--turma` (str, obrigatorio)
- `--arquivo` (str, obrigatorio)
- Exibe: `"Exportando turma {turma} para {arquivo}"`

Exemplos de execucao:

```bash
python main.py listar --turma 7B
python main.py exportar --turma 8A --arquivo saida.csv
```

## Como executar

```bash
cd "82_argparse_subcomando"
python main.py listar --turma 7B
```
