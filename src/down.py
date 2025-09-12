import subprocess

def down(url: str):

    ffmpeg_path = "/usr/bin/ffmpeg"
    yt_dlp_path = "/usr/local/bin/yt-dlp"

    output_template = "Download/%(title)s.%(ext)s"

    command = [
        yt_dlp_path,
        "-f", "bv*+ba/best",
        "--merge-output-format", "mp4",
        "--ffmpeg-location", ffmpeg_path,
        "-o", output_template, url]

    print("\n Baixando o vídeo/live.. Por favor, aguarde!\n")
    subprocess.run(command, check=True)