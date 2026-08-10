# 108 - Heranca: sobrescrever metodo

## Objetivo

Sobrescrever metodo apresentar() em subclasses.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | Secretaria Digital |
| **Setor** | Educacao / secretaria |
| **Solicitacao** | Personalizar mensagem de boas-vindas por tipo de usuario no portal. |

## Enunciado

Crie a hierarquia com metodo `apresentar()` sobrescrito:

**`Usuario`**
- `__init__(self, nome)`
- `apresentar(self)` — retorna `"Ola, {nome}"`

**`Aluno(Usuario)`**
- `apresentar(self)` — retorna `"Aluno {nome}, bem-vindo ao portal!"`

**`Responsavel(Usuario)`**
- `apresentar(self)` — retorna `"Responsavel {nome}, acompanhe o boletim."`

No `main`, crie uma instancia de cada tipo e exiba o retorno de `apresentar()` para cada uma.

## Como executar

```bash
cd "108_heranca_sobrescrever_metodo"
python main.py
```
