import tkinter as tk
from tkinter import *

window = Tk()

window.title('janela teste')


window.geometry('600x600')


entry = tk.Entry(window)
entry.pack()
nome = entry.get()
label = tk.Label(window, text="Hello "+nome, font=("Helvetica", 18), fg="red", bg="blue")

image = tk.PhotoImage(file = 'poles.png')
labelimage = tk.Label(window,image=image)

def sayhello():
    nome = entry.get()
    label = tk.Label(window, text="Hello "+nome, font=("Helvetica", 18), fg="red", bg="blue")
    label.pack()

def sayhello2():
    nome = entry.get()
    label.config(text="Hello " + nome)
    label.pack()
    labelimage.pack()


button = tk.Button(window, text="Click me!", command=sayhello2)
button.pack()

#def draw_circle(canvas, x, y, radius, color):
#    canvas.create_oval(x-radius, y-radius, x+radius, y+radius, fill=color)

#canvas = tk.Canvas(window, width=400, height=400, bg="white")
#canvas.pack()
#draw_circle(canvas, 200, 200, 50, "red")





window.mainloop()
