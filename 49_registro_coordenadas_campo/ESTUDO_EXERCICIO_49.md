# Exercicio 49 — Registro de Coordenadas de Campo

**GeoExplorer Educacional** · Simulacao de excursao escolar (Serra da Capivara, PI)

---

## Objetivo do exercicio

Simular a coleta de dados geograficos em campo: cadastrar locais com latitude e longitude, exibir um relatorio no terminal, salvar os dados em JSON e gerar um mapa interativo em HTML.

---

## Contexto pedagogico

O programa representa uma atividade real de estudo de campo. O usuario registra pontos visitados (paradas, cidades, areas de observacao) com coordenadas geograficas. Ao final, os dados sao organizados, persistidos e visualizados em mapa.

---

## Codigo completo

```python
import json
import webbrowser
import os

import easyansi
import folium

easyansi.activate()


def ler_coordenada(tipo):
    while True:
        entrada = input(f"//yellow/Digite a {tipo} com sinal. Ex: -5.0892: /yellow").strip()
        entrada = entrada.replace(",", ".")

        if len(entrada) == 0:
            print("//red/Erro! A coordenada nao pode ficar vazia./red")
            continue

        if entrada[0] not in ["+", "-"]:
            print("//red/Erro! A coordenada deve comecar com + ou -./red")
            print(f"//cyan/Exemplo valido para {tipo}: -5.0892 ou +5.0892/cyan")
            continue

        try:
            valor = float(entrada)
        except ValueError:
            print("//red/Erro! Digite um numero valido para a coordenada./red")
            continue

        print(f"//cyan/Valor digitado para {tipo}: {valor}/cyan")

        confirmar = input("//blue/Esta correto? [S/N]: /blue").upper().strip()

        if confirmar in ["S", "SIM"]:
            return valor
        else:
            print("//red/Digite novamente a coordenada./red")


print("=" * 95)
print("//bold-green/GEOEXPLORER EDUCACIONAL | GUSTAVO FRANZ/bold-green")
print("=" * 95)

list_coordenadas = []

while True:
    nome = input("//cyan/Nome do local: /cyan").strip().title()

    latitude = ler_coordenada("latitude")
    longitude = ler_coordenada("longitude")

    list_coordenadas.append((nome, latitude, longitude))

    while True:
        parar = input(
            "//blue/Deseja cadastrar mais algum ponto geografico? SIM [S] / NAO [N]: /blue"
        ).upper().strip()

        if parar in ["SIM", "S", "NAO", "NAO", "N"]:
            break
        else:
            print("//red/Resposta invalida! Responda com SIM [S] ou NAO [N]./red")

    if parar in ["NAO", "NAO", "N"]:
        break


print("=" * 95)
print("//bold-green/PONTOS GEOGRAFICOS CADASTRADOS/bold-green")
print("=" * 95)

for i, (nome, latitude, longitude) in enumerate(list_coordenadas, start=1):
    print(
        f"//cyan/{i:02d}. {nome:.<25}/cyan "
        f"│ //yellow/Latitude: {latitude}/yellow "
        f"│ //magenta/Longitude: {longitude}/magenta"
    )

print("=" * 95)
print(f"//green/Total de pontos cadastrados: {len(list_coordenadas)}/green")
print("=" * 95)


pasta_atual = os.path.dirname(__file__)
caminho_json = os.path.join(pasta_atual, "dados_coordenadas.json")

dados = []

for nome, latitude, longitude in list_coordenadas:
    dados.append(
        {
            "nome": nome,
            "latitude": latitude,
            "longitude": longitude
        }
    )

with open(caminho_json, "w", encoding="utf-8") as arquivo:
    json.dump(dados, arquivo, indent=4, ensure_ascii=False)

print(f"//green/Dados salvos em: {caminho_json}/green")


if len(list_coordenadas) > 0:

    media_lat = sum(lat for _, lat, _ in list_coordenadas) / len(list_coordenadas)
    media_long = sum(long for _, _, long in list_coordenadas) / len(list_coordenadas)

    mapa = folium.Map(
        location=[media_lat, media_long],
        zoom_start=6,
        tiles="Esri.WorldImagery",
        attr="Esri World Imagery",
        control_scale=True
    )

    titulo_html = """
    <div style="...">
        <strong>GeoExplorer Educacional | Gustavo Franz</strong><br>
        <span style="font-size: 13px;">Simulacao de excursao escolar para a Serra da Capivara</span>
    </div>
    """

    mapa.get_root().html.add_child(folium.Element(titulo_html))

    coordenadas_mapa = []

    for i, (nome, latitude, longitude) in enumerate(list_coordenadas, start=1):

        coordenadas_mapa.append((latitude, longitude))

        if i == 1:
            cor = "green"
        elif i == len(list_coordenadas):
            cor = "red"
        else:
            cor = "blue"

        popup_html = f"""
        <div style="width:240px; font-family: Arial, sans-serif;">
            <h4>{i}. {nome}</h4>
            <p><b>Latitude:</b> {latitude}</p>
            <p><b>Longitude:</b> {longitude}</p>
            <p><b>Projeto:</b> GeoExplorer Educacional</p>
            <p><b>Autor:</b> Gustavo Franz</p>
        </div>
        """

        folium.Marker(
            location=[latitude, longitude],
            popup=popup_html,
            tooltip=f"{i}. {nome} (clique)",
            icon=folium.Icon(color=cor)
        ).add_to(mapa)

    mapa.fit_bounds(coordenadas_mapa)

    caminho_mapa = os.path.join(pasta_atual, "mapa_pontos.html")

    mapa.save(caminho_mapa)

    print("=" * 95)
    print("//bold-green/MAPA GERADO COM SUCESSO!/bold-green")
    print(f"//cyan/Arquivo salvo em: {caminho_mapa}/cyan")
    print("=" * 95)

    webbrowser.open(caminho_mapa)
```

