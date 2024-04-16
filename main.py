from tkinter import *
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# iniciar app
app = Tk()

# configurações
app.title("Perry's ThermoGraph app")
app.geometry("1000x600")
app.configure(bg="#e7e7e7")

# criação da caixa de entrada e inserção do nome da substância
nome = Label(app, text="Insira o nome da substância:", bg="#e7e7e7",fg="black", font="Arial 11 bold")
nome.place(x=20, y=30, width=200, height=30, anchor=W)
nome_substancia = Entry(app, bg="white",fg="black", font="Arial 11")
nome_substancia.place(x=20, y=60, width=200, height=30, anchor=W)


# leitura da tabela de pressao de vapor
#pressao_vapor_perry = pd.read_csv("pressao_vapor.csv")


# função para calculo da pressao de vapor
""" def calc_pressao_vapor(data: pd.DataFrame, compound: str):
    row_compound = pressao_vapor_perry[pressao_vapor_perry["Name"] == compound]
    C1 = row_compound["C1"].iloc[0]
    C2 = row_compound["C2"].iloc[0]
    C3 = row_compound["C3"].iloc[0]
    C4 = row_compound["C4"].iloc[0]
    C5 = row_compound["C5"].iloc[0]
    Tmin = row_compound["Tmin"].iloc[0]
    Tmax = row_compound["Tmax"].iloc[0]
    T_range = np.linspace(Tmin, Tmax, 2000)
    pressao_vapor = []
    for T in T_range:
        pressao_vapor.append(np.exp(C1 + C2 / T + C3 * np.log(T) + C4 * (T**C5)))
    return T_range, pressao_vapor


# exemplo
compound = "Water"
x, y = calc_pressao_vapor(pressao_vapor_perry, compound)
plt.plot(x, y)

plt.show() """

app.mainloop()
