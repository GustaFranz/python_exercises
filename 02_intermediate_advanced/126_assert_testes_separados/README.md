# 126 - Assert: testes separados com regras de negocio

## Objetivo

Separar implementacao e testes em modulos distintos, cobrindo casos de borda de regras comerciais.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | DevEscola Labs |
| **Setor** | Educacao / qualidade |
| **Solicitacao** | Validar modulo de desconto e pedido minimo antes de liberar checkout do bazar escolar. |

## Estrutura de arquivos

```
126_assert_testes_separados/
├── README.md
├── main.py       # orquestracao / instrucoes
├── calculos.py   # regras de negocio (implementar)
└── testes.py     # asserts de casos normais e borda (implementar)
```

## Enunciado

- Em `calculos.py`, implemente:
  - `calcular_desconto(valor, percentual)` — retorna valor com desconto aplicado
  - `validar_pedido(qtd)` — retorna `True` se quantidade valida para checkout
- Em `testes.py`, importe `calculos` e cubra casos de borda com `assert`:
  - desconto 0%, 100%, valor zero, percentual negativo, percentual acima de 100
  - pedido com qtd 0, negativa e positiva valida
- Execute `python testes.py` e exiba mensagem de sucesso ao final.
- `main.py` orienta execucao dos testes (sem duplicar logica de negocio).

## Como executar

```bash
cd "126_assert_testes_separados"
python testes.py
python main.py
```
