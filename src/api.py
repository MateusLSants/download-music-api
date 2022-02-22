import os
import shutil
from time import sleep

from fastapi import FastAPI
from pytube import YouTube

app = FastAPI()

playlist_lista = list()

@app.get("/")
def home():
    return {'nada':'mada'}

# DOWNLOAD DO .MP4 E CONVERSÃO PARA .MP3

@app.get('/download/{video_url}')
def download_video(video_url):
    linkfrom = YouTube('https://www.youtube.com/watch?'+str(video_url))
    linkfrom.streams.filter(only_audio=True)
    stream = linkfrom.streams.get_audio_only()
    out_file = stream.download()
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)

# CRIAÇÃO DE PASTA E MOVER ARQUIVOS .MP3
    
    sleep(10)
    try:
        os.mkdir('playlist')
    except:
        pass
    diretorio = os.listdir()
    for arquivo in diretorio:
        if '.mp3' in arquivo:
            try:
                shutil.move(arquivo, 'playlist')
                print( f'Arquivo {arquivo} movido com sucesso')
            except FileNotFoundError:
                print('sem arquivo há mover')

    return f'Download completo: {linkfrom.title}'
    
# LISTAGEM DA PASTA PLAYLIST

@app.get("/list")
def listar_playlist():
    playlist_lista.clear()
    diretorio = os.listdir('playlist')
    for arquivo in diretorio:
        if '.mp3' in arquivo:
            playlist_lista.append(arquivo)
    return enumerate(playlist_lista)
    