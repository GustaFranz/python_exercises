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

- Implemente media(lista) em src/calculos.py.
- Implemente formatar_linha(texto) em src/formatacao.py.
- Em main.py importe e teste as duas funcoes.

## Como executar

```bash
cd "75_introducao_multimodulo"
python main.py
```
