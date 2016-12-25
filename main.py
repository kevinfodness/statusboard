import tkinter as tk
import time

def Draw():
    global timeText
    frame = tk.Frame(root, width=100, height=100, relief='solid', bd=1)
    frame.place(x=10, y=10)
    timeText = tk.Label(frame, text=time.strftime('%A\n%B %d %Y\n%I:%M:%S %p'))
    timeText.pack()

def Refresher():
    global timeText
    timeText.configure(text=time.strftime('%A\n%B %d %Y\n%I:%M:%S %p'))
    timeText.after(1000, Refresher)

root = tk.Tk()
Draw()
Refresher()
root.mainloop()
