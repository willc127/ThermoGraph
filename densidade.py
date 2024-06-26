import pandas as pd
import numpy as np


def calc_densidade(compound: str, T_user: float):
    # leitura da tabela de densidade
    data = pd.read_csv("tabelas/densidade_molar.csv")
    # selecionar a linha correspondente ao nome da substância
    row_compound = data[data["Name"] == compound]
    # calculo da pressao de vapor
    C1 = row_compound["C1"].iloc[0]
    C2 = row_compound["C2"].iloc[0]
    C3 = row_compound["C3"].iloc[0]
    C4 = row_compound["C4"].iloc[0]
    Tmin = row_compound["Tmin"].iloc[0]
    Tmax = row_compound["Tmax"].iloc[0]
    T_range = np.linspace(Tmin, Tmax, 2000)
    Massa_Molar = row_compound["MolWeight"].iloc[0]
    # Calculo da pressão de vapor de acordo com a temperatura especifica
    if compound == "Water" or compound == "o-Terphenyl":
        densidade_user = (
            C1 + C2 * T_user + C3 * (T_user**2) + C4 * (T_user**3)
        )  # mol/dm³
        volume_user = 1 / (C1 + C2 * T_user + C3 * (T_user**2) + C4 * (T_user**3))
        densidade_massica_user = (
            (C1 + C2 * T_user + C3 * (T_user**2) + C4 * (T_user**3))
            * Massa_Molar
            / 1000
        )  # [g/cm^3]
        volume_massico_user = 1 / (
            (C1 + C2 * T_user + C3 * (T_user**2) + C4 * (T_user**3))
            * Massa_Molar
            / 1000
        )  # [cm^3/g]
    else:
        densidade_user = C1 / (C2 ** (1 + (1 - T_user / C3) ** C4))  # mol/dm³
        volume_user = 1 / (C1 / (C2 ** (1 + (1 - T_user / C3) ** C4)))
        densidade_massica_user = (
            C1 / (C2 ** (1 + (1 - T_user / C3) ** C4)) * Massa_Molar / 1000
        )  # [g/cm^3]
        volume_massico_user = 1 / (
            C1 / (C2 ** (1 + (1 - T_user / C3) ** C4)) * Massa_Molar / 1000
        )  # [cm^3/g]

    densidade_molar = []
    densidade_massica = []
    volume_molar = []
    volume_massico = []
    for T in T_range:
        if compound == "Water" or compound == "o-Terphenyl":
            densidade_molar.append(C1 + C2 * T + C3 * (T**2) + C4 * (T**3))  # mol/dm³
            volume_molar.append(1 / (C1 + C2 * T + C3 * (T**2) + C4 * (T**3)))
            densidade_massica.append(
                (C1 + C2 * T + C3 * (T**2) + C4 * (T**3)) * Massa_Molar / 1000
            )  # [g/cm^3]
            volume_massico.append(
                1 / ((C1 + C2 * T + C3 * (T**2) + C4 * (T**3)) * Massa_Molar / 1000)
            )  # [cm^3/g]
        else:
            densidade_molar.append(C1 / (C2 ** (1 + (1 - T / C3) ** C4)))  # mol/dm³
            volume_molar.append(1 / (C1 / (C2 ** (1 + (1 - T / C3) ** C4))))
            densidade_massica.append(
                C1 / (C2 ** (1 + (1 - T / C3) ** C4)) * Massa_Molar / 1000
            )  # [g/cm^3]
            volume_massico.append(
                1 / (C1 / (C2 ** (1 + (1 - T / C3) ** C4)) * Massa_Molar / 1000)
            )  # [cm^3/g]
    return (
        densidade_user,
        volume_user,
        densidade_massica_user,
        volume_massico_user,
        T_range,
        densidade_molar,
        volume_molar,
        densidade_massica,
        volume_massico,
    )
