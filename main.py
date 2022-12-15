#REQUIRES PIP INSTALL
#"pip install pytube"

import os
from pytube import YouTube
video_url = input("Enter the URL of a YouTube video: ")
yt = YouTube(video_url)
print(f"Title: {yt.title}")
print(f"Duration: {yt.length} seconds")
video_stream = yt.streams.get_highest_resolution()
print(f"Resolution: {video_stream.resolution}")
print(f"Size: {video_stream.filesize / 1024 / 1024} MB")
video_stream.download(os.getcwd())
print("Download complete!")