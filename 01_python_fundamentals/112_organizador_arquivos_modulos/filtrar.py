

def filtrar_por_tipo(arquivos, extensao):
    print(f'//green/Arquivos do tipo/green //yellow/{extensao}/yellow')

    for arquivo in arquivos:
        if arquivo.endswith(extensao):
            print(f"- //yellow/{arquivo}/yellow")

