## Baixador de músicas

Script Desenvolvido em Python que realiza a busca de músicas no Youtube através da leitura de um arquivo .txt e realiza os respectivos downloads, convertendo os arquivos de audio para o formato .mp3 compatível com todos os dispositivos de reprodução.

## Tecnologias usadas:

- Pytubefix
- GoogleAPIClient
- FFMPEG

## Como usar

1 - É necessário ter um arquivo 'musicas.txt' na raíz do projeto contendo o nome de todas as músicas desejadas.

2 - É necessário ter uma chave de API para realizar requisições na API do Youtube. Tendo sua chave de API, acesse o arquivo '.env' e cole sua chave no devido campo.

- Deixo o [link](https://suporte.presence.com.br/portal/pt/kb/articles/criando-uma-chave-para-a-api-de-dados-do-youtube) de um passo a passo rápido e direto de como conseguir sua chave de API

3 - Importante alterar o caminho da pasta 'musicas' do arquivo '.env' que irá armazenar todas as músicas baixadas.

Após realizar as devidas alterações, basta executar no terminal o comando ```python main.py``` no mesmo caminho onde está o arquivo python.

### Observação:
Eu desenvolvi esse script utilizando o sistema operacional Linux, caso seu sistema seja outro, atente-se a fazer as devidas importações e alterações no código fonte, caso necessário.


