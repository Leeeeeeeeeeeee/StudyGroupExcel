from tkinter import *
l=[]
def f(e):
    r=e.get()
    l.append(r)
root = Tk()
ent = Entry(root)
ent.pack()
root.bind('<Return>',(lambda event,e=ent: fetch(e)))
button = Button(root,text='Input',command=(lambda e=ent: f(e)))
button.pack()
mainloop()
print(l)