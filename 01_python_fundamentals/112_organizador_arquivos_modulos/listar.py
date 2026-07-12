
import easyansi
easyansi.activate()


def listar_arquivos(arquivos):
    print("//green/Arquivos disponíveis:/green")
    for arquivo in arquivos:
        print(f"- //yellow/{arquivo}/yellow")

