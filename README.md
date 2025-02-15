## Baixador de músicas

Script Desenvolvido em Python que realiza a busca de músicas no Youtube através da leitura de um arquivo .txt e realiza os respectivos downloads, convertendo os arquivos de audio para o formato .mp3 compatível com todos os dispositivos de reprodução.

## Tecnologias e dependências necessárias:

- Pytubefix ```pip install pytubefix```
- GoogleAPIClient ```pip install google-api-python-client```
- Dotenv ```pip install python-dotenv```
- FFMPEG (nativo em sistemas linux, no windows é necessário [instalação](https://www.gyan.dev/ffmpeg/builds/))
  <br/>
  Instalando no Windows:
  <br/>
    Ao descompactar a pasta do FFmpeg, altere o seu nome para 'FFmpeg' e recorte ela para o disco 'C:'
  <br/>
    Abra o cmd e cole o seguinte comando: ```setx /m PATH "C:\ffmpeg\bin;%PATH%"``` (vai setar a pasta 'bin' nas variaveis de ambiente)
  
## Como rodar

1 - É necessário ter um arquivo 'musicas.txt' na raíz do projeto contendo o nome de todas as músicas desejadas.

2 - É necessário ter uma chave de API para realizar requisições na API do Youtube. Tendo sua chave de API, acesse o arquivo '.env' e cole sua chave no devido campo.

- Deixo o [link](https://suporte.presence.com.br/portal/pt/kb/articles/criando-uma-chave-para-a-api-de-dados-do-youtube) de um passo a passo rápido e direto de como conseguir sua chave de API

3 - Importante alterar o caminho da pasta 'musicas' do arquivo '.env' que irá armazenar todas as músicas baixadas.

4 - Por fim não esqueça de alterar o nome do arquivo '.env-example' para apenas '.env'

Após realizar as devidas alterações, basta executar no terminal o comando ```python main.py``` no mesmo caminho onde está o arquivo python.


