# -*- coding: utf-8 -*-
"""
Created on Sun Jul 10 21:12:20 2022

@author: sante
"""

# install pytube

import tkinter as tk
import tkinter.filedialog as filedialog

from pytube import YouTube


def download_video():
    
    try:
        you_tube_link = link.get()
        save_file_name = file_name.get()
        
        you_tube = YouTube(you_tube_link)
        
        get_mp4 = you_tube.streams.filter(progressive=True,
                                          file_extension='mp4').order_by('resolution')[-1]
        
        get_mp4.download(output_path = save_directory,
                         filename = save_file_name)
        
        tk.messagebox.showinfo("Downloaded successfull",
                      save_file_name)
       
    except:
        print('Connection Error')
        
    
        
def browser_folder():

    save_directory = filedialog.asksaveasfilename(initialdir='D:/',
                                                     title ='Video Save Path',
                                                     defaultextension='.mp4',
                                                     filetypes=[("mp4 files", '*.mp4')])
    file_name.set(save_directory)
    
    
    
you_tube_link = ''
save_directory = 'D:/'
save_file_name = 'test_download.mp4'



#--------------UI Arrangement---------------
root = tk.Tk()

root.geometry('500x450')
root.resizable(False, False)
root.title('Youtube downloader')


link = tk.StringVar()
file_name = tk.StringVar()
file_name.set(save_directory)


tk.Label(root, 
         text = 'Youtube video downloader using python', 
         font='arial 15 bold ' ).place(x=50, y=100)


tk.Label(root, 
         text = 'Youtube link', 
         font='arial 10 bold ' ).place(x=20, y=150)

tk.Entry(root, 
         width = 50,
         textvariable=link).place(x = 120, y = 150)

tk.Label(root, 
         text = 'Save As', 
         font='arial 10 bold ' ).place(x=20, y=190)

tk.Entry(root, 
         width = 45,
         textvariable=file_name).place(x = 120, y = 190)


tk.Button(root, 
          text = 'Browse', 
          font='arial 8 ',
          command=browser_folder).place(x = 375, y = 187)

tk.Button(root, 
          text = 'DOWNLOAD', 
          font='arial 15 bold ',
          bg='green',
          command=download_video).place(x = 160, y = 230)


root.mainloop()