> **Nota:** O codigo acima omite comentarios iniciais e o bloco CSS completo do titulo por legibilidade. O arquivo `main.py` contem a versao integral.

---

## Explicacao da funcao `ler_coordenada`

### Assinatura

```python
def ler_coordenada(tipo):
```

| Elemento | Significado |
|----------|-------------|
| `def` | Palavra-chave que define uma funcao |
| `ler_coordenada` | Nome da funcao: responsavel por ler uma coordenada valida |
| `tipo` | Parametro recebido (ex.: `"latitude"` ou `"longitude"`) usado nas mensagens ao usuario |

### O que a funcao faz

1. Repete a leitura ate receber um valor valido e confirmado.
2. Valida se o campo nao esta vazio.
3. Exige que o valor comecce com `+` ou `-`.
4. Converte o texto em numero decimal (`float`).
5. Pede confirmacao `[S/N]` antes de retornar.

### Retorno

Retorna um `float` (ex.: `-5.0892`) quando o usuario confirma com `S` ou `SIM`.

---

## Explicacao linha a linha

### Bloco 1 — Importacoes (linhas 39–46)

| Linha | Codigo | Explicacao |
|-------|--------|------------|
| 39 | `import json` | Importa modulo da biblioteca padrao para ler/gravar JSON |
| 40 | `import webbrowser` | Importa modulo para abrir URLs e arquivos no navegador |
| 41 | `import os` | Importa funcoes do sistema operacional (caminhos de arquivos) |
| 43 | `import easyansi` | Importa biblioteca externa para cores no terminal |
| 44 | `import folium` | Importa biblioteca externa para criar mapas interativos |
| 46 | `easyansi.activate()` | Ativa o processamento das marcacoes de cor no `print` |

---

### Bloco 2 — Funcao `ler_coordenada` (linhas 49–76)

| Linha | Codigo | Explicacao |
|-------|--------|------------|
| 49 | `def ler_coordenada(tipo):` | Define funcao com parametro `tipo` |
| 50 | `while True:` | Loop infinito ate um `return` encerrar a funcao |
| 51 | `entrada = input(...).strip()` | Le texto do usuario e remove espacos das pontas |
| 52 | `entrada = entrada.replace(",", ".")` | Troca virgula por ponto (padrao decimal internacional) |
| 54 | `if len(entrada) == 0:` | Verifica se o usuario deixou vazio |
| 55 | `print("//red/...")` | Exibe erro em vermelho via EasyANSI |
| 56 | `continue` | Volta ao inicio do `while` para pedir de novo |
| 58 | `if entrada[0] not in ["+", "-"]:` | Verifica o primeiro caractere |
| 59–61 | `print` + `continue` | Mostra erro e exemplo; repete a leitura |
| 63 | `try:` | Inicia bloco que tenta converter texto em numero |
| 64 | `valor = float(entrada)` | Converte string para numero decimal |
| 65 | `except ValueError:` | Captura erro se conversao falhar |
| 66–67 | `print` + `continue` | Informa erro e repete |
| 69 | `print(f"... {valor} ...")` | Mostra o valor convertido para conferencia |
| 71 | `confirmar = input(...).upper().strip()` | Le confirmacao e padroniza maiusculas |
| 73 | `if confirmar in ["S", "SIM"]:` | Aceita respostas positivas |
| 74 | `return valor` | Encerra funcao devolvendo o numero valido |
| 75–76 | `else` + `print` | Se nao confirmou, pede nova digitacao |

