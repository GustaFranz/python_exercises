# 89 - Logging: auditoria de importacao CSV

## Objetivo

Auditar importacao CSV com log estruturado de sucesso e rejeicao.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | GestaoPro RH |
| **Setor** | Recursos humanos |
| **Solicitacao** | Auditar importacao de funcionarios com registro de linhas rejeitadas. |

## Enunciado

Crie `funcionarios.csv` com o conteudo:

```
nome,cargo
Ana,Analista
,Suporte
Bruno,Coordenador
```

Implemente `importar_funcionarios(caminho) -> list[dict]`:

- Linha valida (nome nao vazio): `logging.info(f"Importado: {nome}")` e inclui na lista
- Linha invalida: `logging.error(f"Rejeitado linha: {linha}")` e nao inclui

Exiba ao final:

- Total importado (esperado: **2**)
- Total rejeitado (esperado: **1**)

## Como executar

```bash
cd "89_logging_auditoria_csv"
python main.py
```
