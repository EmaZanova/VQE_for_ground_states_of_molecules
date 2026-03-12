from qiskit_aer.primitives import EstimatorV2 as Estimator
import pandas as pd
from pathlib import Path
from qiskit_ibm_runtime import QiskitRuntimeService


def cost_function(
    params,
    problem,
    hamiltonian,
    ansatz,
    file_name: str = "vqe_results.csv",
    iterations: list[int] | None = None,
    estimator=Estimator,
    mode=None,
) -> float:
    """
    Vypočítá nákladovou funkci (energii) pro VQE a uloží výsledky do CSV souboru.
    """
    if mode is not None:
        estimator = estimator(mode=mode)
    else:
        estimator = estimator()

    # Inkrementace čítače iterací (seznam se používá pro zachování stavu mimo funkci)
    if iterations is not None:
        iterations[0] += 1
        print(f"Iteration {iterations[0]}: Evaluating cost function...")

    # Dosazení parametrů do variačního obvodu (ansatz)
    bound_circuit = ansatz.assign_parameters(params)

    # Spuštění výpočtu střední hodnoty hamiltoniánu
    job = estimator.run([(bound_circuit, hamiltonian)])
    result = job.result()

    # Získání elektronické energie
    electronic = result[0].data.evs

    # Celková energie = elektronická energie + energie odpuzování jader
    total_energy = electronic + problem.nuclear_repulsion_energy

    # Zápis do souboru
    with open(file_name, "a") as f:
        f.write(f"{iterations[0] if iterations else 'N/A'},{total_energy}\n")

    print(f"  Energy: {total_energy:.6f} Ha")

    return total_energy


def compute_error(estimated, expected):
    return ((expected - estimated) / expected) * 100


import pandas as pd
import matplotlib.pyplot as plt


def plot_convergence(
    file_name: str,
    molecule_name,
    expected_energy,
):
    df = pd.read_csv(file_name, names=["Iteration", "Energy"])

    plt.figure(figsize=(10, 6))
    plt.style.use("seaborn-v0_8-whitegrid")

    plt.plot(
        df["Iteration"],
        df["Energy"],
        label="VQE Energie",
        color="#0066cc",
        linewidth=2,
        marker="o",
        markersize=4,
        alpha=0.8,
    )

    plt.axhline(
        y=expected_energy,
        color="r",
        linestyle="--",
        label=f"Teoretické minimum ({expected_energy})",
    )

    plt.title(
        f"Konvergence algoritmu VQE pro molekulu ${molecule_name}$",
        fontsize=14,
        fontweight="bold",
    )
    plt.xlabel("Iterace (krok optimizeru)", fontsize=12)
    plt.ylabel("Energie [Hartree]", fontsize=12)

    plt.legend(frameon=True, shadow=True)
    plt.grid(True, linestyle=":", alpha=0.6)

    plt.tight_layout()

    plt.savefig("vqe_convergence_plot.png", dpi=300)
    plt.show()


def plot_convergence_simulator_qc(
    sim_filename, sim_filename2, molcule_name, expected_energy
):
    df_sim = pd.read_csv(sim_filename, names=["Iteration", "Energy"])

    df_qc = pd.read_csv(sim_filename2, names=["Iteration", "Energy"])

    qc_len = df_qc.__len__()
    df_sim = df_sim[:qc_len]

    plt.figure(figsize=(10, 6))
    plt.style.use("seaborn-v0_8-whitegrid")

    plt.plot(
        df_sim["Iteration"],
        df_sim["Energy"],
        label="VQE Energie (simulátor)",
        color="#0066cc",
        linewidth=2,
        marker="o",
        markersize=4,
        alpha=0.8,
    )

    plt.plot(
        df_qc["Iteration"],
        df_qc["Energy"],
        label="VQE Energie (kvantový počítač)",
        color="#cc6600",
        linewidth=2,
        marker="o",
        markersize=4,
        alpha=0.8,
    )

    plt.axhline(
        y=expected_energy,
        color="r",
        linestyle="--",
        label=f"Teoretické minimum ({expected_energy})",
    )

    plt.title(
        f"Konvergence algoritmu VQE pro molekulu ${molcule_name}$ (simulátor vs. kvantový počítač)",
        fontsize=14,
        fontweight="bold",
    )
    plt.xlabel("Iterace (krok optimizeru)", fontsize=12)
    plt.ylabel("Energie [Hartree]", fontsize=12)

    plt.legend(frameon=True, shadow=True)
    plt.grid(True, linestyle=":", alpha=0.6)

    plt.tight_layout()

    plt.savefig("vqe_convergence_comparison_plot.png", dpi=300)
    plt.show()


def plot_convergence_comparison(
    sim_filename1, sim_filename2, molecule_name, expected_energy
):
    df_sim = pd.read_csv(sim_filename1, names=["Iteration", "Energy"])
    df_qc = pd.read_csv(sim_filename2, names=["Iteration", "Energy"])

    plt.figure(figsize=(10, 6))
    plt.style.use("seaborn-v0_8-whitegrid")

    plt.plot(
        df_sim["Iteration"],
        df_sim["Energy"],
        label=f"VQE Energie ({sim_filename1})",
        color="#0066cc",
        linewidth=2,
        marker="o",
        markersize=4,
        alpha=0.8,
    )

    plt.plot(
        df_qc["Iteration"],
        df_qc["Energy"],
        label=f"VQE Energie ({sim_filename2})",
        color="#cc6600",
        linewidth=2,
        marker="o",
        markersize=4,
        alpha=0.8,
    )

    plt.axhline(
        y=expected_energy,
        color="r",
        linestyle="--",
        label=f"Teoretické minimum ({expected_energy})",
    )

    plt.title(
        f"Konvergence algoritmu VQE pro molekulu ${molecule_name}$ (simulátor vs. kvantový počítač)",
        fontsize=14,
        fontweight="bold",
    )
    plt.xlabel("Iterace (krok optimizeru)", fontsize=12)
    plt.ylabel("Energie [Hartree]", fontsize=12)

    plt.legend(frameon=True, shadow=True)
    plt.grid(True, linestyle=":", alpha=0.6)

    plt.tight_layout()

    plt.savefig("vqe_convergence_comparison_plot.png", dpi=300)
    plt.show()
