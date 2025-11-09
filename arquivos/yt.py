import yt_dlp
import os
import sys

def check_environment():
    print(f"Python version: {sys.version}")
    print(f"yt-dlp version: {yt_dlp.version.__version__}")
    print(f"Working directory: {os.getcwd()}")

def hook(d):
    if d['status'] == 'downloading':
        print(f"Baixando: {d['filename']} - {d['_percent_str']}")
    elif d['status'] == 'error':
        print(f"Erro durante o download: {d.get('error')}")

def download_video(url):
    if not url or not isinstance(url, str):
        print(f"URL inválida. Valor recebido: {repr(url)}")
        return
        
    ydl_opts = {
        'format': 'bestaudio[ext=m4a]/best',  # Alterado para tentar formato mais simples
        'merge_output_format': 'mp4',
        'progress_hooks': [hook],
        'outtmpl': '%(title)s.%(ext)s',
        'verbose': True  # Adiciona mais informações de debug
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            print(f"Tentando baixar URL: {repr(url)}")
            ydl.download([url])
        except Exception as e:
            print(f"Erro ao baixar: {str(e)}")
            print(f"Tipo do erro: {type(e)}")

if __name__ == '__main__':
    check_environment()
    video_url = 'https://youtu.be/oaExU0D1hB0?si=AfHmRx0n7SUO-CC3'
    print(f"URL definida: {repr(video_url)}")
    download_video(video_url)
