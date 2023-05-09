
from tkinter import *
from tkinter import ttk

janela = Tk()
janela.geometry("290x200")
janela.title("Contador de clicks")
clicks = 0

def clicar():
    global clicks
    clicks += 1
    texto.config(text=f"{clicks}")
    print(clicks)

texto = ttk.Label(janela, text=f"{clicks}")
texto.grid(column=6, row=8)
botao = ttk.Button(janela, command=clicar, text="Clique aqui")
botao.grid(column=5, row=6)

janela.mainloop()
