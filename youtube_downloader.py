from pytube import YouTube
import tkinter as tk
from tkinter import filedialog

FOLDER_NAME = ""

WIDTH = 600
HEIGHT = 400

WHITE = "#ffffff"
RED = "#c4302b"
BLACK = "#282828"

TITLE = "YouTube Downloader"

def findLocation():
    global FOLDER_NAME
    FOLDER_NAME = tk.filedialog.askdirectory()

#donwload video
def DownloadVideo():
    choice = ytdchoices.get()
    url = ytdEntry.get()

    if(len(url)>1):
        ytdError.config(text="")
        yt = YouTube(url)

        if(choice == choices[0]):
            select = yt.streams.filter(progressive=True).first()

        elif(choice == choices[1]):
            select = yt.streams.filter(progressive=True,file_extension='mp4').last()

        elif(choice == choices[2]):
            select = yt.streams.filter(only_audio=True).first()

        else:
            ytdError.config(text="Paste Link again!!",fg="red")

class Youtube_Downloader:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("{}x{}".format(WIDTH, HEIGHT))
        self.window.configure(bg = RED)
        self.window.title(TITLE)
        
        self.link_label = tk.Label(self.window, bg = RED, fg = BLACK, text = "Download Link", font = ("Arial", 20, "bold"))
        self.link_label.grid(column = 0, row = 0)
        self.name_label = tk.Label(self.window, bg = RED, fg = BLACK, text = "Save File as", font = ("Arial", 20, "bold"))
        self.name_label.grid(column = 0, row = 1)
        self.path_label = tk.Label(self.window, bg = RED, fg = BLACK, text = "File Path", font = ("Arial", 20, "bold"))
        self.path_label.grid(column = 0, row = 2)
        self.ext_label = tk.Label(self.window, bg = RED, fg = BLACK, text = "File extension", font = ("Arial", 20, "bold"))
        self.ext_label.grid(column = 0, row = 3)

        self.link_entry = tk.Entry(master = self.window, width = 60)
        self.link_entry.grid(column = 1, row = 0)
        self.name_entry = tk.Entry(master= self.window, width = 60)
        self.name_entry.grid(column = 1, row = 1)
        self.saveEntry = tk.Button(self.window,height = 2, width=20,bg=WHITE,fg=BLACK,text="Choose Folder", font = ("Arial", 10, "bold"),command=findLocation)
        self.saveEntry.grid(column = 1, row = 2)
        self.ext_entry = tk.Entry(master = self.window, width = 60)
        self.ext_entry.grid(column = 1, row = 3)
        self.download_button = tk.Button(self.window, text = "Download", command = self.__get_link)
        self.download_button.grid(column = 1, row = 4)
        return

    def __downloader(self, link, save_path = "", save_name = "", extension = "mp4"):
        
        yt = YouTube(link)
        print(link)
        yt_stream = yt.streams.filter(progressive=True, file_extension=extension).order_by('resolution').desc().first()
        yt_stream.download(output_path = save_path, filename = save_name)

        return

  
    def __get_link(self):
        link = self.link_entry.get()
        path = FOLDER_NAME
        name = self.name_entry.get()
        ext = self.ext_entry.get()

        self.__downloader(link, path, name, ext)
        
        return

    def run(self):
        self.window.mainloop()
        return

def main():
    app = Youtube_Downloader()
    app.run()

if __name__ == '__main__':
    main()