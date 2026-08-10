# 77 - Multi-modulo: utils e models

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
77_multimodulo_utils_models/
├── main.py
├── models.py   # criar_aluno(nome, turma) -> dict
└── utils.py    # validar_nome(nome) -> bool
```

## Enunciado

**`models.py`**
```python
def criar_aluno(nome: str, turma: str) -> dict:
    return {"nome": nome, "turma": turma}
```

**`utils.py`**
```python
def validar_nome(nome: str) -> bool:
    return len(nome.strip()) >= 3
```

No `main.py`:

1) Teste `"Ana"` — nome invalido; exiba mensagem de erro.
2) Teste `"Bruno Costa"` — nome valido; crie o aluno com `criar_aluno` e exiba o dict.

Regras:
- `models.py` nao valida.
- `utils.py` valida.
- `main.py` orquestra.

Exemplo de saida:

```
Nome invalido: Ana
Aluno cadastrado: {'nome': 'Bruno Costa', 'turma': '7A'}
```

## Como executar

```bash
cd "77_multimodulo_utils_models"
python main.py
```
