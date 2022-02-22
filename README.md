# MusicApp

Api para download de músicas direto do youtube.

Como usar: 

- Abra a pasta como projeto existente no PyCharm.
- A IDE vai pedir para configurar o Interpretador do Python e instalar as dependências.
- Execute: "uvicorn src.api:app" sem as aspas no terminal do PyCharm.
- Use o Insomnia/Postman para acessar as rotas da api.

Rotas da API:

- Rota de download: http://127.0.0.1:8000/download/
    OBS: Um link do youtube geralmente é como esse: https://www.youtube.com/watch?v=WdoXZf-FZyA
    Mas na rota de download voçê usará somente o que vem depois de "watch?" (ex: http://127.0.0.1:8000/download/v=WdoXZf-FZyA)
    
- http://127.0.0.1:8000/list (para listar as músicas baixadas)
