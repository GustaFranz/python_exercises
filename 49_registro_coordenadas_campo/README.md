# 49 - Registro de coordenadas de campo

## Objetivo

Registrar pontos geograficos de uma excursao escolar e gerar mapa interativo.

## Enunciado

Simula coleta de dados em campo: cadastra locais com latitude e longitude, salva os registros em JSON e gera um mapa HTML com os pontos visitados.

## Como executar

```bash
cd "49_registro_coordenadas_campo"
python main.py
```

Dependencias: `folium`, `easyansi`.

## Relatorio no terminal

Saida gerada apos cadastrar os pontos da excursao escolar pelo Piaui.

<p align="center">
  <img
    src="imagens/relatorio_terminal.png"
    alt="Relatorio no terminal com sete pontos geograficos cadastrados no GeoExplorer Educacional"
    width="860"
  />
</p>

<p align="center"><em>Relatorio com os pontos geograficos cadastrados e total de registros.</em></p>

## Visualizacao do mapa

Mapa interativo gerado ao final do cadastro, com todos os pontos da excursao escolar no Piaui.

<p align="center">
  <img
    src="imagens/mapa_visao_geral.png"
    alt="Mapa interativo com sete marcadores da excursao escolar pela Serra da Capivara"
    width="860"
  />
</p>

<p align="center"><em>Visao geral dos pontos cadastrados no GeoExplorer Educacional.</em></p>

Ao clicar em um marcador, o sistema exibe os detalhes do local selecionado.

<p align="center">
  <img
    src="imagens/mapa_popup_ponto.png"
    alt="Popup com informacoes do Parque Nacional da Serra da Capivara no mapa"
    width="860"
  />
</p>

<p align="center"><em>Exemplo de popup ao selecionar o Parque Nacional da Serra da Capivara.</em></p>
