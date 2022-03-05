import os
import shutil
from time import sleep
from turtle import title

from fastapi import FastAPI
from pytube import YouTube
from pytube import Playlist
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ['http://localhost:3000',
           'http://192.168.56.1:3000']

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)

path = os.getcwd()
lista_play = list()
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
    
    direct = os.getcwd() + '\\playlist\\' + linkfrom.title + '.mp3'
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
    sleep(2)
    return FileResponse(direct, media_type='application/octet-stream', filename=linkfrom.title +'.mp3')
    
# DOWNLOAD PLAYLIST

"""@app.get('/playlist/{url}')
def download_playlist(url):
    linkfrom = Playlist('https://www.youtube.com/playlist?list='+str(url))
    titulo = linkfrom.title
    try:
        os.mkdir(titulo)
    except:
        pass
    for video in linkfrom.videos:
        video.streams.first().download()"""


# LISTAGEM DA PASTA PLAYLIST

@app.get("/list")
def listar_playlist():
    playlist_lista.clear()
    diretorio = os.listdir('playlist')
    for arquivo in diretorio:
        if '.mp3' in arquivo:
            playlist_lista.append(arquivo)
    return enumerate(playlist_lista)
