# 58 - DESAFIO - Importacao robusta de leads

## Objetivo

Importar CSV/JSON com excecao customizada e try/except/finally em case de entrevista.

## Conteudos cobertos

- CSV e JSON
- Excecao customizada (`raise`)
- `try` / `except` / `finally`
- Validacao de payload

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | GrowLeads Hub |
| **Setor** | Marketing / operacoes comerciais |
| **Solicitacao** | Importar lote de leads do staging sem derrubar o job; auditar falhas. |

## Enunciado

Crie `leads.csv` com linhas validas e invalidas:
```
nome,email,idade
Ana,ana@empresa.com,28
Bruno,bruno_sem_arroba,30
Carla,carla@escola.org,-2
Diego,diego@corp.com,41
```

Checklist:

1) Defina `LeadInvalidoError(Exception)`.
2) `validar_lead(nome, email, idade)`:
   - email deve conter `@`
   - idade int entre 18 e 100
   - se invalido: `raise LeadInvalidoError` com mensagem clara
3) Leia o CSV com `with open`; para cada linha use try/except:
   - sucesso -> lista `importados`
   - falha -> lista `rejeitados` com motivo
4) No `finally` de cada linha (ou do lote), registre em `importacao.log` se processou a linha.
5) Persista `importados` em `leads_ok.json` e imprima resumo (ok / rejeitados / taxa de sucesso %).

## Como executar

```bash
cd "58_desafio_importacao_robusta"
python main.py
```
