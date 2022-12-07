import tkinter as tk
from tkinter import *
import pandas as pd

import pickle
from tkinter import filedialog
import cv2
from PIL import ImageTk, Image
import numpy as np

root = Tk()
root.title('PNEUMONIA DETECTION USING DEEP LEARNING')
root.configure(bg='lightgray')
root.geometry("600x390+100+150") 

#HEADING GUI
heading = tk.Label(root, text="PNEUMONIA DETECTION USING DEEP LEARNING", font= ("Times New Roman", 18), bg='lightgray', fg='darkblue')
heading.pack()



#BUTTON GUI        
#b1 = tk.Button(root, text="Real Time Evaluation",font= ("Times New Roman", 15), bg='black', fg='white')
#b1.place(x=15, y=50)



#ANOTHER BUTTON GUI
browse = tk.Button(root, text="Browse X-Ray Image",font= ("Times New Roman", 15), padx=65, pady=2, bg='darkblue', fg='white')
browse.place(x=20, y=330)

b1 = tk.Button(root, text="VGG-16",font= ("Times New Roman", 10), bg='black', padx=22, pady=5, fg='white')
b1.place(x=440, y=50)

b2 = tk.Button(root, text="ResNet",font= ("Times New Roman", 10), bg='black', padx=22, pady=5, fg='white')
b2.place(x=440, y=140)

b3 = tk.Button(root, text="Xception",font= ("Times New Roman", 10), bg='black', padx=22, pady=5, fg='white')
b3.place(x=440, y=230)

#button_quit = tk.Button(root, text="Exit",font= ("Times New Roman", 10), bg='black', padx=22, pady=5, fg='red', command=root.quit)
#button_quit.place(x=440, y=90)

root.mainloop()