from sys import argv
import yt_dlp

if __name__ == "__main__":
    save_path = "./"

    link = argv[1]
    ydl_opts = {
        'outtmpl': f'{save_path}/%(title)s.%(ext)s',
        'format': 'bestvideo+bestaudio/best'
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(link, download=True)
        print("Title:", info_dict.get('title', None))
