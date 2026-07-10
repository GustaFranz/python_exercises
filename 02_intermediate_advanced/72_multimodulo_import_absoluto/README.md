# 72 - Multi-modulo: import absoluto

## Objetivo

Usar imports absolutos entre modulos no mesmo projeto.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | GestaoPro RH |
| **Setor** | Recursos humanos |
| **Solicitacao** | Padronizar imports no sistema de ponto eletronico piloto. |

## Estrutura de arquivos

```
72_multimodulo_import_absoluto/
├── main.py
├── relogio.py      # horas_trabalhadas(entrada, saida)
└── relatorio.py    # gerar_resumo(nome, horas)
```

## Enunciado

- Implemente horas_trabalhadas em relogio.py.
- Implemente gerar_resumo em relatorio.py.
- Em main.py use imports absolutos e exiba resumo de Ana Silva.

## Como executar

```bash
cd "72_multimodulo_import_absoluto"
python main.py
```
