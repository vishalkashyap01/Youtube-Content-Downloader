# YouTube video/audio/thumbnail downloader
from pytube import YouTube


# Video downloading code section
def download_vid(yt_1):
    # filter() give some specific options to download video
    videos = yt_1.streams.filter(progressive=True)
    # make together all the streams by enumerate keyword
    vid = list(enumerate(videos))
    for i in vid:
        print(i)
    # code for selecting video quality on the bases of px
    st_1 = int(input("please provide your index you want to download : "))
    if st_1 == 1 or st_1 == 2 or st_1 == 0:
        videos[st_1].download()
        print("\n successfully downloaded !")
    else:
        return


# Audio downloading code section
def download_aud(yt_2):
    audio = yt_2.streams.filter(only_audio=True)
    aud = list(enumerate(audio))
    for i in aud:
        print(i)
    st_2 = int(input("\n please type index that want to download : "))
    if st_2 <= 0:
        audio[st_2].download()
        print("\n Successfully download Audio")
    else:
        return


# thumbnail downloading code section
def download_thumbnail(yt_3):
    thumbnail = yt_3.thumbnail_url
    print("thumbnail url : ", thumbnail)

# Convert the bytes into megabytes section
def byte_to_megabyte(size):
    megabytes = size / (1024 * 1024)
    return megabytes

# Main section code
link = input("provide link here : ")
youtube_0 = YouTube(link)
size = youtube_0.streams.get_highest_resolution().filesize

# size = size of the YouTube video
# new_size = size.to_bytes()
print("Size : ", size)

size = byte_to_megabyte(size)
print("Download size : ", size, "MB")

print("Title : ", youtube_0.title)
print('\n')

print("Choose from the following options ")
print("Press 1 for Download Video ")
print("Press 2 for Download Audio ")
print("Press 3 for Download Thumbnail ")
print("Press 4 for Print Channel Name ")
check = int(input(""))

if check == 1:
    youtube_1 = YouTube(link)
    download_vid(youtube_1)
elif check == 2:
    youtube_2 = YouTube(link)
    download_aud(youtube_2)
elif check == 3:
    youtube_3 = YouTube(link)
    download_thumbnail(youtube_3)
else:
    youtube_4 = YouTube(link)


