# 17 - Pandas - Exportar CSV

## Demanda

A Diretoria precisa do relatorio consolidado exportado para auditoria externa.

## Contexto do problema

Dados processados devem ser salvos em arquivo para outros setores.

## Conceitos que voce vai usar

### `.to_csv()`

Salva DataFrame em arquivo CSV.

### `index=False`

Nao grava indice numerico como coluna extra.

### `encoding='utf-8-sig'`

UTF-8 com BOM para Excel abrir acentos corretamente no Windows.

### `Path.mkdir(parents=True, exist_ok=True)`

Cria pasta de saida se nao existir.

## Tarefas

1. Leia notas_consolidadas.csv de dados/.
2. Salve copia em saidas/relatorio_final.csv.
3. Imprima caminho salvo.

## Criterios de aceite

- Arquivo criado em saidas/.
- Encoding utf-8-sig.
- Mesmo conteudo da entrada.

## Como executar

```bash
cd 17_pandas_exportar_csv
python main.py
```

## Referencia no projeto real

`src/consolidacao.py - salvar_relatorio_final()`
