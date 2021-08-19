from tkinter import *
from tkinter import ttk, filedialog
from pytube import YouTube
import os, subprocess

Folder_Name = ""
def openLoc():
    global Folder_Name
    Folder_Name = filedialog.askdirectory()
    if (len(Folder_Name) > 1):
        locErr.config(text=Folder_Name, fg="green")
    else:
        locErr.config(text="Please select a folder.", fg="red")

def downloader():
    chioce = ytChs.get()
    url = ytEntry.get()
    if (len(url) > 1):
        ytErr.config(text="")
        yt = YouTube(url)
        if (chioce == chioces[0]):
            select = yt.streams.filter(progressive=True).first()
            select.download(Folder_Name)
        elif(chioce == chioces[1]):
            select = yt.streams.filter(progressive=True, file_extension="mp4").last()
            select.download(Folder_Name)
        elif(chioce == chioces[2]): 
            select = yt.streams.filter(only_audio=True).first()
            select.download(Folder_Name)
            new_filename = f"{yt.title}.mp3"
            default_filename = select.default_filename
            subprocess.run([
                'ffmpeg',
                '-i', os.path.join(Folder_Name, default_filename),
                os.path.join(Folder_Name, new_filename)])
            os.remove(f"{Folder_Name}\\{yt.title}.mp4")
        else:
            ytErr.config(text="Try again.")
    ytErr.config(text="Download completed.")

root = Tk()
root.title("YTDownloaderV2")
root.geometry("350x400")
root.columnconfigure(0,weight=1)
ytLabel = Label(root, text="Enter the YT URL")
ytLabel.grid()
ytEntryVar = StringVar()
ytEntry = Entry(root, width=50, textvariable=ytEntryVar)
ytEntry.grid()
ytErr = Label(root, text="", fg="green", font=("jost", 10))
ytErr.grid()
svLabel = Label(root, text="Path", font=("jost", 15))
svLabel.grid()
saveEnt = Button(root, width=10, bg="red", fg="white", text="Choose a path.", command=openLoc)
saveEnt.grid()
locErr = Label(root, text="", fg="green", font=("jost", 10))
locErr.grid()
ytQual = Label(root, text="Quality", font=("jost", 15))
ytQual.grid()
chioces = ["720p", "144p", "Audio"]
ytChs = ttk.Combobox(root, value=chioces)
ytChs.grid()
dwnbutton = Button(root, text="Download", width=10, bg="red", fg="white", command=downloader)
dwnbutton.grid()
root.mainloop()
