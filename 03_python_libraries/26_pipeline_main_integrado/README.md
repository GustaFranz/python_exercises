# 26 - Pipeline integrado (main)

## Demanda

A escola quer um unico comando que execute: consolidar, exportar e gerar boletins.

## Contexto do problema

Orquestracao final como main.py do boletim. Neste exercicio, `notas_fonte.csv` ja simula a tabela unificada (pos-merge); `consolidar()` deve calcular `media`, `situacao`, exportar CSV e gerar boletins HTML.

## Conceitos que voce vai usar

### `def main()`

Funcao que coordena etapas em ordem.

### `import entre funcoes locais`

Separe em funcoes: consolidar, exportar, gerar_boletins.

### `if __name__ == '__main__'`

Executa main apenas quando script e chamado diretamente.

## Tarefas

1. Crie main() que chama 3 funcoes em sequencia.
2. Use dados/notas_fonte.csv como entrada.
3. Gere saidas/consolidado.csv e boletins HTML.

## Criterios de aceite

- python main.py executa fluxo completo.
- Arquivos gerados em saidas/.
- Funcoes separadas por responsabilidade.

## Como executar

```bash
cd 26_pipeline_main_integrado
python main.py
```

## Referencia no projeto real

`main.py do projeto boletim`
