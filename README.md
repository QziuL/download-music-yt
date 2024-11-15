## Download de Músicas a partir do Youtube

Script em Python que realiza leitura de um arquivo.txt com uma listagem de músicas e realiza a busca no Youtube, baixando o canal de audio do vídeo e convertendo para MP3.

Tecnologias usadas:
- Python
- Api Youtube Data V3
- pytubefix
- FFMPEG

É necessário ter uma KEY da Api do Youtube para usar e também um arquivo .txt com o nome das músicas.

Para ter a Key basta acessar o site https://console.cloud.google.com criar um projeto, ir na sessão de APIs e Serviços, selecionar o 
Youtube Data V3, ativar e criar sua credencial. Existe um limite de 100 requisições que você pode fazer por dia.

Fiz esse script para resolver as questões do tipo "Filho, baixe essas músicas para mim", 
e como eu não tenho tanta prática com Python, o código não deve estar bem estruturado xD.

Tive que usar o FFMPEG pois ao baixar o arquivo do Youtube no formato MP3, a caixinha de som não reconhecia o arquivo de áudio, provavelmente por falta de codec, 
fiz o teste realizando a conversão com o FFMPEG e verifiquei que o arquivo passava a ser reconhecido normalmente.

Performance: para baixar cerca de 27 músicas, levou +/- um minuto e meio todo o processo de pesquisar, baixar, renomear, converter.

Obs.: Quando escrevi o script, fiz usando o sistema Linux, então se for usar no Windows
vai ser necessário fazer algumas adaptações, mas nada de dificil - eu imagino.
