# 55 - Try except: arquivo opcional

## Objetivo

Implemente carregar_config(caminho) com try/except FileNotFoundError.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | MonitoraTI |
| **Setor** | Infraestrutura / suporte |
| **Solicitacao** | Ler configuracao local se existir; caso contrario usar padrao. |

## Enunciado

1) Crie o arquivo `config.txt` com uma linha:
```
modo=producao
```

2) Implemente:
```python
def carregar_config(caminho: str) -> str:
    try:
        with open(caminho, encoding="utf-8") as f:
            return f.read().strip()
    except FileNotFoundError:
        return "modo=padrao"
```

3) Teste:
   - `carregar_config("config.txt")` — arquivo existente.
   - `carregar_config("arquivo_inexistente.txt")` — fallback.

Exemplo de saida:

```
Config: modo=producao
Config: modo=padrao
```

## Como executar

```bash
cd "55_try_arquivo_opcional"
python main.py
```
