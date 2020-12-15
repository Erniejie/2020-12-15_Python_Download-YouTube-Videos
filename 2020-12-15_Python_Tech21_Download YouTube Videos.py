##---Download YouTube Videos Using Python-TECH21 YT
# pip install first : pytube

from pytube import YouTube
link = input ("Please Enter the Video Link: ")
print("Downloading....")
YouTube(link).streams.first().download()

print("Video Downloaded Succesfully!!")