---

### Bloco 3 — Cabecalho e lista inicial (linhas 79–83)

| Linha | Codigo | Explicacao |
|-------|--------|------------|
| 79 | `print("=" * 95)` | Imprime linha decorativa com 95 sinais `=` |
| 80 | `print("//bold-green/GEOEXPLORER...")` | Titulo colorido do sistema |
| 81 | `print("=" * 95)` | Fecha cabecalho visual |
| 83 | `list_coordenadas = []` | Cria lista vazia que armazenara tuplas `(nome, lat, long)` |

---

### Bloco 4 — Cadastro de pontos (linhas 85–104)

| Linha | Codigo | Explicacao |
|-------|--------|------------|
| 85 | `while True:` | Loop principal de cadastro (multiplos pontos) |
| 86 | `nome = input(...).strip().title()` | Le nome, limpa espacos e capitaliza palavras |
| 88 | `latitude = ler_coordenada("latitude")` | Chama funcao para ler latitude valida |
| 89 | `longitude = ler_coordenada("longitude")` | Chama funcao para ler longitude valida |
| 91 | `list_coordenadas.append((nome, latitude, longitude))` | Adiciona tupla a lista |
| 93 | `while True:` | Loop interno para validar resposta SIM/NAO |
| 94–96 | `parar = input(...).upper().strip()` | Pergunta se deseja cadastrar mais |
| 98 | `if parar in ["SIM", "S", "NAO", "NAO", "N"]:` | Aceita variantes validas de resposta (com e sem acento) |
| 99 | `break` | Sai do loop interno (resposta valida) |
| 100–101 | `else` + `print` | Resposta invalida: repete pergunta |
| 103 | `if parar in ["NAO", "NAO", "N"]:` | Se usuario quis parar |
| 104 | `break` | Sai do loop principal de cadastro |

**Logica importante:** O loop interno so valida a resposta. O loop externo decide continuar ou encerrar o cadastro.

---

### Bloco 5 — Relatorio no terminal (linhas 107–120)

| Linha | Codigo | Explicacao |
|-------|--------|------------|
| 107–109 | `print` com titulo | Cabecalho do relatorio |
| 111 | `for i, (nome, latitude, longitude) in enumerate(..., start=1):` | Percorre lista numerando a partir de 1; desempacota tupla |
| 112–116 | `print(f"...")` | Formata linha com numero (`02d`), nome alinhado (`.<25`), lat e long coloridos |
| 118–120 | `print` totais | Linha separadora e total de pontos com `len()` |

**Formatacao usada:**

- `{i:02d}` → numero com 2 digitos e zero a esquerda (01, 02...)
- `{nome:.<25}` → nome + pontos ate completar 25 caracteres
- `│` → separador visual entre colunas

---

### Bloco 6 — Salvamento em JSON (linhas 127–144)

| Linha | Codigo | Explicacao |
|-------|--------|------------|
| 127 | `pasta_atual = os.path.dirname(__file__)` | Obtem pasta onde o script esta salvo |
| 128 | `caminho_json = os.path.join(...)` | Monta caminho completo do arquivo JSON |
| 130 | `dados = []` | Lista que recebera dicionarios |
| 132 | `for nome, latitude, longitude in list_coordenadas:` | Percorre cada tupla cadastrada |
| 133–138 | `dados.append({...})` | Converte tupla em dicionario e adiciona |
| 141 | `with open(..., "w", encoding="utf-8") as arquivo:` | Abre arquivo para escrita com UTF-8 |
| 142 | `json.dump(dados, arquivo, indent=4, ensure_ascii=False)` | Grava JSON formatado, preservando acentos |
| 144 | `print(...)` | Confirma caminho do arquivo salvo |

**Por que dicionario?** JSON trabalha bem com pares chave-valor (`"nome"`, `"latitude"`, `"longitude"`).

---

### Bloco 7 — Criacao do mapa (linhas 151–227)

