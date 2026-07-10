# 74 - Multi-modulo: calculadora de folha

## Objetivo

Montar folha de pagamento simples com 3 modulos cooperando.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | GestaoPro RH |
| **Setor** | Recursos humanos |
| **Solicitacao** | Calcular holerite simplificado para equipe de agosto. |

## Estrutura de arquivos

```
74_multimodulo_folha_pagamento/
├── main.py
├── models.py    # Funcionario(nome, salario_base)
├── calculos.py  # calcular_liquido(salario, desconto_pct)
└── relatorio.py # formatar_holerite(nome, liquido)
```

## Enunciado

- Implemente criar_funcionario, calcular_liquido e formatar_holerite.
- Em main.py gere holerite de Carla com salario 3000 e 8% de desconto.

## Como executar

```bash
cd "74_multimodulo_folha_pagamento"
python main.py
```
