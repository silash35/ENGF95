import control as ctrl
import matplotlib.pyplot as plt
import numpy as np

from lib.utils import input_units, output_units

plt.rcParams.update(
    {
        "font.size": 14,
        "axes.grid": True,
        "figure.constrained_layout.use": True,
        "figure.dpi": 300,
    }
)

save_folder = "../figures/"


def plot_or_show(save_path=None):
    if save_path is None:
        plt.show()
    else:
        save_path = save_folder + save_path + ".png"
        plt.savefig(save_path)
        print(f"Plot saved to {save_path}")
        plt.close()


def plot_system_inputs(t, u, save_path=None):
    _fig, axs = plt.subplots(1, 3, figsize=(16, 3), sharex=True)

    axs[0].plot(t, u[0], label="$F_{f1}$")
    axs[0].set_ylabel(f"Vazão / {input_units[0]}")

    axs[1].plot(t, u[1], label="$F_{f2}$")
    axs[1].set_ylabel(f"Vazão / {input_units[1]}")

    axs[2].plot(t, u[2], label="$F_R$")
    axs[2].set_ylabel(f"Vazão / {input_units[2]}")

    for ax in axs.flat:
        ax.legend()
        ax.set_xlabel("Tempo / h")

    plot_or_show(save_path)


def plot_system_outputs(t, y, save_path=None):
    T1, T2, T3 = y[0], y[1], y[2]
    xA1, xB1 = y[3], y[4]
    xA2, xB2 = y[5], y[6]
    xA3, xB3 = y[7], y[8]

    xC1 = 1 - xA1 - xB1
    xC2 = 1 - xA2 - xB2
    xC3 = 1 - xA3 - xB3

    _fig, axs = plt.subplots(2, 3, figsize=(16, 6), sharex=True)

    titles = ["Reator 1", "Reator 2", "Separador"]
    Ts = [T1, T2, T3]
    xAs = [xA1, xA2, xA3]
    xBs = [xB1, xB2, xB3]
    xCs = [xC1, xC2, xC3]
    labels = [("A1", "B1", "C1"), ("A2", "B2", "C2"), ("A3", "B3", "C3")]

    for i, (title, T, xA, xB, xC, lbl) in enumerate(
        zip(titles, Ts, xAs, xBs, xCs, labels)
    ):
        axs[0, i].set_title(title)
        axs[0, i].plot(t, T)
        axs[1, i].plot(t, xA, label=f"$x_{{{lbl[0]}}}$")
        axs[1, i].plot(t, xB, label=f"$x_{{{lbl[1]}}}$")
        # axs[1, i].plot(t, xC, label=f"$x_{{{lbl[2]}}}$")
        axs[1, i].set_xlabel("Tempo / h")
        axs[1, i].legend()

    axs[0, 0].set_ylabel(f"Temperatura / {output_units[0]}")
    axs[1, 0].set_ylabel("Composição")

    plot_or_show(save_path)


def pzplot(G, save_path=None):
    poles = ctrl.poles(G)
    zeros = ctrl.zeros(G)

    _, ax = plt.subplots(figsize=(16 / 3, 9 / 3))

    if len(zeros) > 0:
        ax.scatter(np.real(zeros), np.imag(zeros), marker="o", label="Zeros")

    if len(poles) > 0:
        ax.scatter(np.real(poles), np.imag(poles), marker="x", label="Polos")

    ax.axhline(0, color="black", linewidth=0.8)
    ax.axvline(0, color="black", linewidth=0.8)

    ax.set_xlabel("Parte Real")
    ax.set_ylabel("Parte Imaginária")

    if len(zeros) > 0 or len(poles) > 0:
        ax.legend()

    plot_or_show(save_path)


def plot_fft(t, y, save_path=None):
    N = len(y)
    dt = t[1] - t[0]

    Y = np.fft.fft(y)
    freq = np.fft.fftfreq(N, d=dt)

    omega = 2 * np.pi * freq
    mask = omega >= 0
    omega_pos = omega[mask]
    Y_pos = Y[mask]

    mag = np.abs(Y_pos) / N

    plt.figure(figsize=(8, 4))
    plt.plot(omega_pos, mag)

    plt.xlim(0, 300)

    plt.xlabel(r"Frequência angular / (rad$\cdot$h$^{-1}$)")
    plt.ylabel("Magnitude")

    plot_or_show(save_path)
