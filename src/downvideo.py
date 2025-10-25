import subprocess
from utils import ffmpeg_path, yt_dlp_path, get_output_template

def downvideo(url: str):

    output_template = get_output_template(url)

    command = [
        yt_dlp_path,
        "-f", "bv+ba/best", # "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]"
        "--merge-output-format", "mp4",
        "--ffmpeg-location", ffmpeg_path,
        "-o", output_template, url]

    print("\n Baixando o vídeo/live.. Por favor, aguarde!\n")

    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print("\n❌ Erro ao executar o yt-dlp. Verifique se o caminho está correto e se a URL é válida.")
        print(f"Detalhes: {e}")
