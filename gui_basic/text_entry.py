from tkinter import *

root = Tk()
root.title('GUI')
root.geometry("640x480")

txt = Text(root, width=30, height = 5)
txt.pack()

txt.insert(END, "Please write your name.")

e = Entry(root, width=30) # for ID or passwoord, enter impossible
e.pack()
e.insert(0, "write only one sentence")

def btncmd():
    print(txt.get("1.0", END)) # 1: line 1, 0: 0th column position
    print(e.get())

    txt.delete("1.0", END)
    e.delete(0,END)

btn = Button(root, text='click', command=btncmd)
btn.pack()

root.mainloop()