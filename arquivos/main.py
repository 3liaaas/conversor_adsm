import os
import sys
import yt_dlp
from tqdm import tqdm

def verificar_ffmpeg():
    """Verifica se o FFmpeg está instalado e acessível"""
    ffmpeg_paths = [
        "C:\\ffmpeg\\bin\\ffmpeg.exe",
        os.path.join(os.getenv('LOCALAPPDATA', ''), 'Microsoft', 'WinGet', 'Packages', 'ffmpeg.exe'),
        os.path.join(os.getenv('PROGRAMFILES', ''), 'ffmpeg', 'bin', 'ffmpeg.exe'),
        "ffmpeg"
    ]
    
    for path in ffmpeg_paths:
        try:
            if os.path.exists(path) or os.system(f'"{path}" -version 2>nul') == 0:
                print(f"FFmpeg encontrado em: {path}")
                return True
        except:
            continue
    return False

def criar_opcoes_download(output_path):
    """Cria as opções de configuração para o download"""
    def progress_hook(d):
        if d['status'] == 'downloading':
            print(f"Baixando: {d['_percent_str']} concluído")
        elif d['status'] == 'finished':
            print("Download completo, convertendo...")

    return {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best',
        'outtmpl': f'{output_path}/%(title)s.mp4',
        'progress_hooks': [progress_hook],
        'overwrites': True,
        'keepvideo': False,  # Não mantém arquivos de vídeo intermediários
        'no_warnings': True,
        'quiet': False,
        'verbose': False,
        'merge_output_format': 'mp4'
    }

def download_video(url, output_path='.'):
    """Realiza o download do vídeo"""
    try:
        print(f"Iniciando download do vídeo: {url}")
        ydl_opts = criar_opcoes_download(output_path)

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            try:
                info = ydl.extract_info(url, download=True)
                filename = ydl.prepare_filename(info)
                
                if os.path.exists(filename):
                    print(f"\nDownload concluído: {filename}")
                else:
                    print("\nErro: Arquivo não encontrado após download")
                
            except Exception as e:
                print(f"Erro durante o download: {str(e)}")
                return None

    except Exception as e:
        print(f"Erro na configuração: {str(e)}")
        return None

def main():
    """Função principal"""
    if not verificar_ffmpeg():
        print("\nERRO: FFmpeg não encontrado!")
        print("Execute: winget install ffmpeg")
        return

    video_url = input("URL do vídeo: ").strip()
    if not video_url:
        print("URL inválida")
        return

    download_video(video_url, '.')

if __name__ == '__main__':
    main() 