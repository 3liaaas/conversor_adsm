import os
from pytube import YouTube
from tqdm import tqdm

def download_youtube_video(url, output_path='.'):
    try:
        # Create a YouTube object
        yt = YouTube(url)

        # Get the highest resolution stream available
        stream = yt.streams.get_highest_resolution()

        # Get the total file size for the progress bar
        total_size = stream.filesize

        # Define a callback function to update the progress bar
        def progress_callback(stream, chunk, bytes_remaining):
            bytes_downloaded = total_size - bytes_remaining
            progress_bar.update(len(chunk))

        # Create a progress bar
        progress_bar = tqdm(total=total_size, unit='B', unit_scale=True, desc=yt.title)

        # Register the callback function
        stream.on_progress = progress_callback

        # Download the video
        stream.download(output_path)

        # Close the progress bar
        progress_bar.close()
        print(f'Download completed: {yt.title}')

    except Exception as e:
        print(f'An error occurred: {e}')

if __name__ == '__main__':
    video_url = input("Enter the YouTube video URL: ")
    download_path = input("Enter the download path (leave blank for current directory): ") or '.'
    
    download_youtube_video(video_url, download_path)