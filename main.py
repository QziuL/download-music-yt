from googleapiclient.discovery import build
from pytubefix import YouTube
from dotenv import load_dotenv
import os

load_dotenv()

# API_KEY armazenada no arquivo '.env'
API_KEY = os.environ["API_KEY"]
musicas_urls = []

def buscaVideo_e_retornaUrl(search_query):
    youtube = build('youtube', 'v3', developerKey=API_KEY)
    
    # Executa uma pesquisa na API
    request = youtube.search().list(
        q=search_query,
        part='snippet',
        type='video',
        maxResults=1
    )
    response = request.execute()
    
    # Extrai o link do vídeo do primeiro resultado
    if response['items']:
        video_id = response['items'][0]['id']['videoId']
        video_url = f"https://www.youtube.com/watch?v={video_id}"
        return video_url
    else:
        print("Vídeo não encontrado.")
        return "nao_achou"

# Faz a leitura de cada linha do arquivo
# e chama a função 'buscaVideo_e_retornaUrl' 
# para cada nome de musica do arquivo, 
# armazenando o retorno da função no vetor 'musicas_urls'
with open("musicas.txt", "r") as arquivo:
    search_query = arquivo.readline()
    while search_query != "":
        url = buscaVideo_e_retornaUrl(search_query)
        if url != "nao_achou":
            musicas_urls.append(url)
        search_query = arquivo.readline()

# Busca e baixa cada URL do vetor 'musicas_urls' no
# formato 'm4a' e salva na pasta 'musicas'
for musica in musicas_urls:
    yt = YouTube(musica)
    audio = yt.streams.get_audio_only()    # pegando apenas o audio do video
    audio.download(output_path="musicas/")
    print(f"Musica baixada: {audio.default_filename}")

path = os.getenv("LOCAL_ONDE_ESTAO_AS_MUSICAS")   # pegando do '.env' o caminho completo da pasta que armazena os downloads 

# Renomeia cada musica baixada,
# trocando os espaços vazios do nome por underline
for nome_arquivo in os.listdir(path):
    if " " in nome_arquivo:
        novo_nome = nome_arquivo.replace(" ", "_")
        caminho_antigo = os.path.join(path, nome_arquivo)
        caminho_novo = os.path.join(path, novo_nome)
        
        os.rename(caminho_antigo, caminho_novo)
        print(f"Renomeado: {nome_arquivo} -> {novo_nome}")
    
    file_without_ext = os.path.splitext(novo_nome)[0]   # variavel que armazena apenas o nome sem a extensao do arquivo
    
    # Acessa a pasta onde está contido os downloads e
    # utiliza o comando de conversão dos arquivos de m4a para mp3 do FFMPEG, previamente instalado no sistema
    command_convert = f"cd musicas/ && ffmpeg -i '{file_without_ext}.m4a' '{file_without_ext}.mp3'"
    # Acessa a pasta e realiza removação do arquivo antigo (formato m4a)
    command_remove = f"cd musicas/ && rm '{file_without_ext}.m4a'"

    os.system(command_convert)
    os.system(command_remove)
    print("Musica convertida!!")
print("== Finalizado. ==")