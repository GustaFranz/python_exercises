# 25 - PyAutoGUI - Coleta no portal (modo simulado)

## Demanda

O portal escolar nao tem API. A TI contratou automacao de interface para baixar CSVs.

## Contexto do problema

RPA simula cliques humanos. Modo simulado permite treinar sem calibrar coordenadas.

## Conceitos que voce vai usar

### `MODO_SIMULADO = True`

Flag para pular cliques reais e apenas demonstrar fluxo.

### `pyautogui.click() / .write()`

Simula clique e digitacao na tela.

### `time.sleep()`

Pausa entre acoes para a interface responder.

### `shutil.move()`

Move arquivo da pasta Downloads para pasta do projeto.

### `webbrowser.open()`

Abre portal no navegador.

## Tarefas

1. Implemente fluxo: abrir portal, login, download, mover CSV.
2. Use MODO_SIMULADO=True por padrao.
3. No modo simulado, copie `dados/simulado_baixado.csv` para `dados/simulados/simulado_baixado.csv`.

## Criterios de aceite

- Modo simulado funciona sem PyAutoGUI real.
- Arquivo final em destino correto.
- Fluxo documentado em comentarios.

## Como executar

```bash
cd 25_pyautogui_coleta_portal
python main.py
```

## Referencia no projeto real

`src/automacao_portal.py`
