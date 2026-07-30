# 14 - Set: auditoria de tags do catalogo

## Objetivo

Auditar cobertura de tags obrigatorias e tags orfas com conjuntos.

## Demanda

| Campo | Detalhe |
|-------|---------|
| **Empresa** | Livraria Saber |
| **Setor** | Varejo / catalogo digital |
| **Solicitacao** | Garantir filtros do e-commerce com tags obrigatorias e limpar tags orfas. |

## Enunciado

produtos = [
    {"nome": "Python Basico", "tags": ["programacao", "iniciante", "python"]},
    {"nome": "Git Pratico", "tags": ["ferramentas", "git", "iniciante"]},
    {"nome": "Logica", "tags": ["logica", "iniciante"]},
    {"nome": "SQL Pro", "tags": ["banco", "avancado", "sql"]},
]

tags_obrigatorias = {"programacao", "iniciante", "ferramentas"}
tags_proibidas = {"spam", "promocao_falsa"}

1) Una todas as tags dos produtos em um `set` (`tags_catalogo`).
2) Calcule:
   - `cobertura_ok`: intersecao com obrigatorias
   - `faltando`: obrigatorias ausentes no catalogo
   - `orfas`: tags do catalogo que nao estao em obrigatorias nem em um set
     `tags_permitidas_extra = {"python", "git", "logica", "banco", "avancado", "sql"}`
   - `bloqueadas`: intersecao com tags_proibidas (deve ficar vazia neste lote)
3) Relatorio de auditoria com totais e cada conjunto ordenado.

## Como executar

```bash
cd "14_set_tags_produtos_catalogo"
python main.py
```
