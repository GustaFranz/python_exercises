# 46 - With open: copiar arquivos com verificacao de integridade

## Objetivo

Implementar pipeline de backup local com verificacao de integridade apos a copia.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | Clinica BemViver |
| **Setor** | Saude / prontuario digital |
| **Solicitacao** | Copiar prontuario resumido para pasta backup antes de atualizacao do sistema, com auditoria de sucesso ou falha. |

## Enunciado

- Crie a pasta `backup/` (se ainda nao existir).
- Crie `prontuario_maria.txt` com pelo menos 4 linhas de resumo de consulta.
- Copie o arquivo para `backup/prontuario_maria.txt` usando apenas `with open`.
- Verifique integridade: conteudo identico **ou** mesma quantidade de linhas nos dois arquivos.
- Exiba relatorio final com status (`SUCESSO` ou `FALHA`), caminhos origem/destino e contagem de linhas.

## Como executar

```bash
cd "46_with_copiar_arquivos"
python main.py
```
