# CONTEXTO DO PROJETO (SIMULAÇÃO EDUCACIONAL)
# ------------------------------------------------------------------------------------------

#Inicialmente esse exercício era bem mais simples. A medida que fui pesquisando e executando, fui me interessando em transformar
#ele em algo maior. Acabou se tornado um exercicio prazeroso, o qual fui desenvolvendo aos poucos, observando modelos, estudando novas bibliotecas...

# ===============================================
#DESCRIÇÃO DO PROJETO
# ===============================================

# Este sistema simula uma atividade de campo realizada por alunos em uma excursão
# escolar para a região da Serra da Capivara (PI), um dos mais importantes
# patrimônios arqueológicos do Brasil.
#
# Durante essa simulação, o usuário assume o papel de um professor ou aluno
# responsável por registrar os pontos visitados ao longo da viagem, incluindo:
#
# - locais de parada durante o trajeto;
# - cidades de passagem;
# - pontos turísticos e científicos;
# - áreas de observação e estudo em campo.
#
# Para cada local, são registradas as coordenadas geográficas (latitude e longitude),
# simulando uma coleta de dados real, como ocorre em atividades de pesquisa
# científica e estudos ambientais.
#
# Ao final do processo, o sistema organiza os dados e gera um mapa interativo,
# permitindo visualizar todos os pontos registrados ao longo da excursão.
#
# Esse tipo de abordagem integra programação com um contexto educacional real,
# aproximando o desenvolvimento de software de aplicações práticas em sala de aula
# e atividades de campo.
#
# =============================================================================
# # RESOLUÇÃO DO EXERCÍCIO
# =============================================================================


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
            print("//red/Erro! A coordenada não pode ficar vazia./red")
            continue

        if entrada[0] not in ["+", "-"]:
            print("//red/Erro! A coordenada deve começar com + ou -./red")
            print(f"//cyan/Exemplo válido para {tipo}: -5.0892 ou +5.0892/cyan")
            continue

        try:
            valor = float(entrada)
        except ValueError:
            print("//red/Erro! Digite um número válido para a coordenada./red")
            continue

        print(f"//cyan/Valor digitado para {tipo}: {valor}/cyan")

        confirmar = input("//blue/Está correto? [S/N]: /blue").upper().strip()

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
            "//blue/Deseja cadastrar mais algum ponto geográfico? SIM [S] / NÃO [N]: /blue"
        ).upper().strip()

        if parar in ["SIM", "S", "NAO", "NÃO", "N"]:
            break
        else:
            print("//red/Resposta inválida! Responda com SIM [S] ou NÃO [N]./red")

    if parar in ["NAO", "NÃO", "N"]:
        break


print("=" * 95)
print("//bold-green/PONTOS GEOGRÁFICOS CADASTRADOS/bold-green")
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


# ===============================
# SALVANDO OS DADOS EM JSON
# ===============================

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


# ===============================
# CRIAÇÃO DO MAPA COM FOLIUM
# ===============================

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
    <div style="
        position: fixed;
        top: 10px;
        left: 50%;
        transform: translateX(-50%);
        z-index: 9999;
        background-color: white;
        color: #1f2937;
        padding: 10px 18px;
        border-radius: 8px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.35);
        font-family: Arial, sans-serif;
        text-align: center;
    ">
        <strong>GeoExplorer Educacional | Gustavo Franz</strong><br>
        <span style="font-size: 13px;">Simulação de excursão escolar para a Serra da Capivara</span>
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



# =============================================================================
# # APRENDIZADOS E CONSOLIDAÇÃO DE CONCEITOS
# =============================================================================

# Oportunidade de construir minha própria função para organização dos dados
# Aplicação de bibliotecas externas para enriquecimento do projeto
# Contato com integração entre diferentes tecnologias e linguagens
# Manipulação de dados estruturados com foco em contexto real
# Geração de resultado visual interativo e didático
# Aplicação prática em cenário educacional (atividade próxima da realidade escolar)
# Uso de bibliotecas: json, webbrowser, folium
# Utilização da biblioteca EasyAnsi para melhoria visual do sistema

# Link do repositório da biblioteca EasyAnsi: https://github.com/GustaFranz/easyansi
#
# 
# OBRIGADO!
# FIQUE A VONTADE PARA CONTRIBUIR COM O MEU APRENDIZADO
