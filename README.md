
# Downloader de Lives do YouTube

Este projeto é um utilitário em Python, ideal para baixar vídeo aulas ou transmissões longas (lives).

---

## REQUISITOS
Certifique-se de que as seguintes ferramentas estão instaladas no seu sistema Linux:

- **Python 3.10+** (https://www.python.org/downloads/)
- **[uv](https://github.com/astral-sh/uv)**  (gerenciador de pacotes) OPCIONAL
- **ffmpeg**
- **yt-dlp**

---

## INSTALAÇÃO NO LINUX (via terminal)

#### Instalar o Python  (verificar versão já instalada)
python3 --version

#### Instalar as ferramentas
sudo apt update
sudo apt install ffmpeg
pip install yt-dlp

#### Instalar e configurar UV
curl -Ls https://astral.sh/uv/install.sh | bash
uv venv
uv pip install -r requirements.txt

#### Teste após configurar
python src/main.py
uv run src/main.py  (caso use o UV)

---

## INSTALAÇÃO NO WINDOWS

#### Baixe e instale o Python 3.10 ou superior pelo site oficial:
https://www.python.org/downloads/
##### - Durante a instalação, marque a opção "Add Python to PATH" antes de clicar em "Install Now"

#### Instale o yt-dlp  (cmd ou PowerShell)
pip install yt-dlp

#### Instalação do Chocolatey para o ffmpeg  (PowerShell como administrador)
Set-ExecutionPolicy Bypass -Scope Process -Force; `
[System.Net.ServicePointManager]::SecurityProtocol = `
[System.Net.ServicePointManager]::SecurityProtocol -bor 3072; `
iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))

#### Instale o ffmpeg
choco install ffmpeg

#### Teste após configurar
python src/main.py
uv run src/main.py  (caso use o UV)

---

## ENFRENTANDO PROBLEMAS

### yt-dlp ou ffmpeg não encontrado?  Isso significa que eles não estam no seu PATH.

#### No Linux, execute 'which yt-dlp' e 'which ffmpeg' para ver onde está instalado e use esse caminho no código.
- YT_DLP_PATH = "/usr/local/bin/yt-dlp" 
- FFMPEG_PATH = "/usr/bin/ffmpeg"

#### No Windows, execute no PowerShell 'Get-Command yt-dlp' 'Get-Command ffmpeg' para ver onde está instalado e use esse caminho no código.
- YT_DLP_PATH = r"C:\Users\SeuUsuario\AppData\Roaming\Python\Python310\Scripts\yt-dlp.exe"
- FFMPEG_PATH = r"C:\ProgramData\chocolatey\bin\ffmpeg.exe"

