# 75 - Introducao a projeto multi-modulo

## Objetivo

Organizar codigo em pasta src/ com dois modulos importados.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | DevEscola Labs |
| **Setor** | Educacao / formacao dev |
| **Solicitacao** | Separar calculos e formatacao em modulos para projeto piloto. |

## Visao do bloco (exercicios 75 a 79)

Topico **Mini-projeto multi-modulo**: dividir responsabilidades em arquivos Python.

| # | Foco |
|---|------|
| 75 | Introducao + src/ com 2 modulos |
| 76 | Import absoluto entre modulos |
| 77 | Separar utils e models |
| 78 | Calculadora de folha com 3 arquivos |
| 79 | Pacote analise_vendas com __init__.py |

## Estrutura de arquivos

```
75_introducao_multimodulo/
├── README.md
├── main.py
└── src/
    ├── calculos.py    # media(lista)
    └── formatacao.py  # formatar_linha(texto)
```

## Enunciado

Implemente nos modulos e importe em `main.py`:

**`src/calculos.py`**
```python
def media(lista: list) -> float:
    return sum(lista) / len(lista)
```

**`src/formatacao.py`**
```python
def formatar_linha(texto: str) -> str:
    return f"[OK] {texto.upper()}"
```

No `main.py`:

1) Importe com caminho absoluto: `from src.calculos import media` e `from src.formatacao import formatar_linha`.
2) Exiba `media([7, 8, 9])` e `formatar_linha("turma 7b")`.

Exemplo de saida:

```
Media: 8.0
[OK] TURMA 7B
```

Rode sempre da pasta do exercicio: `python main.py`.

## Como executar

```bash
cd "75_introducao_multimodulo"
python main.py
```
