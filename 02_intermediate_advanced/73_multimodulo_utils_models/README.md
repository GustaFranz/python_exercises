# 73 - Multi-modulo: utils e models

## Objetivo

Separar modelos de dados e funcoes utilitarias.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | Edutech Brasil |
| **Setor** | Educacao / cadastro |
| **Solicitacao** | Organizar cadastro de alunos em camadas para manutencao futura. |

## Estrutura de arquivos

```
73_multimodulo_utils_models/
├── main.py
├── models.py   # criar_aluno(nome, turma) -> dict
└── utils.py    # validar_nome(nome) -> bool
```

## Enunciado

- Implemente criar_aluno em models.py.
- Implemente validar_nome em utils.py.
- Em main.py valide e cadastre aluno valido.

## Como executar

```bash
cd "73_multimodulo_utils_models"
python main.py
```
