# 02 - Pathlib - Raiz do projeto (parent.parent)

## Demanda

No projeto de boletim, os modulos ficam em `src/` e precisam acessar pastas como `dados/` e `saidas/` que ficam um nivel acima. Voce deve reproduzir esse padrao para localizar a raiz do projeto automaticamente.

## Contexto do problema

Se o script usa apenas `.parent`, ele aponta para `src/` e nao encontra `dados/simulados`. O projeto real sobe dois niveis com `.parent.parent`.

## Conceitos que voce vai usar

### `Path(__file__).resolve().parent.parent`

Sobe dois niveis: de `src/main.py` para a pasta raiz do exercicio (equivalente a raiz do projeto real).

### `.parent` encadeado

Cada `.parent` sobe uma pasta na arvore de diretorios.

### Comparacao com exercicio 01

No exercicio 01, `main.py` ficava na raiz do exercicio (`.parent` bastava). Aqui o script esta em `src/`, como `leitor_simulados.py` no projeto real.

## Tarefas

1. Em `src/main.py`, defina `pasta_projeto` com `Path(__file__).resolve().parent.parent`.
2. Defina `pasta_dados = pasta_projeto / "dados"`.
3. Defina `pasta_simulados = pasta_dados / "simulados"`.
4. Imprima `pasta_projeto`, `pasta_dados` e `pasta_simulados`.
5. Imprima se `pasta_simulados.exists()` (deve ser False ate voce criar a pasta, ou True se existir).

## Criterios de aceite

- `pasta_projeto` aponta para a pasta `02_pathlib_raiz_do_projeto`, nao para `src/`.
- Nenhum caminho fixo tipo `C:/Users/...` no codigo.
- O script roda com `python src/main.py` a partir da pasta do exercicio.

## Como executar

```bash
cd 02_pathlib_raiz_do_projeto
python src/main.py
```

## Referencia no projeto real

`src/leitor_simulados.py`, `src/consolidacao.py`, `src/boletins.py` (linha `pasta_projeto = Path(__file__).resolve().parent.parent`)
