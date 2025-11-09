import yt_dlp

def hook(d):
    if d['status'] == 'downloading':
        print(f"Baixando: {d['filename']} - {d['_percent_str']}")

def download_video(url):
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',  # melhor vídeo + melhor áudio
        'merge_output_format': 'mp4',          # converte para mp4
        'progress_hooks': [hook],
        'outtmpl': '%(title)s.%(ext)s'         # nomeia o arquivo com o título do vídeo
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == '__main__':
    video_url = 'https://youtu.be/hdFJK7ZBrw0?si=sAJWkU1xkcxJeqCc' 
    download_video(video_url)
