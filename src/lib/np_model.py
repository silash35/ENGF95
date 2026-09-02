from collections.abc import Callable

import numpy as np

from .parameters import (
    E1,
    E2,
    Q1,
    Q2,
    Q3,
    T0,
    V1,
    V2,
    V3,
    Cp,
    R,
    alphaA,
    alphaB,
    alphaC,
    dH1,
    dH2,
    eps,
    k1,
    k2,
    m,
    rho,
    xA0,
)


# --- System Dynamics ---
def model(t: float, y: np.ndarray, u: list[Callable[[float], float]]):
    """
    Differential equations for reactor-separator system.

    Parameters:
    - t: time [s]
    - y: state vector
    - u: input vector
    """

    # States
    T1 = y[0]  # Temperature of reactor 1 [K]
    T2 = y[1]  # Temperature of reactor 2 [K]
    T3 = y[2]  # Temperature of separator [K]

    xA1 = y[3]  # Mole fraction of A in reactor 1 [-]
    xB1 = y[4]  # Mole fraction of B in reactor 1 [-]

    xA2 = y[5]  # Mole fraction of A in reactor 2 [-]
    xB2 = y[6]  # Mole fraction of B in reactor 2 [-]

    xA3 = y[7]  # Mole fraction of A in separator [-]
    xB3 = y[8]  # Mole fraction of B in separator [-]

    # Inputs
    Ff1 = u[0](t)  # Feed flow rate to reactor 1 [m³/h]
    Ff2 = u[1](t)  # Feed flow rate to reactor 2 [m³/h]
    FR = u[2](t)  # Recycle flow rate [m³/h]

    # Flow rate to keep volumes constant
    F1 = Ff1 + FR
    F2 = Ff2 + F1

    # Component C
    xC3 = 1 - xA3 - xB3

    # Purge
    FP = eps * FR

    # Arrhenius kinetics
    k11 = k1 * np.exp(-E1 / (R * T1))
    k21 = k2 * np.exp(-E2 / (R * T1))

    k12 = k1 * np.exp(-E1 / (R * T2))
    k22 = k2 * np.exp(-E2 / (R * T2))

    # Recycle composition (equilibrium)
    denom = alphaA * xA3 + alphaB * xB3 + alphaC * xC3
    xAR = alphaA * xA3 / denom
    xBR = alphaB * xB3 / denom

    # --- Balances ---
    # Temperature
    dT1dt = (
        (Ff1 / V1) * (T0 - T1)
        + (FR / V1) * (T3 - T1)
        + Q1 / (rho * Cp * V1)
        - (m / Cp) * (k11 * xA1 * dH1 + k21 * xB1 * dH2)
    )

    dT2dt = (
        (Ff2 / V2) * (T0 - T2)
        + (F1 / V2) * (T1 - T2)
        + Q2 / (rho * Cp * V2)
        - (m / Cp) * (k12 * xA2 * dH1 + k22 * xB2 * dH2)
    )

    dT3dt = (F2 / V3) * (T2 - T3) + Q3 / (rho * Cp * V3)

    # Compositions
    dxA1dt = (Ff1 / V1) * (xA0 - xA1) + (FR / V1) * (xAR - xA1) - k11 * xA1
    dxB1dt = (FR / V1) * (xBR - xB1) - (Ff1 / V1) * xB1 + k11 * xA1 - k21 * xB1

    dxA2dt = (Ff2 / V2) * (xA0 - xA2) + (F1 / V2) * (xA1 - xA2) - k12 * xA2
    dxB2dt = (F1 / V2) * (xB1 - xB2) - (Ff2 / V2) * xB2 + k12 * xA2 - k22 * xB2

    dxA3dt = (F2 / V3) * (xA2 - xA3) - ((FP + FR) / V3) * (xAR - xA3)
    dxB3dt = (F2 / V3) * (xB2 - xB3) - ((FP + FR) / V3) * (xBR - xB3)

    return [
        dT1dt,
        dT2dt,
        dT3dt,
        dxA1dt,
        dxB1dt,
        dxA2dt,
        dxB2dt,
        dxA3dt,
        dxB3dt,
    ]
