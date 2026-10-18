from .parameters import FR_0, Ff1_0, Ff2_0
from .utils import pulse


def Ff1_func(t, disturb=False):
    """Feed flow rate to reactor 1 [m³/h]"""
    return pulse(t, Ff1_0, disturb=disturb)


def Ff2_func(t, disturb=False):
    """Feed flow rate to reactor 2 [m³/h]"""
    return pulse(t, Ff2_0, disturb=disturb)


def FR_func(t, disturb=False):
    """Recycle flow rate [m³/h]"""
    return pulse(t, FR_0, disturb=disturb)
