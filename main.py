from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from pressao_vapor import calc_pressao_vapor
from densidade import calc_densidade
import os

caminho = os.path.dirname(__file__)

# iniciar app
app = Tk()

# configurações básicas
app.title("Perry's ThermoGraph app")
app.geometry("1000x600")
app.configure(bg="#e7e7e7")

# criação da caixa de entrada e inserção do nome da substância
nome = Label(
    app,
    text="Insira o nome da substância:",
    bg="#e7e7e7",
    fg="black",
    font="Arial 11 bold",
)
nome.place(x=20, y=30, width=200, height=30, anchor=W)
nome_substancia = Entry(app, bg="white", fg="black", font="Arial 11")
nome_substancia.place(x=20, y=60, width=200, height=30, anchor=W)


# criação do grafico
fig, ax = plt.subplots()
canvas = FigureCanvasTkAgg(fig, master=app)
canvas_widget = canvas.get_tk_widget()
canvas_widget.place(x=350, y=50)

# criação da barra de ferramentas
toolbar = NavigationToolbar2Tk(canvas, app, pack_toolbar=False)
toolbar.update()
toolbar.pack(side=BOTTOM)

# chamar função e criar botão para plotar o grafico da pressão de vapor
def plotar_grafico_pressao():
    ax.clear()
    t1,p1 = calc_pressao_vapor(nome_substancia.get())
    ax.plot(t1,p1)
    plt.title("Pressão de Vapor: " + nome_substancia.get())
    plt.xlabel("Temperatura (K)")
    plt.ylabel("Pressão de Vapor (Pa)")
    canvas.draw()

botao_PV = Button(
    app,
    text="PV",
    bg="#e7e7e7",
    fg="black",
    font="Arial 11",
    command=plotar_grafico_pressao
)
botao_PV.place(x=20, y=90, width=100, height=30, anchor=W)

# chamar função e criar botão para plotar o grafico da densidade
def plotar_grafico_densidade():
    ax.clear()
    t1,d1,v1 = calc_densidade(nome_substancia.get())
    ax.plot(t1,d1)
    plt.title("Densidade molar: " + nome_substancia.get())
    plt.xlabel("Temperatura (K)")
    plt.ylabel("Densidade (mol/dm³)")
    canvas.draw()

botao_Densidade = Button(
    app,
    text="Densidade",
    bg="#e7e7e7",
    fg="black",
    font="Arial 11",
    command=plotar_grafico_densidade
)
botao_Densidade.place(x=20, y=120, width=100, height=30, anchor=W)


# chamar função e criar botão para plotar o grafico do volume molar
def plotar_grafico_volume():
    ax.clear()
    t1,d1,v1 = calc_densidade(nome_substancia.get())
    ax.plot(t1,v1)
    plt.title("Volume molar: " + nome_substancia.get())
    plt.xlabel("Temperatura (K)")
    plt.ylabel("Volume (dm³/mol)")
    canvas.draw()

botao_volume = Button(
    app,
    text="Volume",
    bg="#e7e7e7",
    fg="black",
    font="Arial 11",
    command=plotar_grafico_volume
)
botao_volume.place(x=120, y=120, width=100, height=30, anchor=W)

# criação do botão para limpar o grafico
def limpar():
    ax.clear()
    canvas.draw()
    
botao_limpar = Button(
    app,
    text="Limpar",
    bg="#e7e7e7",
    fg="black",
    font="Arial 11",
    command=limpar
)
botao_limpar.place(x=120, y=90, width=100, height=30, anchor=W)



app.mainloop()
