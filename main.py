from tkinter import *
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


# criação do botão para confirmar o nome da substância
def confirma_substancia():
    print(f"Substância: {nome_substancia.get()}")


botao1 = Button(
    app,
    text="OK",
    bg="#e7e7e7",
    fg="black",
    font="Arial 11",
    command=confirma_substancia,
)
botao1.place(x=20, y=90, width=100, height=30, anchor=W)


# criação do botão para gravar o nome da substância
def gravar_substancia():
    nome_arquivo = caminho + "\\Resultados_" + nome_substancia.get() + ".txt"
    arquivo = open(nome_arquivo, "a")
    arquivo.write("Substância: " + nome_substancia.get())
    arquivo.close()
    print(f"Substância: {nome_substancia.get()}")


botao2 = Button(
    app,
    text="Gravar",
    bg="#e7e7e7",
    fg="black",
    font="Arial 11",
    command=gravar_substancia,
)
botao2.place(x=120, y=90, width=100, height=30, anchor=W)

app.mainloop()
