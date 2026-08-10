# 59 - Introducao a regex e e-mail

## Objetivo

Valide e-mails com regex (padrao simples com @ e dominio).

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | MktEscolar |
| **Setor** | Marketing / comunicacao |
| **Solicitacao** | Validar e-mails de responsaveis antes de enviar campanha. |

## Visao do bloco (exercicios 59 a 63)

Topico **Regex com modulo `re`**: validar, extrair e formatar texto.

| # | Nivel | Foco |
|---|-------|------|
| 59 | Leve | Introducao + validar e-mail simples |
| 60 | Leve | Extrair numeros de texto |
| 61 | Ponte | Mascarar CPF parcial |
| 62 | Entrevista | Parsear linhas + rejeicoes + filtro turma |
| 63 | Entrevista | Limpar e padronizar telefones |

## Enunciado

1) Implemente:
```python
def validar_email(email: str) -> bool:
    # use re.fullmatch com padrao simples
```

Padrao sugerido: `r"^[\w.+-]+@[\w.-]+\.[a-zA-Z]{2,}$"`

2) Teste os 3 e-mails:
   - `"ana@escola.com"` — valido
   - `"ana.escola.com"` — invalido
   - `"bruno@mail"` — invalido

3) Exiba resultado de cada teste: `"Valido"` ou `"Invalido"`.

Exemplo de saida:

```
ana@escola.com: Valido
ana.escola.com: Invalido
bruno@mail: Invalido
```

## Como executar

```bash
cd "59_introducao_regex_email"
python main.py
```
