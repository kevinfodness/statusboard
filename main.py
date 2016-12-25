import tkinter, time
l = tkinter.Label(text = time.strftime('%A\n%B %d %Y\n%I:%M:%S %p'))
l.pack()
l.mainloop()
