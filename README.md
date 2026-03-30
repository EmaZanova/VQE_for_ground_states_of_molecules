# README.md

## Česky (ČJ)

## VQE pro zemní stavy molekul

Toto repozitář implementuje **Variational Quantum Eigensolver (VQE)** pro výpočet zemních stavů molekul pomocí knihovny Qiskit. VQE je hybridní kvantově-klasický algoritmus optimalizující očekávanou hodnotu Hamiltoniánu molekuly.

### 📚 Hlavní inspirace
Tento kód vychází z oficiálního IBM Qiskit tutoriálu:  
[Spin Chain VQE Tutorial](https://quantum.cloud.ibm.com/docs/en/tutorials/spin-chain-vqe)[web:1]

### Funkce
- Výpočet Hamiltoniánu molekul (H2, LiH, N2)
- Ansatz efficient_su2 (efektivní na kvantovém hardwaru)
- Optimalizace pomocí klasických optimalizátorů (COBYLA)
- Simulace na klasickém hardware i Qiskit Aer

### Instalace
```bash
# 1. Vytvoř virtuální prostředí (doporučeno)
python -m venv vqe_env
source vqe_env/bin/activate  # Linux/Mac
# vqe_env\Scripts\activate    # Windows

# 2. Nainstaluj závislosti
pip install -r requirements.txt
```

### Příklady výstupů
Repo obsahuje grafy konvergence energie a srovnání s klasickými metodami (HF, FCI).

---

## English (EN)

## VQE for Ground States of Molecules

This repository implements the **Variational Quantum Eigensolver (VQE)** to compute ground states of molecules using Qiskit. VQE is a hybrid quantum-classical algorithm that variationally minimizes the expectation value of the molecular Hamiltonian.

## 📚 Main Reference
This code is based on official IBM Qiskit tutorial:  
[Spin Chain VQE Tutorial](https://quantum.cloud.ibm.com/docs/en/tutorials/spin-chain-vqe)[web:1]

### Features
- Molecular Hamiltonian computation (H2, LiH, N2)
- efficient_su2 (hardware efficient ansatz)
- Classical optimization (COBYLA)
- Simulation on classical hardware and Qiskit Aer

### Installation
```bash
# 1. Create virtual environment (recommended)
python -m venv vqe_env
source vqe_env/bin/activate  # Linux/Mac
# vqe_env\Scripts\activate    # Windows

# 2. Install dependencies
pip install -r requirements.txt
```

### Example Outputs
The repo includes convergence plots and comparisons with classical methods (HF, FCI).
