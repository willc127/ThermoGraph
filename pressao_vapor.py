import pandas as pd
import numpy as np


def calc_pressao_vapor(compound: str, T_user: float):
    # leitura da tabela de pressao de vapor
    data = pd.read_csv("tabelas/pressao_vapor.csv")
    # selecionar a linha correspondente ao nome da substância
    row_compound = data[data["Name"] == compound]
    # calculo da pressao de vapor
    C1 = row_compound["C1"].iloc[0]
    C2 = row_compound["C2"].iloc[0]
    C3 = row_compound["C3"].iloc[0]
    C4 = row_compound["C4"].iloc[0]
    C5 = row_compound["C5"].iloc[0]
    Tmin = row_compound["Tmin"].iloc[0]
    Tmax = row_compound["Tmax"].iloc[0]
    T_range = np.linspace(Tmin, Tmax, 2000)
    # Calculo da pressão de vapor de acordo com a temperatura especifica
    pressao_user = 1e-6 * np.exp(
        C1 + C2 / T_user + C3 * np.log(T_user) + C4 * (T_user**C5)
    )
    # Calculo da pressão de vapor de acordo com o intervalo de temperatura
    pressao_vapor = []
    for T in T_range:
        pressao_vapor.append(
            1e-6 * np.exp(C1 + C2 / T + C3 * np.log(T) + C4 * (T**C5))
        )  # [MPa]
    return pressao_user, T_range, pressao_vapor
