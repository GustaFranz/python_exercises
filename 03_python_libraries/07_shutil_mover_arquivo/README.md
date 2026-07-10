# 07 - Shutil - Mover arquivo baixado para pasta do projeto

## Demanda

Apos o portal baixar o CSV de simulado, a automacao deve mover o arquivo da pasta Downloads para `dados/simulados/`, substituindo versao antiga se necessario.

## Contexto do problema

`shutil.move()` transporta o arquivo (nao copia). Se o destino ja existir, o projeto real apaga com `.unlink()` antes de mover, evitando falha no Windows.

## Conceitos que voce vai usar

### `import shutil`

Biblioteca padrao para operacoes de arquivo de alto nivel.

### `shutil.move(origem, destino)`

Move arquivo ou pasta. `origem` deixa de existir apos o move.

### `.unlink()`

Apaga um arquivo. Usado quando destino ja existe.

### Fluxo do projeto real

1. `origem = pasta_downloads / nome_arquivo`
2. `destino = pasta_simulados / nome_arquivo`
3. Verificar `origem.exists()`
4. Se `destino.exists()`, `destino.unlink()`
5. `shutil.move(origem, destino)`

Neste exercicio, `dados/downloads/` simula Downloads.

## Tarefas

1. Implemente `mover_csv_baixado(nome_arquivo)` com o fluxo acima.
2. Chame com `"simulado_7ano.csv"`.
3. Confirme que o arquivo sumiu de `downloads/` e apareceu em `simulados/`.
4. Imprima `Arquivo movido para: {destino}`.

## Criterios de aceite

- Arquivo movido (nao copiado) para `dados/simulados/`.
- Funcao trata origem inexistente com mensagem, sem quebrar.
- Se executar duas vezes seguidas, segunda chamada avisa que origem nao existe.

## Como executar

```bash
cd 07_shutil_mover_arquivo
python main.py
```

Depois, copie manualmente o CSV de volta para `dados/downloads/` se quiser repetir o teste.

## Referencia no projeto real

`src/automacao_portal.py` — funcao `mover_csv_baixado()` (linhas 49-61)
