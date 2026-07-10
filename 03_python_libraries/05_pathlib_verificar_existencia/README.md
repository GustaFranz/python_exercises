# 05 - Pathlib - Verificar existencia antes de agir

## Demanda

Apos a automacao baixar um CSV do portal, o script so deve mover o arquivo se ele realmente existir na pasta Downloads. Caso contrario, deve avisar o operador e parar aquela etapa.

## Contexto do problema

No projeto real, `mover_csv_baixado()` verifica `origem.exists()` antes de chamar `shutil.move()`. Sem essa checagem, o programa quebra com erro pouco claro.

## Conceitos que voce vai usar

### `.exists()`

Retorna `True` se arquivo ou pasta existe no disco.

### `.name`

Nome do arquivo com extensao. Util em mensagens de erro.

### `return` antecipado

Sai da funcao cedo quando pre-condicao falha, evitando erro posterior.

### Simulacao local

Neste exercicio, `dados/downloads/` simula a pasta Downloads. No projeto real: `Path.home() / "Downloads"`.

## Tarefas

1. Crie a funcao `verificar_arquivo(nome_arquivo)` que:
   - Monta `origem = pasta_downloads / nome_arquivo`
   - Se nao existir, imprime `Arquivo nao encontrado: {origem}` e retorna `False`
   - Se existir, imprime `Arquivo encontrado: {origem.name}` e retorna `True`
2. Teste com `"simulado_7ano.csv"` (existe) e `"simulado_8ano.csv"` (nao existe).
3. Imprima o resultado booleano de cada teste.

## Criterios de aceite

- Primeiro teste retorna True e mostra o nome do arquivo.
- Segundo teste retorna False com mensagem clara.
- Nenhuma excecao nao tratada ao testar arquivo inexistente.

## Como executar

```bash
cd 05_pathlib_verificar_existencia
python main.py
```

## Referencia no projeto real

`src/automacao_portal.py` — funcao `mover_csv_baixado()` (linhas 49-55)
