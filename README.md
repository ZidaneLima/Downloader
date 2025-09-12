
# Downloader de Lives do YouTube

Este projeto é um utilitário em Python, criado para baixar vídeo aulas ou transmissões longas (lives) no YouTube.

---

## REQUISITOS
Certifique-se de que as seguintes ferramentas estão instaladas no seu sistema:

- **Python 3.13+** (https://www.python.org/downloads/)
- **ffmpeg** (https://github.com/FFmpeg/FFmpeg, https://www.ffmpeg.org/download.html)
- **yt-dlp** (https://github.com/yt-dlp/yt-dlp/releases, https://pypi.org/project/yt-dlp/)

---

## INSTALAÇÃO NO LINUX (via terminal Ubuntu e derivados) 

#### Instalar o Python  (verificar versão, se já estiver instalado)
*python3 --version*
**ou para instalar**
*sudo apt-get install python*

#### Instalar as ferramentas
*sudo apt update*
*sudo apt install ffmpeg*
*sudo apt install yt-dlp*

#### Teste após configurar
*python src/main.py*

---

## INSTALAÇÃO NO WINDOWS

#### Baixe e instale o Python 3.10 ou superior pelo site oficial:
*https://www.python.org/downloads/*
##### - Durante a instalação, marque a opção "Add Python to PATH" antes de clicar em "Install Now"

#### Instalar o yt-dlp  (cmd ou PowerShell)
*pip install yt-dlp*

#### Instalação do Chocolatey para o ffmpeg  (PowerShell como administrador)
*Set-ExecutionPolicy Bypass -Scope Process -Force; `
[System.Net.ServicePointManager]::SecurityProtocol = `
[System.Net.ServicePointManager]::SecurityProtocol -bor 3072; `
iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))*

#### Instalar o ffmpeg
*choco install ffmpeg*

#### Teste após configurar
*python src/main.py*

---

## ENFRENTANDO PROBLEMAS

**'yt-dlp' ou 'ffmpeg' não encontrado?** Isso significa que eles não estam no seu PATH.

#### No Linux, execute 'which yt-dlp' e 'which ffmpeg' para ver onde está instalado e cole o caminho no código.
#### Ex.:

- *YT_DLP_PATH = "/usr/local/bin/yt-dlp"*
- *FFMPEG_PATH = "/usr/bin/ffmpeg"*

#### No Windows, execute no PowerShell 'Get-Command yt-dlp' 'Get-Command ffmpeg' para ver onde está instalado e cole o caminho no código.
#### Ex.:

- *YT_DLP_PATH = r"C:\Users\SeuUsuario\AppData\Roaming\Python\Python310\Scripts\yt-dlp.exe"*
- *FFMPEG_PATH = r"C:\ProgramData\chocolatey\bin\ffmpeg.exe"*
