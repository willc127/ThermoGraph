import tkinter as tk
from tkinter import ttk
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from pressao_vapor import calc_pressao_vapor
from densidade import calc_densidade
from entalpia_vap import calc_entalpia_vap
import os

caminho = os.path.dirname(__file__)

# iniciar app
app = tk.Tk()

# configurações básicas
app.title("Perry's ThermoGraph app")
app.geometry("1800x900")
app.configure(bg="#e7e7e7")

# criação do icone
app.iconbitmap(os.path.join(caminho, "icone/biochemistry_sj1_icon.ico"))

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


# criação da caixa de entrada da temperatura de interesse
temp = tk.Label(
    app,
    text="Insira a temperatura (K):",
    bg="#e7e7e7",
    fg="black",
    font="Arial 11 bold",
)
temp.place(x=20, y=90, width=200, height=30, anchor=tk.W)

entry_temp = tk.Entry(app, width=10)
entry_temp.place(x=20, y=120, width=200, height=30, anchor=tk.W)


# criação da janela de grafico
fig, ax = plt.subplots(figsize=(12, 8))
canvas = FigureCanvasTkAgg(
    fig,
    master=app,
)
canvas_widget = canvas.get_tk_widget()
canvas_widget.place(x=500, y=50)

# criação da barra de ferramentas
toolbar = NavigationToolbar2Tk(canvas, app, pack_toolbar=False)
toolbar.update()
toolbar.pack(side=tk.BOTTOM, fill=tk.X, padx=(500, 0))


# chamar função e criar botão para plotar o grafico da pressão de vapor
def plotar_grafico_pressao():
    ax.clear()
    p_user, t1, p1 = calc_pressao_vapor(nome_substancia.get(), float(entry_temp.get()))
    ax.plot(t1, p1)
    plt.title("Pressão de Vapor: " + nome_substancia.get())
    plt.xlabel("Temperatura (K)")
    plt.ylabel("Pressão de Vapor (MPa)")
    canvas.draw()

    resultado_PV = tk.Label(
        app,
        text="Pressão de vapor ({:}): {:.2f} MPa".format(nome_substancia.get(), p_user),
        bg="#e7e7e7",
        fg="black",
        font="Arial 11 bold",
    )
    resultado_PV.place(x=20, y=300)


botao_PV = tk.Button(
    app,
    text="PV",
    bg="#e7e7e7",
    fg="black",
    font="Arial 11",
    command=plotar_grafico_pressao,
)
botao_PV.place(x=20, y=170, width=100, height=30, anchor=tk.W)


# chamar função e criar botão para plotar o grafico da densidade
def plotar_grafico_densidade():
    ax.clear()
    d_user, v_user, dm_user, vm_user, t1, d1, v1, dm1, vm1 = calc_densidade(nome_substancia.get(),float(entry_temp.get()))
    ax.plot(t1, d1)
    plt.title("Densidade molar: " + nome_substancia.get())
    plt.xlabel("Temperatura (K)")
    plt.ylabel("Densidade (mol/dm^3)")
    canvas.draw()

    # criar label com resultado da densidade
    resultado_densidade = tk.Label(
        app,
        text="Densidade ({:}): {:.2f} mol/dm^3".format(nome_substancia.get(), d_user),
        bg="#e7e7e7",
        fg="black",
        font="Arial 11 bold",
    )
    resultado_densidade.place(x=20, y=330)


botao_Densidade = tk.Button(
    app,
    text="Densidade",
    bg="#e7e7e7",
    fg="black",
    font="Arial 11",
    command=plotar_grafico_densidade,
)
botao_Densidade.place(x=20, y=200, width=100, height=30, anchor=tk.W)


# chamar função e criar botão para plotar o grafico do volume molar
def plotar_grafico_volume():
    ax.clear()
    d_user, v_user, dm_user, vm_user, t1, d1, v1, dm1, vm1 = calc_densidade(nome_substancia.get(), float(entry_temp.get()))
    ax.plot(t1, v1)
    plt.title("Volume molar: " + nome_substancia.get())
    plt.xlabel("Temperatura (K)")
    plt.ylabel("Volume (dm³/mol)")
    canvas.draw()
    # criar label com resultado do volume

    resultado_volume = tk.Label(
        app,
        text="Volume ({:}): {:.2f} dm^3/mol".format(nome_substancia.get(), v_user),
        bg="#e7e7e7",
        fg="black",
        font="Arial 11 bold",
    )
    resultado_volume.place(x=20, y=360)


botao_volume = tk.Button(
    app,
    text="Volume",
    bg="#e7e7e7",
    fg="black",
    font="Arial 11",
    command=plotar_grafico_volume,
)
botao_volume.place(x=120, y=200, width=100, height=30, anchor=tk.W)


# chamar função e criar botão para plotar o grafico da entalpia de vaporização
def plotar_grafico_entalpia_vap():
    ax.clear()
    dh_user, t1, dh1 = calc_entalpia_vap(nome_substancia.get(), float(entry_temp.get()))
    ax.plot(t1, dh1)
    plt.title("entalpia molar: " + nome_substancia.get())
    plt.xlabel("Temperatura (K)")
    plt.ylabel("Entalpia de vaporização (J/mol)")
    canvas.draw()

    resultado_entalpia = tk.Label(
    app,
    text="Entalpia de vaporização ({:}): {:.2f} J/mol".format(nome_substancia.get(), dh_user),
    bg="#e7e7e7",
    fg="black",
    font="Arial 11 bold",
)
    resultado_entalpia.place(x=20, y=390)

botao_entalpia = tk.Button(
    app,
    text="\u0394H_vap",
    bg="#e7e7e7",
    fg="black",
    font="Arial 11",
    command=plotar_grafico_entalpia_vap,
)
botao_entalpia.place(x=120, y=170, width=100, height=30, anchor=tk.W)


# criação do botão para limpar o grafico
def limpar():
    ax.clear()
    canvas.draw()


botao_limpar = tk.Button(
    app, text="Limpar", bg="#e7e7e7", fg="black", font="Arial 11", command=limpar
)
botao_limpar.place(x=20, y=250, width=100, height=30, anchor=tk.W)

# criação do botão para sair
botao_sair = tk.Button(
    master=app,
    text="Sair",
    bg="#e7e7e7",
    fg="black",
    font="Arial 11",
    command=app.quit,
)
botao_sair.place(x=120, y=250, width=100, height=30, anchor=tk.W)


app.mainloop()
