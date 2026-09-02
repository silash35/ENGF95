from .parameters import FR_0, Ff1_0, Ff2_0
from .utils import step


def Ff1_func(t, disturb=False):
    """Feed flow rate to reactor 1 [m³/h]"""
    return step(t, Ff1_0, disturb=disturb, gain=1.5)


def Ff2_func(t, disturb=False):
    """Feed flow rate to reactor 2 [m³/h]"""
    return step(t, Ff2_0, disturb=disturb, gain=1.5)


def FR_func(t, disturb=False):
    """Recycle flow rate [m³/h]"""
    return step(t, FR_0, disturb=disturb, gain=1.5)
