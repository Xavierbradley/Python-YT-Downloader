# where to save
SAVE_PATH = r"C:/" #This will change based on where you would like to save the video

#lionk of the video to be downloaded

#link of the video to be downloaded.
link = "https://www.youtube.com/watch?v=-FjwUXiWfQs"

# Open link with a text file (Uncomment to run and Comment the link above out)
#link=open('links_file.txt', 'r')

for i in link:
    try:
        #object creation using Youtube which was imported at the beginning
        yt = YouTube(i)
    except:
        #to handle exception
        print("Connection Error")
    #filters out all the files with "mp4" extension
    mp4files = yt.filter("mp4")

    #get the video with the extension and resolution passed in the get() function
    d_video = yt.get(mp4files[-1].extension,mp4files[-1].resolution)
    try:
        #download the video
        d_video.download(SAVE_PATH)
    except:
        print("Some Error!")

print('Task Completed!')
