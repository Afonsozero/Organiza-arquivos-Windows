import os
import shutil
from tkinter import *
from tkinter import filedialog
from tqdm import tqdm

extensoes = {
    '.jpg': 'imagens',
    '.jpeg': 'imagens',
    '.png': 'imagens',
    '.mp4': 'videos',
    '.avi': 'videos',
    '.mkv': 'videos',
    '.mp3': 'musicas',
    '.wav': 'musicas',
    '.pdf': 'documentos',
    '.rar': 'compactados',
    '.zip': 'compactados',
    '.doc': 'documentos',
    '.docx': 'documentos',
}

root = Tk()
root.withdraw()

dir = filedialog.askdirectory()

if not os.path.exists(dir):
    print("Diretório não encontrado!")
else:
    lista_arquivos = []
    for pasta_raiz, pastas, arquivos in os.walk(dir):
        for arquivo in arquivos:
            lista_arquivos.append(os.path.join(pasta_raiz, arquivo))

    for arquivo in tqdm(lista_arquivos):
        extensao = os.path.splitext(arquivo)[1].lower()

        if extensao in extensoes:
            pasta_destino = os.path.join(dir, extensoes[extensao])

            if not os.path.exists(pasta_destino):
                os.makedirs(pasta_destino)

            nome_arquivo = os.path.basename(arquivo)
            destino_arquivo = os.path.join(pasta_destino, nome_arquivo)

            # Lidar com arquivos duplicados
            if os.path.exists(destino_arquivo):
                novo_nome = nome_arquivo
                contador = 1
                while os.path.exists(destino_arquivo):
                    nome_sem_extensao = os.path.splitext(nome_arquivo)[0]
                    nova_extensao = os.path.splitext(nome_arquivo)[1]
                    novo_nome = f"{nome_sem_extensao}_{contador}{nova_extensao}"
                    destino_arquivo = os.path.join(pasta_destino, novo_nome)
                    contador += 1

                print(f"Arquivo duplicado encontrado. Renomeando para: {novo_nome}")

            try:
                shutil.move(arquivo, destino_arquivo)
            except PermissionError:
                print(f"Erro de permissão ao mover o arquivo {arquivo}")
            except Exception as e:
                print(f"Erro ao mover o arquivo {arquivo}: {str(e)}")
