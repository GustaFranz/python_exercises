# 43 - Introducao ao with open

## Objetivo

Crie servidor.log com 4 linhas de log de exemplo.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | MonitoraTI |
| **Setor** | Infraestrutura / suporte |
| **Solicitacao** | Ler arquivo de log de servidor sem esquecer de fechar o arquivo. |

## Visao do bloco (exercicios 43 a 47)

Topico **Context manager `with open`**: abrir, ler, escrever e copiar arquivos com seguranca.

| # | Nivel | Foco |
|---|-------|------|
| 43 | Leve | Introducao + ler log com `with` |
| 44 | Leve | Escrever arquivo de texto |
| 45 | Ponte | Append seguro em arquivo |
| 46 | Entrevista | Copiar com verificacao de integridade + backup |
| 47 | Entrevista | Log em chunks + auditoria ERROR/INFO |

## Enunciado

- Crie servidor.log com 4 linhas de log de exemplo.
- Leia o arquivo inteiro com `with open`.
- Exiba o conteudo e o total de linhas.

## Como executar

```bash
cd "43_introducao_with_open"
python main.py
```
