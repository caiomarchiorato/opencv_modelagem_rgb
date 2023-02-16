from os import listdir

def listar_arquivos(caminho=None) :
    lista_arqs = [arq for arq in listdir(caminho)]
    return lista_arqs

if __name__ == '__main__':
    arquivos = listar_arquivos(caminho="unusual/imagens")
    print(arquivos)