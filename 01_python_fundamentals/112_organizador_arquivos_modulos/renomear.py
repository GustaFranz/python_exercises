

def renomear_arquivo(arquivos, antigo, novo):
    if antigo in arquivos:
        indice = arquivos.index(antigo)
        arquivos[indice] = novo
        print(f'//green/Arquivo/green "//yellow/{antigo}/yellow" //green/renomeado para/green "//yellow/{novo}/yellow".')
    else:
        print("//red/Arquivo não encontrado.//red")

