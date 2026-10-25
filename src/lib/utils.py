import control as ctrl
import numpy as np
import sympy as sp
from IPython.display import Math, display

input_labels = ["$F_{f1}$", "$F_{f2}$", "$F_R$"]
output_labels = [
    "$T_1$",
    "$T_2$",
    "$T_3$",
    "$x_{A1}$",
    "$x_{B1}$",
    "$x_{A2}$",
    "$x_{B2}$",
    "$x_{A3}$",
    "$x_{B3}$",
]

input_names = ["Ff1", "Ff2", "FR"]
output_names = ["T1", "T2", "T3", "xA1", "xB1", "xA2", "xB2", "xA3", "xB3"]

output_units = ["K"] * 3 + ["-"] * 6
input_units = ["(m$^3\\cdot$h$^{-1}$)"] * 3


def show(left, right, digitos=3):
    display(Math(left + " = " + sp.latex(sp.N(right, digitos))))


def G_sp_to_ctrl(G_sym):
    s = sp.symbols("s")
    num, den = sp.fraction(G_sym)
    num = sp.Poly(num, s).all_coeffs()
    den = sp.Poly(den, s).all_coeffs()
    num = [float(coef) for coef in num]
    den = [float(coef) for coef in den]
    return ctrl.TransferFunction(num, den)


gain = 1.5


def step(t, y0: float, step_time: float = 0.2, disturb: bool = False):
    y1 = gain * y0

    if not disturb:
        return y0 if np.isscalar(t) else np.full_like(t, y0, dtype=float)

    return np.where(t < step_time, y0, y1)


def pulse(
    t, y0: float, step_time: float = 0.2, end_time: float = 2.5, disturb: bool = False
):
    y1 = gain * y0

    if not disturb:
        return y0 if np.isscalar(t) else np.full_like(t, y0, dtype=float)

    return np.where((t >= step_time) & (t < end_time), y1, y0)
