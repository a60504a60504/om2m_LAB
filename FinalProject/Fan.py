import tkinter as tk
import random
import datetime
import requests
import json
from PIL import ImageTk, Image

GAURI = "http://localhost:5000"
LevelName = ["Off","Week","Mid","Strong","Error"]
INTERVAL = 1000

def clock():
    global label,root,resultIntensity,Intensity
    
    r = requests.get(GAURI+"/GetFan")
    Intensity = int(r.content)
    resultIntensity.set("Level: "+str(LevelName[Intensity]))
    root.after(INTERVAL, clock)

    
if __name__ == '__main__':
    global label,root,resultIntensity,Intensity

    Intensity = 0
    
    root = tk.Tk()
    root.title("Fan")

    img = ImageTk.PhotoImage(Image.open("fan.jpg"))
    panel = tk.Label(root, image = img)
    panel.pack(side = "top", fill = "both", expand = "yes")

    resultIntensity = tk.StringVar()
    resultIntensity.set("Level: "+str(LevelName[Intensity]))
    label = tk.Label(root, textvariable=resultIntensity, font=("Courier", 22), width=20)
    label.pack()
    
    clock()

    root.mainloop()
