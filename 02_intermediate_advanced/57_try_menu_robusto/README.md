# 57 - Try except: menu CLI robusto com log de sessao

## Objetivo

Implementar menu interativo que nao trava com entradas invalidas e registra encerramento da sessao.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | Secretaria Digital |
| **Setor** | Educacao / atendimento |
| **Solicitacao** | Painel CLI para cadastro rapido de alunos com tratamento de erro e auditoria de encerramento. |

## Enunciado

- Mantenha lista `cadastros = []` em memoria.
- Loop de menu ate o usuario sair:
  - `1` — listar cadastros numerados (ou aviso se vazio)
  - `2` — cadastrar nome (nao aceitar vazio ou so espacos)
  - `0` — sair
- Trate `ValueError` (opcao nao numerica) e entrada vazia com mensagens claras.
- Use `try/except/finally`: no `finally` do bloco principal, grave `"Sessao encerrada"` em `sessao.log` (append).
- Teste manualmente com entradas validas e invalidas.

## Como executar

```bash
cd "57_try_menu_robusto"
python main.py
```
