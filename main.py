import tkinter as tk
import random

root = tk.Tk()
root.title("Quer namorar comigo?")
root.geometry("400x400")

def hover(event):
    x = random.randint(0, 400)
    y = random.randint(0, 400)
    nao.place(x=x, y=y)

def message():
    text = tk.Label(root, text="Te amo S2")
    text.place(x=70, y=120, relx=0, rely=0)
    text.pack(anchor="n", pady=20)

nao = tk.Button(root, text="Não")
nao.place(x=200, y=140)
nao.bind('<Enter>', hover)

sim = tk.Button(root, text="Sim", command=message)
sim.place(x=120, y=140,relx=0, rely=0)

root.mainloop()