| Linha | Codigo | Explicacao |
|-------|--------|------------|
| 151 | `if len(list_coordenadas) > 0:` | So gera mapa se houver pelo menos 1 ponto |
| 153 | `media_lat = sum(lat for _, lat, _ in ...) / len(...)` | Calcula media das latitudes (comprehension + sum) |
| 154 | `media_long = sum(long for _, _, long in ...) / len(...)` | Calcula media das longitudes |
| 156–162 | `mapa = folium.Map(...)` | Cria mapa centrado na media, zoom 6, satelite Esri |
| 164–182 | `titulo_html = """..."""` | String HTML/CSS para titulo fixo no topo do mapa |
| 184 | `mapa.get_root().html.add_child(folium.Element(titulo_html))` | Insere HTML personalizado no mapa |
| 186 | `coordenadas_mapa = []` | Lista para ajuste automatico de enquadramento |
| 188 | `for i, (nome, latitude, longitude) in enumerate(...):` | Percorre pontos para criar marcadores |
| 190 | `coordenadas_mapa.append((latitude, longitude))` | Guarda par lat/long para `fit_bounds` |
| 192–197 | `if/elif/else` com `cor` | Primeiro ponto verde, ultimo vermelho, demais azuis |
| 199–207 | `popup_html = f"""..."""` | HTML do popup ao clicar no marcador |
| 209–214 | `folium.Marker(...).add_to(mapa)` | Cria marcador com popup, tooltip e icone colorido |
| 216 | `mapa.fit_bounds(coordenadas_mapa)` | Ajusta zoom para mostrar todos os pontos |
| 218 | `caminho_mapa = os.path.join(...)` | Define caminho do HTML de saida |
| 220 | `mapa.save(caminho_mapa)` | Salva mapa interativo em arquivo |
| 222–225 | `print` | Mensagens de sucesso |
| 227 | `webbrowser.open(caminho_mapa)` | Abre mapa no navegador padrao |

---

## Fluxo logico do programa

```text
INICIO
  │
  ├─ Ativa cores no terminal (EasyANSI)
  │
  ├─ LOOP de cadastro
  │    ├─ Le nome do local
  │    ├─ Le latitude (funcao com validacao)
  │    ├─ Le longitude (funcao com validacao)
  │    ├─ Armazena tupla na lista
  │    └─ Pergunta se continua → SIM continua / NAO encerra
  │
  ├─ Exibe relatorio formatado no terminal
  │
  ├─ Converte lista de tuplas → lista de dicionarios → JSON
  │
  └─ Se existir ao menos 1 ponto:
       ├─ Calcula centro do mapa (media lat/long)
       ├─ Cria mapa Folium com titulo HTML
       ├─ Adiciona marcadores coloridos com popup
       ├─ Ajusta enquadramento (fit_bounds)
       ├─ Salva mapa_pontos.html
       └─ Abre no navegador
FIM
```

---

## Conhecimentos necessarios

### Python basico

| Conceito | Onde aparece |
|----------|--------------|
| Variaveis e tipos | `nome`, `latitude`, `list_coordenadas` |
| Entrada do usuario | `input()` |
| Saida formatada | `print()`, f-strings |
| Condicionais | `if`, `elif`, `else` |
| Repeticao | `while True`, `for`, `continue`, `break` |
| Funcoes | `def ler_coordenada(tipo)` |
| Listas | `list_coordenadas`, `dados`, `coordenadas_mapa` |
| Tuplas | `(nome, latitude, longitude)` |
| Dicionarios | `{"nome": ..., "latitude": ..., "longitude": ...}` |
| Tratamento de erros | `try/except ValueError` |
| Metodos de string | `.strip()`, `.replace()`, `.title()`, `.upper()` |
| Funcoes built-in | `len()`, `sum()`, `float()`, `enumerate()` |

### Python intermediario

| Conceito | Onde aparece |
|----------|--------------|
| List comprehension | `sum(lat for _, lat, _ in list_coordenadas)` |
| Desempacotamento | `(nome, latitude, longitude)` no `for` |
| Descarte com `_` | `_, lat, _` ignora campos nao usados |
| Formatacao avancada | `{i:02d}`, `{nome:.<25}` |
| Context manager | `with open(...) as arquivo` |
| Caminhos de arquivo | `__file__`, `os.path.dirname`, `os.path.join` |

---

## Bibliotecas utilizadas

### Biblioteca padrao (vem com Python)

