# 45 - With open: append seguro

## Objetivo

Arquivo rotas_dia.txt com 2 rotas iniciais.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | LogiRapida |
| **Setor** | Logistica / rastreamento |
| **Solicitacao** | Registrar novas entregas no fim do arquivo de rotas do dia. |

## Enunciado

1) Crie `rotas_dia.txt` com 2 linhas iniciais:
```
Rota 01 — Centro
Rota 02 — Zona Norte
```

2) Adicione 2 novas linhas com modo `"a"` (append):
```
Rota 03 — Zona Sul
Rota 04 — Aeroporto
```

3) Leia e exiba o arquivo completo apos o append com um segundo `with open` em modo `"r"`.

Exemplo de saida:

```
Rota 01 — Centro
Rota 02 — Zona Norte
Rota 03 — Zona Sul
Rota 04 — Aeroporto
```

## Como executar

```bash
cd "45_with_append_seguro"
python main.py
```
