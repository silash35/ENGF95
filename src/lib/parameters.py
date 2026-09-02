from typing import Final

rho: Final = 1000.0
"""Fluid density [kg/m³]"""

Cp: Final = 4.2
"""Heat capacity [kJ/kg·K]"""

m: Final = 0.00279
"""Molality [kmol/kg]"""

R: Final = 8.314
"""Universal gas constant [kJ/kmol·K]"""

k1: Final = 2.77e3 * 3600
"""Pre-exponential factor for reaction A -> B [1/h]"""

k2: Final = 2.5e3 * 3600
"""Pre-exponential factor for reaction B -> C [1/h]"""

E1: Final = 5.0e4
"""Activation energy for reaction A -> B [kJ/kmol]"""

E2: Final = 6.0e4
"""Activation energy for reaction B -> C [kJ/kmol]"""

dH1: Final = -6.0e4
"""Heat of reaction A -> B [kJ/kmol]"""

dH2: Final = -7.0e4
"""Heat of reaction B -> C [kJ/kmol]"""

alphaA: Final = 5.0
"""Relative volatility of component A [-]"""

alphaB: Final = 1.0
"""Relative volatility of component B [-]"""

alphaC: Final = 0.5
"""Relative volatility of component C [-]"""

eps: Final = 0.02
"""Purge ratio (FP = eps * FR) [-]"""

xA0 = 1.0
"""Feed mole fraction of component A [-]"""

V1 = 1.0
"""Volume of reactor 1 [m³]"""

V2 = 0.5
"""Volume of reactor 2 [m³]"""

V3 = 1.0
"""Volume of separator [m³]"""

Q1 = 715.3e3
"""Heat input to reactor 1 [kJ/h]"""

Q2 = 579.8e3
"""Heat input to reactor 2 [kJ/h]"""

Q3 = 568.7e3
"""Heat input to separator [kJ/h]"""

T0 = 359.1
"""Feed temperature [K]"""

# --- Initial conditions ---

T1_0 = 432.4
T2_0 = 427.1
T3_0 = 432.1

xA1_0 = 0.536
xB1_0 = 0.448
xA2_0 = 0.545

xB2_0 = 0.438
xA3_0 = 0.298
xB3_0 = 0.670

y0 = [T1_0, T2_0, T3_0, xA1_0, xB1_0, xA2_0, xB2_0, xA3_0, xB3_0]

Ff1_0 = 5.04
Ff2_0 = 5.04
FR_0 = 17.0

u0 = [Ff1_0, Ff2_0, FR_0]
