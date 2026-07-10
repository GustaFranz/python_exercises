# 86 - Introducao a tratamento HTTP

## Objetivo

Tratar respostas simuladas 200, 404 e timeout em cliente HTTP.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | Edutech Brasil |
| **Setor** | Educacao / integracoes |
| **Solicitacao** | Consumir API de matriculas com tratamento correto de falhas. |

## Visao do bloco (exercicios 86 a 90)

Topico **API com tratamento HTTP**: lidar com sucesso, erro e indisponibilidade.

| # | Foco |
|---|------|
| 86 | Introducao + 200 vs 404 vs timeout |
| 87 | Retry simples |
| 88 | Mensagem amigavel ao usuario |
| 89 | Consulta clima com fallback |
| 90 | Cliente HTTP com cache e log de falhas |

## Enunciado

- Crie simular_api(codigo) com status 200, 404 e timeout.
- Implemente consultar_matricula tratando cada caso.
- Teste os tres cenarios.

## Como executar

```bash
cd "86_introducao_http_tratamento"
python main.py
```
