import pandas as pd
import numpy as np

entalpia_perry = pd.read_csv("tabelas/entalpia_vap.csv")
criticos_perry = pd.read_csv("tabelas/criticos.csv")


def calc_entalpia_vap(compound: str, T_user: float):
    row_compound = entalpia_perry[entalpia_perry["Name"] == compound]
    row_compound_criticos = criticos_perry[criticos_perry["Name"] == compound]
    Tc = float(row_compound_criticos["Tc"].iloc[0])
    C1 = float(row_compound["C1"].iloc[0])
    C2 = float(row_compound["C2"].iloc[0])
    C3 = float(row_compound["C3"].iloc[0])
    C4 = float(row_compound["C4"].iloc[0])
    Tmin = float(row_compound["Tmin"].iloc[0])
    Tmax = float(row_compound["Tmax"].iloc[0])
    T_range = np.linspace(Tmin, Tmax, 2000)
    entalpia_vap_user = (
        C1
        / 1000
        * (1 - T_user / Tc) ** (C2 + C3 * T_user / Tc + C4 * (T_user / Tc) ** 2)
    )
    entalpia_vap = []
    for T in T_range:
        entalpia_vap.append(
            C1
            / 1000
            * (1 - T / Tc) ** (C2 + C3 * T / Tc + C4 * (T / Tc) ** 2)  # [J/mol]
        )
    return entalpia_vap_user, T_range, entalpia_vap
