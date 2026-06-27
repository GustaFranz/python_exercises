"""
Adiciona moldura visual às capturas de tela do mapa para uso no README.

Objetivo: gerar PNGs com borda, cantos arredondados e sombra leve,
no estilo de documentação GitHub.
"""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter


COR_FUNDO = (246, 248, 250)      # #f6f8fa
COR_BORDA = (208, 215, 222)      # #d0d7de
COR_SOMBRA = (140, 149, 159, 90)  # sombra suave

PADDING_INTERNO = 20
ESPESSURA_BORDA = 2
RAIO_CANTO = 12
MARGEM_SOMBRA = 16
LARGURA_ALVO = 860


def caminho_windows(caminho: Path) -> Path:
    """Usa prefixo estendido no Windows para caminhos longos."""
    texto = str(caminho.resolve())
    if len(texto) >= 240 and not texto.startswith("\\\\?\\"):
        return Path("\\\\?\\" + texto)
    return caminho


def cantos_arredondados(imagem: Image.Image, raio: int) -> Image.Image:
    """Aplica máscara de cantos arredondados na imagem."""
    mascara = Image.new("L", imagem.size, 0)
    draw = ImageDraw.Draw(mascara)
    draw.rounded_rectangle((0, 0, imagem.width, imagem.height), raio, fill=255)
    resultado = imagem.copy()
    resultado.putalpha(mascara)
    return resultado


def adicionar_moldura(caminho_origem: Path, caminho_destino: Path) -> None:
    """
    Cria versão com moldura a partir de uma captura de tela.

    Parâmetros:
        caminho_origem: PNG original.
        caminho_destino: PNG final com moldura.
    """
    original = Image.open(caminho_windows(caminho_origem)).convert("RGBA")

    if original.width > LARGURA_ALVO:
        nova_altura = int(original.height * (LARGURA_ALVO / original.width))
        original = original.resize((LARGURA_ALVO, nova_altura), Image.Resampling.LANCZOS)

    conteudo = cantos_arredondados(original, RAIO_CANTO)

    largura = conteudo.width + (PADDING_INTERNO * 2) + (ESPESSURA_BORDA * 2)
    altura = conteudo.height + (PADDING_INTERNO * 2) + (ESPESSURA_BORDA * 2)

    canvas_largura = largura + (MARGEM_SOMBRA * 2)
    canvas_altura = altura + (MARGEM_SOMBRA * 2)

    canvas = Image.new("RGBA", (canvas_largura, canvas_altura), (0, 0, 0, 0))

    sombra = Image.new("RGBA", (largura, altura), COR_SOMBRA)
    sombra = cantos_arredondados(sombra, RAIO_CANTO + 2)
    sombra = sombra.filter(ImageFilter.GaussianBlur(8))
    canvas.alpha_composite(sombra, (MARGEM_SOMBRA + 4, MARGEM_SOMBRA + 6))

    moldura = Image.new("RGBA", (largura, altura), COR_FUNDO + (255,))
    draw = ImageDraw.Draw(moldura)
    draw.rounded_rectangle(
        (0, 0, largura - 1, altura - 1),
        RAIO_CANTO,
        outline=COR_BORDA,
        width=ESPESSURA_BORDA,
    )

    offset_x = MARGEM_SOMBRA + PADDING_INTERNO + ESPESSURA_BORDA
    offset_y = MARGEM_SOMBRA + PADDING_INTERNO + ESPESSURA_BORDA
    canvas.alpha_composite(moldura, (MARGEM_SOMBRA, MARGEM_SOMBRA))
    canvas.alpha_composite(conteudo, (offset_x, offset_y))

    fundo_final = Image.new("RGB", canvas.size, COR_FUNDO)
    fundo_final.paste(canvas, mask=canvas.split()[3])
    fundo_final.save(caminho_destino, "PNG", optimize=True)


def main() -> None:
    """Processa as capturas originais e grava as versões com moldura."""
    pasta = Path(__file__).resolve().parent
    pasta_originais = pasta / "originais"
    pasta_originais.mkdir(parents=True, exist_ok=True)

    pasta_assets = Path(
        r"C:\Users\mgran\.local\projects"
        r"\c-Users-mgran-OneDrive-rea-de-Trabalho-GUSTAVO-PROGRAMA-O-PROJETOS-exercicios-python"
        r"\assets"
    )

    entradas = [
        (
            "c__Users_mgran_AppData_Roaming_User_workspaceStorage_9b1cbaa6aa3909c8494eef4b560af7b6_images_image-04df2534-2e87-4564-ab0e-89c5657ba664.png",
            pasta_originais / "mapa_visao_geral_original.png",
            pasta / "mapa_visao_geral.png",
        ),
        (
            "c__Users_mgran_AppData_Roaming_User_workspaceStorage_9b1cbaa6aa3909c8494eef4b560af7b6_images_image-7ca5f66f-eb4d-47ce-97e6-3b5444cdda3b.png",
            pasta_originais / "mapa_popup_ponto_original.png",
            pasta / "mapa_popup_ponto.png",
        ),
    ]

    for nome_assets, caminho_original, caminho_final in entradas:
        if not caminho_original.exists():
            origem_assets = caminho_windows(pasta_assets / nome_assets)
            if not origem_assets.exists():
                raise FileNotFoundError(f"Arquivo não encontrado: {origem_assets}")
            caminho_original.write_bytes(origem_assets.read_bytes())

        adicionar_moldura(caminho_original, caminho_final)
        print(f"Gerado: {caminho_final.name}")


if __name__ == "__main__":
    main()
