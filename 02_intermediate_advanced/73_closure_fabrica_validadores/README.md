# 73 - Closure: fabrica de validadores

## Objetivo

Criar fabrica que gera validadores com min e max configuraveis.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | Clinica BemViver |
| **Setor** | Saude / triagem |
| **Solicitacao** | Validar sinais vitais com faixas diferentes por tipo de exame. |

## Enunciado

Implemente a fabrica:

```python
def criar_validador(minimo, maximo):
    def validar(valor) -> bool:
        return minimo <= valor <= maximo
    return validar
```

No `main`:

1) Crie `validar_pressao = criar_validador(90, 140)`.
2) Crie `validar_temp = criar_validador(35.0, 37.5)`.
3) Execute 4 testes e exiba resultado (`True`/`False`):
   - `validar_pressao(120)` → `True`
   - `validar_pressao(160)` → `False`
   - `validar_temp(36.8)` → `True`
   - `validar_temp(38.0)` → `False`

Exemplo de saida:

```
Pressao 120: True
Pressao 160: False
Temp 36.8: True
Temp 38.0: False
```

## Como executar

```bash
cd "73_closure_fabrica_validadores"
python main.py
```
