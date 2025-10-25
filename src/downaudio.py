import subprocess
from utils import ffmpeg_path, yt_dlp_path, get_output_template

def downaudio (url: str):

    output_template = get_output_template(url)

    command = [
        yt_dlp_path,
        "-f", "bestaudio/best",  # "bestaudio[ext=m4a]/best"
        "--extract-audio",
        "--audio-format", "mp3",
        "--audio-quality", "0",
        "--ffmpeg-location", ffmpeg_path,
        "-o", output_template, url]

    print("\n Baixando o áudio/música.. Por favor, aguarde!\n")

    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print("\n❌ Erro ao executar o yt-dlp. Verifique se o caminho está correto e se a URL é válida.")
        print(f"Detalhes: {e}")