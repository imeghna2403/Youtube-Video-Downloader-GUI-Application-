from ctypes import alignment
from tkinter import *
from pytube import YouTube

root = Tk()
root.geometry('700x350')
root.resizable(0,0)
root.title("PYTHON YOUTUBE VIDEO DOWNLOADER")
Label(root,text = 'YOUTUBE VIDEO DOWNLOADER', font ='arial 20 bold underline').pack()
link = StringVar()

img=PhotoImage(file='C:/Users/KIIT/Downloads/y1.png')
Label(root,image=img).pack()

#Label(root, text = 'Paste Link Here:', font = 'arial 15 bold').place(x= 160 , y = 60)   place(relx=0.05, rely=0.2)
Label(root, text='Enter the Youtube link:', font=("arial bold", 13)).place(x= 250 , y = 150) 
link_enter = Entry(root,justify='center', width = 70,textvariable = link).place(x = 140, y = 180)


def Downloader():     
    url =YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(root, text = 'DOWNLOAD SUCCESSFUL', font = 'arial 15',fg='dark red').place(x= 220 , y = 250)  

Button(root,justify='center',text = 'DOWNLOAD', font = 'arial 15 bold' ,bg = 'red', padx = 2, command = Downloader).place(x=270 ,y = 210)

root.mainloop()