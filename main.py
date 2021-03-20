from tkinter import *
from tkinter.filedialog import askdirectory
import time
from tkinter import messagebox

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

    def check_input(self):
        if len(self.folder)==0:
            messagebox.showerror("Error","Please select a folder before you start downloading!!")
            pass



if __name__=="__main__":

    wnd = window()
    wnd.make_widget()

    mainloop()
