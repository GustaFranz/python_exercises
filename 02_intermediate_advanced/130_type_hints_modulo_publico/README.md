# 130 - Type hints: modulo publico tipado

## Objetivo

Publicar modulo de mensalidades com contrato tipado completo (padrao de API interna em entrevista).

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | FinEdu Carteira |
| **Setor** | Financeiro educacional |
| **Solicitacao** | Expor modulo de calculo de mensalidades com hints, docstrings e estrutura de retorno tipada. |

## Estrutura de arquivos

```
130_type_hints_modulo_publico/
├── README.md
├── main.py
└── mensalidades.py   # API publica tipada
```

## Enunciado

- Em `mensalidades.py`, implemente funcoes publicas com type hints completos:
  - `calcular_desconto(valor: float, percentual: float) -> float`
  - `somar_valores(valores: List[float]) -> float`
  - `resumo_mensalidades(alunos: List[Dict[str, float]]) -> Dict[str, float]`
- `resumo_mensalidades` deve retornar dict com chaves: `total`, `media`, `maior`, `menor`.
- Use `from typing import List, Dict, Optional` (Optional se aplicavel).
- Toda funcao publica deve ter docstring explicando parametros e retorno.
- `main.py` importa o modulo, processa lista de alunos e exibe resumo formatado.

## Como executar

```bash
cd "130_type_hints_modulo_publico"
python main.py
```
