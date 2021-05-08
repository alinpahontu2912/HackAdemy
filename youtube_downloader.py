import pytube
import tkinter as tk
import playsound

WIDTH = 600
HEIGHT = 400

WHITE = "#ffffff"
RED = "#c4302b"
BLACK = "#282828"

TITLE = "YouTube Downloader"

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


        return

    def run(self):
        self.window.mainloop()
        return

def main():
    app = Youtube_Downloader()
    app.run()

if __name__ == '__main__':
    main()