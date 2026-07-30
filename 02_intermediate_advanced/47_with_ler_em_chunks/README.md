# 47 - With open: ler log em chunks e auditar tokens

## Objetivo

Processar arquivo de log grande em blocos e gerar relatorio de auditoria sem carregar tudo na memoria.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | MonitoraTI |
| **Setor** | Infraestrutura / observabilidade |
| **Solicitacao** | Auditar arquivo de acesso simulado em chunks para contagem de linhas e tokens ERROR/INFO dentro do SLA de processamento. |

## Enunciado

- Crie `acesso.log` com pelo menos 30 linhas simulando access log (mix de `INFO` e `ERROR`).
- Leia o arquivo em chunks de 128 caracteres com `read(128)` dentro de um loop (nao use `.read()` sem tamanho).
- Conte total de linhas e ocorrencias dos tokens `ERROR` e `INFO` no arquivo inteiro.
- Exiba relatorio: chunks lidos, caracteres totais, linhas, ERROR, INFO e proporcao ERROR (%).

## Como executar

```bash
cd "47_with_ler_em_chunks"
python main.py
```
