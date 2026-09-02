import sympy as sp

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

# --- Symbolic Variables ---

T1 = sp.symbols("T1")
T2 = sp.symbols("T2")
T3 = sp.symbols("T3")
xA1 = sp.symbols("xA1")
xB1 = sp.symbols("xB1")
xA2 = sp.symbols("xA2")
xB2 = sp.symbols("xB2")
xA3 = sp.symbols("xA3")
xB3 = sp.symbols("xB3")

Ff1 = sp.symbols("Ff1")
Ff2 = sp.symbols("Ff2")
FR = sp.symbols("FR")

# --- Equations ---

F1 = Ff1 + FR
F2 = Ff2 + F1

xC3 = 1 - xA3 - xB3
FP = eps * FR

k11 = k1 * sp.exp(-E1 / (R * T1))  # type: ignore
k21 = k2 * sp.exp(-E2 / (R * T1))  # type: ignore
k12 = k1 * sp.exp(-E1 / (R * T2))  # type: ignore
k22 = k2 * sp.exp(-E2 / (R * T2))  # type: ignore


denom = alphaA * xA3 + alphaB * xB3 + alphaC * xC3
xAR = alphaA * xA3 / denom
xBR = alphaB * xB3 / denom


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


dxA1dt = (Ff1 / V1) * (xA0 - xA1) + (FR / V1) * (xAR - xA1) - k11 * xA1
dxB1dt = (FR / V1) * (xBR - xB1) - (Ff1 / V1) * xB1 + k11 * xA1 - k21 * xB1

dxA2dt = (Ff2 / V2) * (xA0 - xA2) + (F1 / V2) * (xA1 - xA2) - k12 * xA2
dxB2dt = (F1 / V2) * (xB1 - xB2) - (Ff2 / V2) * xB2 + k12 * xA2 - k22 * xB2

dxA3dt = (F2 / V3) * (xA2 - xA3) - ((FP + FR) / V3) * (xAR - xA3)
dxB3dt = (F2 / V3) * (xB2 - xB3) - ((FP + FR) / V3) * (xBR - xB3)
