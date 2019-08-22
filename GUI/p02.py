import tkinter

def showlabel():
    global baseframe
    lb = tkinter.Label(baseframe, text="show yiyi")
    lb.pack()

baseframe = tkinter.Tk()

btn = tkinter.Button(baseframe, text="show label", command=showlabel)
btn.pack()

baseframe.mainloop()
