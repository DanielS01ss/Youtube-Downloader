from tkinter import *
from tkinter.filedialog import askdirectory
import time
from tkinter import messagebox
from pytube import YouTube
from tkinter.ttk import Progressbar

class download:

    def __init__(self,location,link):
        self.video = YouTube(link,on_progress_callback=self.progress_Check)
        self.link = link
        self.folder = location
        self.second_window = Tk()
        self.second_window.geometry("300x250")
        self.progress = Progressbar(self.second_window, orient = HORIZONTAL,
              length = 100, mode = 'determinate')
        self.download_text = Label(self.second_window,text="Download progress...")
        self.download_text.pack(pady=10)
        self.progress.pack(pady=30)

    def start_download(self):
        self.video_type = self.video.streams.filter(progressive = True, file_extension = "mp4").first()
        self.title = self.video.title
        self.file_size = self.video_type.filesize
        self.video_type.download(self.folder)

    def percent(self,tem, total):
        perc = (float(tem) / float(total)) * float(100)
        return perc

    def update_progress_bar(self,perc):
        self.progress['value'] = perc
        self.second_window.update_idletasks()

    def progress_Check(self,chunk,file_handle,bytes_remaining):
        self.percent_progress = self.percent(self.file_size-bytes_remaining,self.file_size)
        self.update_progress_bar(self.percent_progress)
        if self.percent_progress == 100:
            messagebox.showinfo("Completed","Download is completed!!")
            self.second_window.destroy()


class window:

    def __init__(self):
        self.root = Tk()
        self.root.title("Youtube video downloader")
        self.root.geometry("1000x600")
        self.folder = ''

    def make_widget(self):
        self.label = Label(text="Alpha Kode Downloader")
        self.label.config(font=("Courier", 30))
        self.label.pack()
        self.image = PhotoImage(file="./Images/yt_logo_mono_light.png")
        Label(self.root,image=self.image).pack(pady=70)
        self.input_label = Label(text="Insert link here:")
        self.input_label.config(font="Verdana 20 bold")
        self.input_label.pack()
        self.entry = Entry(fg="black",bg="white",width=100)
        self.entry.pack(pady=20)
        self.folder_path_label = Label(text="Folder path:")
        self.folder_path_label.config(font=("Helvetica",20))
        self.folder_path_text = Entry(fg="white",bg="black",width=70)
        self.folder_path_text.config(state="disabled")
        self.folder_path_text.insert(0,self.folder)
        self.button_image = PhotoImage(file="./Images/add-folder-btn.png")
        self.folder_btn = Button(self.root,bg="white",image = self.button_image,command=self.handleClick)

        self.folder_path_label.pack()
        self.folder_path_text.pack()
        self.folder_btn.pack()

        self.download_image =  PhotoImage(file="./Images/donwload.png")
        self.download_btn = Button(self.root,bg="white",image = self.download_image,command=self.check_input)
        self.download_text = Label(text="Start Download:")
        self.download_text.config(font=("Helvetica",20))
        self.download_text.pack()
        self.download_btn.pack(pady=10)

    def handleClick(self):
        self.folder = askdirectory()
        self.folder_path_text.config(state="normal")
        self.folder_path_text.insert(0,self.folder)
        self.folder_path_text.config(state="disabled")

    def hello():
        print("Salut")

    def check_input(self):
        if len(self.folder)==0:
            messagebox.showerror("Error","Please select a folder before you start downloading!!")
            pass
        self.link = self.entry.get()
        if len(self.link) == 0:
            messagebox.showerror("Error","Please insert a link before starting!!!")
            pass
        try:
             video_data = YouTube(self.link)
        except:
            messagebox.showerror("Error","Invalid Link OR Problem with internet connection")
            pass

        video = download(self.folder_path_text.get(),self.link)
        video.start_download()


if __name__=="__main__":

    wnd = window()
    wnd.make_widget()


    mainloop()
