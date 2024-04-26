import tkinter as tk
from tkinter import ttk
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from pressao_vapor import calc_pressao_vapor
from densidade import calc_densidade
import os

caminho = os.path.dirname(__file__)

# iniciar app
app = tk.Tk()

# configurações básicas
app.title("Perry's ThermoGraph app")
app.geometry("1000x600")
app.configure(bg="#e7e7e7")

# criação da caixa de entrada
nome = tk.Label(
    app,
    text="Insira o nome da substância:",
    bg="#e7e7e7",
    fg="black",
    font="Arial 11 bold",
)
nome.place(x=20, y=30, width=200, height=30, anchor=tk.W)

# inserção da substância
data = pd.read_csv("tabelas/pressao_vapor.csv")
lista_nomes = data["Name"].tolist()
nome_substancia = ttk.Combobox(
    app, values=lista_nomes, state="readonly", font="Arial 11 bold"
)
nome_substancia.place(x=20, y=60, width=200, height=30, anchor=tk.W)


# criação da janela de grafico
fig, ax = plt.subplots()
canvas = FigureCanvasTkAgg(fig, master=app)
canvas_widget = canvas.get_tk_widget()
canvas_widget.place(x=350, y=50)

# criação da barra de ferramentas
toolbar = NavigationToolbar2Tk(canvas, app, pack_toolbar=False)
toolbar.update()
toolbar.pack(side=tk.BOTTOM, fill=tk.X, padx=(350, 0))


# chamar função e criar botão para plotar o grafico da pressão de vapor
def plotar_grafico_pressao():
    ax.clear()
    t1, p1 = calc_pressao_vapor(nome_substancia.get())
    ax.plot(t1, p1)
    plt.title("Pressão de Vapor: " + nome_substancia.get())
    plt.xlabel("Temperatura (K)")
    plt.ylabel("Pressão de Vapor (MPa)")

    canvas.draw()


botao_PV = tk.Button(
    app,
    text="PV",
    bg="#e7e7e7",
    fg="black",
    font="Arial 11",
    command=plotar_grafico_pressao,
)
botao_PV.place(x=20, y=90, width=100, height=30, anchor=tk.W)


# chamar função e criar botão para plotar o grafico da densidade
def plotar_grafico_densidade():
    ax.clear()
    t1, d1, v1, dm1, vm1 = calc_densidade(nome_substancia.get())
    ax.plot(t1, d1)
    plt.title("Densidade molar: " + nome_substancia.get())
    plt.xlabel("Temperatura (K)")
    plt.ylabel("Densidade (mol/dm³)")
    canvas.draw()


botao_Densidade = tk.Button(
    app,
    text="Densidade",
    bg="#e7e7e7",
    fg="black",
    font="Arial 11",
    command=plotar_grafico_densidade,
)
botao_Densidade.place(x=20, y=120, width=100, height=30, anchor=tk.W)


# chamar função e criar botão para plotar o grafico do volume molar
def plotar_grafico_volume():
    ax.clear()
    t1, d1, v1, dm1, vm1 = calc_densidade(nome_substancia.get())
    ax.plot(t1, v1)
    plt.title("Volume molar: " + nome_substancia.get())
    plt.xlabel("Temperatura (K)")
    plt.ylabel("Volume (dm³/mol)")
    canvas.draw()


botao_volume = tk.Button(
    app,
    text="Volume",
    bg="#e7e7e7",
    fg="black",
    font="Arial 11",
    command=plotar_grafico_volume,
)
botao_volume.place(x=120, y=120, width=100, height=30, anchor=tk.W)


# criação do botão para limpar o grafico
def limpar():
    ax.clear()
    canvas.draw()


botao_limpar = tk.Button(
    app, text="Limpar", bg="#e7e7e7", fg="black", font="Arial 11", command=limpar
)
botao_limpar.place(x=20, y=200, width=100, height=30, anchor=tk.W)

# criação do botão para sair
botao_sair = tk.Button(
    master=app,
    text="Sair",
    bg="#e7e7e7",
    fg="black",
    font="Arial 11",
    command=app.destroy,
)
botao_sair.place(x=120, y=200, width=100, height=30, anchor=tk.W)


app.mainloop()
