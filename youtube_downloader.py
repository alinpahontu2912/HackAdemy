from pytube import YouTube
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import os

FOLDER_NAME = ""
options = ["lowest", "highest", "mp3"]

WIDTH = 500
HEIGHT = 400

WHITE = "#ffffff"
RED = "#c4302b"
BLACK = "#282828"

TITLE = "YouTube Downloader"

def find_location():
    global FOLDER_NAME
    FOLDER_NAME = tk.filedialog.askdirectory()

class Youtube_Downloader:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("{}x{}".format(WIDTH, HEIGHT))
        self.window.configure(bg = RED)
        self.window.title(TITLE)
        
        # centering the labels
        self.window.columnconfigure(0, weight = 1)

        # added labels
        self.link_label = tk.Label(self.window, bg = RED, fg = BLACK, text = "Youtube Link", font = ("Arial", 20, "bold"))
        self.link_label.grid(column = 0, row = 0)
        self.name_label = tk.Label(self.window, bg = RED, fg = BLACK, text = "Choose File name", font = ("Arial", 20, "bold"))
        self.name_label.grid(column = 0, row = 2)
        self.path_label = tk.Label(self.window, bg = RED, fg = BLACK, text = "File Path", font = ("Arial", 20, "bold"))
        self.path_label.grid(column = 0, row = 4)
        self.path_label = tk.Label(self.window, bg = RED, fg = BLACK, text = "Download Options", font = ("Arial", 20, "bold"))
        self.path_label.grid(column = 0, row = 6)
        self.option_box = ttk.Combobox(self.window, values = options)
        self.option_box.grid(column = 0, row = 7)

        # receive input from buttons/entries
        self.link_entry = tk.Entry(master = self.window, width = 60)
        self.link_entry.grid(column = 0, row = 1)
        self.name_entry = tk.Entry(master = self.window, width = 60)
        self.name_entry.grid(column = 0, row = 3)
        self.saveEntry = tk.Button(self.window,height = 2, width = 20, bg = WHITE, fg = BLACK, text = "Choose Folder", font = ("Arial", 10, "bold"), command = find_location)
        self.saveEntry.grid(column = 0, row = 5)
        self.empty_space = tk.Label(self.window, bg = RED, fg = RED, text = "")
        self.empty_space.grid(column = 0, row = 8)
        self.download_button = tk.Button(self.window, height = 2, width = 20, text = "Download", command = self.__get_link)
        self.download_button.grid(column = 0, row = 9)

        return

    # choose format and download
    def get_format(self, link, save_path = "", save_name = ""):
        choice = self.option_box.get()
        yt = YouTube(link)

        # lowest video resolution
        if(choice == options[0]):
            select = yt.streams.filter(progressive = True).get_lowest_resolution()
            select.download(output_path = save_path, filename = save_name)
        
        # highest video resolution
        elif(choice == options[1]):
            select = yt.streams.filter(progressive = True, file_extension = 'mp4').get_highest_resolution()
            select.download(output_path = save_path, filename = save_name)
        
        elif(choice == options[2]):
            name = ""
            # if mp3 then change file extension
            select = yt.streams.filter(only_audio = True).first()
            name = select.download(output_path = save_path, filename = save_name)
            base, extension = os.path.splitext(name)
            new = base + ".mp3"
            os.rename(name, new)

    # download to wanted location
    def __get_link(self):
        link = self.link_entry.get()
        path = FOLDER_NAME
        name = self.name_entry.get()
        self.get_format(link, path, name)
        
        return

    # app loop
    def run(self):
        self.window.mainloop()
        return

def main():
    app = Youtube_Downloader()
    app.run()

if __name__ == '__main__':
    main()