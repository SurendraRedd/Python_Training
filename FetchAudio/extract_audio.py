from pytube import YouTube

# where to save. 
# replce /home/balasundar/Downloads/ with the path where you want to store the dowload file
destination = "/FetchAudio/"
# link of the video to be downloaded
# Replace with the Youtube video link you want to download.
video_link = "https://www.youtube.com/watch?v=8bae-SpN0P4"

try:
    video = YouTube(video_link)
    # filtering the audio. File extension can be mp4/webm
    # You can see all the available streams by print(video.streams)
    audio = video.streams.filter(only_audio=True, file_extension='mp4').first()
    audio.download()
    print('Download Completed!')

except:
    print("Connection Error")  # to handle exception


