# 91 - Introducao a tratamento HTTP

## Objetivo

Tratar respostas simuladas 200, 404 e timeout em cliente HTTP.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | Edutech Brasil |
| **Setor** | Educacao / integracoes |
| **Solicitacao** | Consumir API de matriculas com tratamento correto de falhas. |

## Visao do bloco (exercicios 91 a 95)

Topico **API com tratamento HTTP**: lidar com sucesso, erro e indisponibilidade.

| # | Foco |
|---|------|
| 91 | Introducao + 200 vs 404 vs timeout |
| 92 | Retry simples |
| 93 | Mensagem amigavel ao usuario |
| 94 | Consulta clima com fallback |
| 95 | Cliente HTTP com cache e log de falhas |

## Enunciado

- Crie simular_api(codigo) com status 200, 404 e timeout.
- Implemente consultar_matricula tratando cada caso.
- Teste os tres cenarios.

## Como executar

```bash
cd "91_introducao_http_tratamento"
python main.py
```