| Modulo | Funcao principal | Como foi usado |
|--------|------------------|----------------|
| `json` | Serializacao de dados | `json.dump()` grava lista de dicionarios em `dados_coordenadas.json` |
| `webbrowser` | Abrir navegador | `webbrowser.open(caminho_mapa)` exibe o mapa HTML |
| `os` | Sistema de arquivos | `dirname(__file__)` e `join()` montam caminhos relativos ao script |

### Biblioteca externa: EasyANSI

| Item | Detalhe |
|------|---------|
| Instalacao | `pip install easyansi` (ou pacote do repositorio EasyAnsi) |
| Ativacao | `easyansi.activate()` |
| Uso | Marcacoes no texto: `//red/texto/red`, `//bold-green/texto/bold-green` |
| Objetivo | Melhorar legibilidade do terminal sem poluir o codigo com codigos ANSI manuais |

### Biblioteca externa: Folium

| Classe/Metodo | Como foi usado |
|---------------|----------------|
| `folium.Map()` | Cria mapa base com centro, zoom e camada de satelite |
| `folium.Element()` | Injeta HTML personalizado (titulo fixo) |
| `folium.Marker()` | Marca cada ponto geografico |
| `folium.Icon(color=...)` | Define cor do pin (green, blue, red) |
| `.add_to(mapa)` | Adiciona elemento ao mapa |
| `mapa.fit_bounds()` | Enquadra todos os marcadores na tela |
| `mapa.save()` | Exporta mapa interativo para `.html` |
| `mapa.get_root().html.add_child()` | Anexa HTML extra ao documento do mapa |

---

## Explicacao da logica por etapas

### Etapa 1 — Validacao robusta de entrada

A funcao `ler_coordenada` encapsula toda a logica de validacao. Isso evita repetir codigo para latitude e longitude.

**Padrao usado:** loop `while True` + `continue` para repetir + `return` para encerrar.

**Beneficio pedagogico:** separar *leitura* de *validacao* de *confirmacao* torna o codigo mais legivel e reutilizavel.

### Etapa 2 — Armazenamento em tuplas

Cada ponto e uma tupla `(nome, lat, long)`.

**Por que tupla?** Representa um registro imutavel de 3 campos relacionados. Facilita iteracao e desempacotamento.

### Etapa 3 — Dois loops aninhados no cadastro

- **Loop externo:** cadastra pontos.
- **Loop interno:** so aceita respostas validas (SIM/NAO).

Isso impede que o programa avance com entrada invalida.

### Etapa 4 — Relatorio visual no terminal

Usa formatacao alinhada para simular tabela. Combina logica (`enumerate`) com apresentacao (f-string + EasyANSI).

### Etapa 5 — Persistencia em JSON

Transforma estrutura em memoria (lista de tuplas) em formato portavel (JSON). Permite reutilizar dados em outros programas ou futuras versoes do projeto.

### Etapa 6 — Visualizacao geografica

Calcula o **centro geometrico** (media das coordenadas) para posicionar o mapa.

Usa **codigo de cores semantico** nos marcadores:

- Verde → primeiro ponto (inicio da rota)
- Vermelho → ultimo ponto (fim da rota)
- Azul → pontos intermediarios

`fit_bounds` garante que todos os pontos fiquem visiveis, independentemente da distancia entre eles.

---

## Ideias para exercicios de estudo (serie derivada)

Use este material para praticar variacoes:

1. **Validacao:** aceitar coordenadas sem sinal `+`/`-` e inferir pelo hemisferio.
2. **Estruturas:** trocar lista de tuplas por lista de dicionarios desde o cadastro.
3. **Funcoes:** extrair `salvar_json()` e `gerar_mapa()` em funcoes separadas.
4. **Arquivos:** ler pontos de um JSON existente em vez de digitar no terminal.
5. **Mapa:** usar cor unica ou cor por tipo de local (cidade, parque, area de estudo).
6. **Relatorio:** exportar relatorio em `.txt` ou `.csv`.
7. **Erros:** limitar cadastro a no maximo N pontos.
8. **Testes:** criar funcao pura que calcula media de latitude/longitude.

---

## Dependencias para executar

```bash
pip install folium easyansi
cd 49_registro_coordenadas_campo
python main.py
```

**Arquivos gerados apos execucao:**

- `dados_coordenadas.json` — dados estruturados
- `mapa_pontos.html` — mapa interativo

---

## Resumo em uma frase

Este exercicio integra **entrada validada**, **estruturas de dados**, **persistencia JSON**, **formatacao de saida** e **visualizacao web com Folium** — simulando um fluxo real de coleta e analise de dados geograficos em contexto educacional.
