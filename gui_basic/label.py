from tkinter import *

root = Tk()
root.title("GUI")

label1 = Label(root, text="Hi!")
label1.pack()

photo = PhotoImage(file=r'gui_basic/img.png')
label2 = Label(root, image = photo)
label2.pack()

def change():
    label1.config(text='see you!')
    
    global photo2
    photo2 = PhotoImage(file = 'gui_basic/img2.png')
    label2.config(image=photo2)

btn = Button(root, text='click', command=change)
btn.pack()



root.mainloop()