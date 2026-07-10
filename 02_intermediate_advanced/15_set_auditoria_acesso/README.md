# 15 - Set: auditoria de acesso

## Objetivo

Auditar permissoes com operacoes de conjuntos.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | TechSecure Solutions |
| **Setor** | Seguranca da informacao |
| **Solicitacao** | Auditar divergencia entre permissoes autorizadas e permissoes ativas. |

## Enunciado

autorizados = {"leitura", "escrita", "exportar", "admin"}
ativos = {"leitura", "escrita", "imprimir"}
Identifique:
- permissoes_ok (intersecao)
- nao_autorizadas (em ativos mas nao em autorizados)
- revogadas (em autorizados mas nao em ativos)
Exiba relatorio de auditoria.

## Como executar

```bash
cd "15_set_auditoria_acesso"
python main.py
```
