import tkinter

base = tkinter.Tk()

#负责标题
base.wm_title("label Test")

lb = tkinter.Label(base, text = "Python Label", background="green")

#给相应组件指定布局
lb.pack()

base.mainloop()

