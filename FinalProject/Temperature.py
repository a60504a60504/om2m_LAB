import tkinter as tk
import random
import datetime
import requests
import json
from PIL import ImageTk, Image

GAURI = "http://localhost:5000"


def buttonPress():
    global resultTemp,tempString,temp
    
    resultTemp.set(tempString.get()+"℃")
    temp = int(tempString.get())
    
    payload = {'data':str(temp)}
    r = requests.post(GAURI+"/UpdateTemperature", json=payload)
    
    
    
if __name__ == '__main__':
    global label,root,resultTemp,tempString,temp

    temp = 23
    
    root = tk.Tk()
    root.title("Temperature")

    img = ImageTk.PhotoImage(Image.open("temp.jpg"))
    panel = tk.Label(root, image = img)
    panel.pack(side = "top", fill = "both", expand = "yes")

    resultTemp = tk.StringVar()
    resultTemp.set(str(temp)+"℃")
    label = tk.Label(root, textvariable=resultTemp, font=("Courier", 44), width=10)
    label.pack()

    tempString = tk.StringVar()
    entryNum = tk.Entry(root, width=20, textvariable=tempString)
    entryNum.pack()   
    
    modifyButton = tk.Button(root, text="Modify", command=buttonPress)
    modifyButton.pack()  

    root.mainloop()
