from pytube import YouTube
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from tkinter import messagebox
from tkinter import *
from playsound import playsound
import os

FOLDER_NAME = ""
options = ["mp4 lowest quality", "mp4 highest highest", "mp3"]

WIDTH = 700
HEIGHT = 550

WHITE = "#ffffff"
RED = "#c4302b"
BLACK = "#282828"

TITLE = "YouTube Downloader"

download_complete_sound = 'download_complete_sound.mp3'
error_sound = 'error_sound.mp3'
help_sound = 'help_sound.mp3'

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

        # label for Youtube logo
        self.youtube = tk.PhotoImage(file='youtube.png')
        self.youtube_image = tk.Label(self.window, image = self.youtube, bd=0, highlightthickness=0)
        self.youtube_image["bg"] = RED
        self.youtube_image["border"] = "0"
        self.youtube_image.grid(column = 0, row = 2)

        # enter link label photo
        self.enter_link_label = tk.PhotoImage(file='enter_link.png')
        self.link_label = tk.Label(self.window, image = self.enter_link_label, bd=0, highlightthickness=0)
        self.link_label["bg"] = RED
        self.link_label["border"] = "0"
        self.link_label.grid(column = 0, row = 3)
    
        # enter label photo
        self.enter_name_label = tk.PhotoImage(file='enter_name.png')
        self.name_label = tk.Label(self.window, image = self.enter_name_label, bd=0, highlightthickness=0)
        self.name_label["bg"] = RED
        self.name_label["border"] = "0"
        self.name_label.grid(column = 0, row = 5)
    
        # location label with photo
        self.location_name_label = tk.PhotoImage(file='location_name.png')
        self.location_label = tk.Label(self.window, image = self.location_name_label, bd=0, highlightthickness=0)
        self.location_label["bg"] = RED
        self.location_label["border"] = "0"
        self.location_label.grid(column = 0, row = 7)
    
        # path label with photo
        self.path_name_label = tk.PhotoImage(file='path_name.png')
        self.path_label = tk.Label(self.window, image = self.path_name_label, bd=0, highlightthickness=0)
        self.path_label["bg"] = RED
        self.path_label["border"] = "0"
        self.path_label.grid(column = 0, row = 9)

        # receive input from buttons/entries

        # help button image
        self.help_btn = PhotoImage(file='help.png')
        self.help_button = tk.Button(self.window, image = self.help_btn, command = self.get_help, bd=0, highlightthickness=0)
        self.help_button["bg"] = RED
        self.help_button["border"] = "0"
        self.help_button.grid(column = 1, row = 0)
    
        # display empty space
        self.empty_space = tk.Label(self.window, bg = RED, fg = RED, text = "")
        self.empty_space.grid(column = 0, row = 1)

        # display entry for entering link
        self.link_entry = tk.Entry(master = self.window, width = 60, font=("Petendo", 11, "bold"))
        self.link_entry.grid(column = 0, row = 4)
    
        # display entry for entering file name
        self.name_entry = tk.Entry(master = self.window, width = 60, font=("Petendo", 11, "bold"))
        self.name_entry.grid(column = 0, row = 6)

        # display button image for choosing folder
        self.choose_folder_btn = PhotoImage(file='choose_folder.png')
        self.save_entry = tk.Button(self.window, image = self.choose_folder_btn, command = find_location, bd=0, highlightthickness=0)
        self.save_entry["bg"] = RED
        self.save_entry["border"] = "0"
        self.save_entry.grid(column = 0, row = 8)
    
        # display option box for entering quality of mp3 options
        self.option_box = ttk.Combobox(self.window, values = options, font=("Petendo", 11, "bold"))
        self.option_box.grid(column = 0, row = 10)

        self.empty_space = tk.Label(self.window, bg = RED, fg = RED, text = "")
        self.empty_space.grid(column = 0, row = 11)

        self.download_btn = tk.PhotoImage(file='download.png')
        self.download_button = tk.Button(self.window, image = self.download_btn, command = self.get_link, bd=0, highlightthickness=0)
        self.download_button["bg"] = RED
        self.download_button["border"] = "0"
        self.download_button.grid(column = 0, row = 12)

        return
    
    # show help message box and play sound
    def get_help(self):
        playsound(help_sound)
        messagebox.showinfo(title="Help",
        message="Hello! In order to download from YouTube, paste a valid Youtube link, choose a name for your file and a location, then choose the format and you're good to go!") 
    
    # choose format and download
    def get_format(self, link, save_path = "", save_name = ""):
        choice = self.option_box.get()

        # check if a format chioce has been made, play sound and show error box
        if len(choice) == 0:
            playsound(error_sound)
            messagebox.showerror('Required Fields', 'No Download Options selected!')
            return
        
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

    # check if the thumbnail of a  youtube link exists and if it doesn't, return False
    def is_valid_link(self, link):
        try:
            thumbnail = YouTube(link).thumbnail_url
            return True
        except Exception:
            return False

    # download to wanted location
    def get_link(self):
        link = self.link_entry.get()

        # if no link has been added, play sound and show error box
        if len(link) == 0:
            playsound(error_sound)
            messagebox.showerror('Required Fields', 'No URL address provided!')
            return

        # if the user did not introduce a youtube link, play sound and show error box
        if "youtube.com" not in link:
            playsound(error_sound)
            messagebox.showerror('Required Fields', 'Please provide Youtube Link!')
            return

        # if the user did not introduce a valid youtube link, play sound and show error box
        if self.is_valid_link(link) == False:
            playsound(error_sound)
            messagebox.showerror('Required Fields', 'Please provide a valid Youtube Link!')
            return

        # download
        path = FOLDER_NAME
        name = self.name_entry.get()
        self.get_format(link, path, name)

        # play sound after download is complete
        playsound(download_complete_sound)

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