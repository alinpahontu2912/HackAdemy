import pytube
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

      

    def run(self):
        self.window.mainloop()
        return

def main():
    app = Youtube_Downloader()
    app.run()

if __name__ == '__main__':
    main()