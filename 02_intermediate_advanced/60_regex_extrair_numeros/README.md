# 60 - Regex: extrair numeros

## Objetivo

Extraia todos os numeros de um texto de rastreio com re.findall.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | LogiRapida |
| **Setor** | Logistica / rastreamento |
| **Solicitacao** | Extrair codigos numericos de texto de rastreio. |

## Enunciado

Texto de rastreio:
```python
texto = "Pedido 4521 enviado em 10/07 com NF 99887"
```

1) Extraia todos os grupos de digitos com `re.findall(r"\d+", texto)`.
2) Exiba a lista de numeros encontrados.

Exemplo de saida:

```
Numeros: ['4521', '10', '07', '99887']
```

## Como executar

```bash
cd "60_regex_extrair_numeros"
python main.py
```
