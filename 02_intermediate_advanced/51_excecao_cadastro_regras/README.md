# 51 - Excecao customizada: cadastro com regras

## Objetivo

Crie EmailInvalidoError e CargoInvalidoError.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | GestaoPro RH |
| **Setor** | Recursos humanos |
| **Solicitacao** | Validar cadastro de funcionario antes de inserir no sistema piloto. |

## Enunciado

1) Crie as excecoes:
```python
class EmailInvalidoError(Exception):
    pass

class CargoInvalidoError(Exception):
    pass
```

2) Implemente:
```python
def cadastrar_funcionario(nome: str, email: str, cargo: str) -> dict:
    # nome nao vazio
    # email deve conter "@"
    # cargo deve estar em ("Analista", "Suporte", "Coordenador")
    # levanta excecao especifica em cada falha
    # retorna dict do funcionario se tudo ok
```

3) Teste 3 casos:
   - Valido: `"Ana Silva"`, `"ana@empresa.com"`, `"Analista"`.
   - Email invalido: `"Bruno"`, `"bruno-email"`, `"Suporte"`.
   - Cargo invalido: `"Carla"`, `"carla@empresa.com"`, `"Diretor"`.

Use `except EmailInvalidoError` e `except CargoInvalidoError` separados.

## Como executar

```bash
cd "51_excecao_cadastro_regras"
python main.py
```
