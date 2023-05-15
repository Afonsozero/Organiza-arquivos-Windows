import os # Importando o módulo os para trabalhar com o sistema operacional
import shutil # Importando o módulo shutil para manipular arquivos e diretórios
from tkinter import *
from tkinter import filedialog
from tqdm import tqdm # Importando a biblioteca tqdm para mostrar uma barra de progresso

# Definindo as extensões de arquivos e suas respectivas pastas de destino
extensoes = {
    '.jpg': 'imagens',
    '.jpeg': 'imagens',
    '.png': 'imagens',
    '.mp4': 'videos',
    '.avi': 'videos',
    '.mkv': 'videos',
    '.mp3': 'musicas',
    '.wav': 'musicas',
}

# Criando a janela de opções
root = Tk()
root.withdraw()

# Solicitando o diretório para o usuário
dir = filedialog.askdirectory()

# Verificando se o diretório existe
if not os.path.exists(dir):
    print("Diretório não encontrado!")
else:
    # Obtendo a lista de todos os arquivos no diretório
    lista_arquivos = []
    for pasta_raiz, pastas, arquivos in os.walk(dir):
        for arquivo in arquivos:
            lista_arquivos.append(os.path.join(pasta_raiz, arquivo))

    # Percorrendo todos os arquivos e movendo para a pasta de destino correspondente
    for arquivo in tqdm(lista_arquivos):
        # Obtendo a extensão do arquivo
        extensao = os.path.splitext(arquivo)[1].lower()

        # Verificando se a extensão está na lista de extensões definidas
        if extensao in extensoes:
            # Obtendo o caminho completo do arquivo e da pasta de destino
            pasta_destino = os.path.join(dir, extensoes[extensao])

            # Criando a pasta de destino, se ela não existir ainda
            if not os.path.exists(pasta_destino):
                os.makedirs(pasta_destino)

            try:
                # Movendo o arquivo para a pasta de destino
                shutil.move(arquivo, os.path.join(pasta_destino, os.path.basename(arquivo)))
            except Exception as e:
                # Se não for possível mover o arquivo, exibir uma mensagem de erro e pular para o próximo arquivo
                print(f"Erro ao mover o arquivo {arquivo}: {str(e)}")
                continue
