from utils import sanitize_filename
import yt_dlp
import os

# Essa função abaixo obtém informação sobre o vídeo e faz o download em formato MP3
def downloader(link, tmp_save_path):
   with yt_dlp.YoutubeDL() as ydl:
      # Extrair informações do vídeo
      info = ydl.extract_info(link, download=False)
      title = sanitize_filename(info.get("title", "audio"))

   file_name = f"{title}"
   ydl_opts = {
      'format': 'bestaudio/best',  # Baixar a melhor qualidade de áudio
      'postprocessors': [{
         'key': 'FFmpegExtractAudio',  # Usar FFmpeg para extrair o áudio
         'preferredcodec': 'mp3',  # Formato de saída: MP3
         'preferredquality': '192',  # Qualidade do áudio
      }],
      'outtmpl': os.path.join(tmp_save_path, file_name),
   }

   # Baixar o arquivo
   with yt_dlp.YoutubeDL(ydl_opts) as ydl:
      ydl.download([link])

   return file_name