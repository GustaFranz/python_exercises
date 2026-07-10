# 06 - Pathlib - Criar pastas de saida e gravar arquivo

## Demanda

A consolidacao precisa salvar o relatorio final e os boletins em pastas que podem ainda nao existir. O sistema deve criar a estrutura automaticamente e gravar arquivos de texto.

## Contexto do problema

No projeto real, `salvar_relatorio_final()` e `gerar_boletins()` usam `mkdir(parents=True, exist_ok=True)` antes de gravar. `boletins.py` usa `write_text()` para gerar HTML.

## Conceitos que voce vai usar

### `.mkdir(parents=True, exist_ok=True)`

Cria a pasta e subpastas necessarias. `exist_ok=True` nao gera erro se ja existir.

### `.write_text(conteudo, encoding="utf-8")`

Grava texto no arquivo. Substitui `open()` + `write()` + `close()`.

### Caminho de saida

`pasta_relatorios / "resumo.txt"` monta o caminho completo do arquivo de saida.

## Tarefas

1. Defina `pasta_projeto` e `pasta_relatorios = pasta_projeto / "saidas" / "relatorios"`.
2. Crie `pasta_relatorios` com `mkdir`.
3. Defina `caminho = pasta_relatorios / "resumo.txt"`.
4. Grave o texto `"Relatorio gerado com sucesso."` com `write_text`.
5. Imprima `Relatorio salvo em: {caminho}` (como no projeto real).

## Criterios de aceite

- Pasta `saidas/relatorios/` criada apos executar.
- Arquivo `resumo.txt` existe com o texto correto.
- Rodar duas vezes nao gera erro (exist_ok=True).

## Como executar

```bash
cd 06_pathlib_criar_pastas_saida
python main.py
```

## Referencia no projeto real

`src/consolidacao.py` — `salvar_relatorio_final()` (linhas 45-49)
`src/boletins.py` — `gerar_boletins()` (linhas 19, 64)
