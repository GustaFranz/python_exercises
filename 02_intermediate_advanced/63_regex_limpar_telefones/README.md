# 63 - Regex: limpar telefones

## Objetivo

Limpe digitos com regex e formate telefones 11 digitos como (XX) XXXXX-XXXX.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | Secretaria Digital |
| **Setor** | Educacao / cadastro |
| **Solicitacao** | Padronizar telefones de responsaveis para formato unico. |

## Enunciado

Lista suja de telefones:
```python
telefones = [
    "(11) 98765-4321",
    "11 987654321",
    "+55 11 98765-4321",
    "11987654321",
]
```

Para cada item:

1) Extraia apenas digitos com `re.sub(r"\D", "", texto)`.
2) Se tiver 11 digitos, formate como `(XX) XXXXX-XXXX`.
3) Ignore entradas com menos de 10 digitos.

Implemente `padronizar_telefone(texto: str) -> str | None` e exiba a lista de telefones formatados.

Exemplo de saida:

```
Telefones padronizados:
(11) 98765-4321
(11) 98765-4321
(11) 98765-4321
(11) 98765-4321
```

## Como executar

```bash
cd "63_regex_limpar_telefones"
python main.py
```
