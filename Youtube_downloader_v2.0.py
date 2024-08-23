import requests
import yt_dlp

def download_video(url, resolution=None):
    ydl_opts = {'format': resolution or 'best'}  # Download in specified or best quality
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def download_audio(url):
    ydl_opts = {'format': 'bestaudio/best'}  # Best quality audio
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def download_playlist(url):
    ydl_opts = {'format': 'best'}  # Download all videos in best quality
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def extract_video_info(url):
    ydl_opts = {}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=False)
        print(f"Title: {info_dict['title']}")
        print(f"Description: {info_dict['description']}")
        print(f"Views: {info_dict['view_count']}")
        print(f"Duration: {info_dict['duration']} seconds")
        print(f"Uploader: {info_dict['uploader']}")
        print(f"Upload Date: {info_dict['upload_date']}")

def download_subtitles(url, language='en'):
    ydl_opts = {'writesubtitles': True, 'subtitleslangs': [language], 'skip_download': True}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def download_thumbnail(url):
    ydl_opts = {'skip_download': True}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=False)
        thumbnail_url = info_dict.get('thumbnail')
        if thumbnail_url:
            response = requests.get(thumbnail_url)
            if response.status_code == 200:
                with open(f"{info_dict['title']}_thumbnail.jpg", "wb") as file:
                    file.write(response.content)
                print("Thumbnail downloaded successfully!")
            else:
                print("Failed to download thumbnail.")
        else:
            print("Thumbnail not found.")

link = input("Provide link here: ")

print("Choose from the following options:")
print("Press 1 to Download video")
print("Press 2 to Download audio")
print("Press 3 to Download playlist")
print("Press 4 to Extract video information")
print("Press 5 to Download subtitles")
print("Press 6 to Download thumbnail")
check = int(input(""))

if check == 1:
    res = input("Enter resolution (e.g., 720p, 1080p) or leave empty for best quality: ")
    download_video(link, resolution=res)
elif check == 2:
    download_audio(link)
elif check == 3:
    download_playlist(link)
elif check == 4:
    extract_video_info(link)
elif check == 5:
    lang = input("Enter language code for subtitles (default is 'en'): ")
    download_subtitles(link, language=lang)
elif check == 6:
    download_thumbnail(link)
else:
    print("Invalid option.")
