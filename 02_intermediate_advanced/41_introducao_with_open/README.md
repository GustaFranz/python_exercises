# 41 - Introducao ao with open

## Objetivo

Crie servidor.log com 4 linhas de log de exemplo.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | MonitoraTI |
| **Setor** | Infraestrutura / suporte |
| **Solicitacao** | Ler arquivo de log de servidor sem esquecer de fechar o arquivo. |

## Visao do bloco (exercicios 41 a 45)

Topico **Context manager `with open`**: abrir, ler, escrever e copiar arquivos com seguranca.

| # | Foco |
|---|------|
| 41 | Introducao + ler log com `with` |
| 42 | Escrever arquivo de texto |
| 43 | Append seguro em arquivo |
| 44 | Copiar conteudo entre arquivos |
| 45 | Processar arquivo em blocos (chunks) |

## Enunciado

- Crie servidor.log com 4 linhas de log de exemplo.
- Leia o arquivo inteiro com `with open`.
- Exiba o conteudo e o total de linhas.

## Como executar

```bash
cd "41_introducao_with_open"
python main.py
```
