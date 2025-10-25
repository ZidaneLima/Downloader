ffmpeg_path = "/usr/bin/ffmpeg"
yt_dlp_path = "/usr/local/bin/yt-dlp"
output_template_list = "Download/%(playlist_title)s/%(title)s.%(ext)s"
output_template_unic = "Download/%(title)s.%(ext)s"

def get_output_template(url: str) -> str:
    
    if "playlist" in url or "list=" in url:
        return output_template_list
    return output_template_unic