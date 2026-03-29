# README.md

## Česky (ČJ)

## VQE pro zemní stavy molekul

Toto repo implementuje **Variational Quantum Eigensolver (VQE)** pro výpočet zemních stavů molekul pomocí knihovny Qiskit. VQE je hybridní kvantově-klasický algoritmus optimalizující očekávanou hodnotu Hamiltoniánu molekuly.

### Funkce
- Výpočet Hamiltoniánu molekul (H2, LiH, atd.)
- Ansatz UCCSD (Unitary Coupled Cluster Singles and Doubles)
- Optimalizace pomocí klasických optimalizátorů (SPSA, COBYLA)
- Simulace na klasickém hardware i Qiskit Aer

### Požadavky
```bash
pip install qiskit qiskit-nature qiskit-algorithms pyscf matplotlib numpy
```

### Příklady výstupů
Repo obsahuje grafy konvergence energie a srovnání s klasickými metodami (HF, FCI).

---

## English (EN)

## VQE for Ground States of Molecules

This repository implements the **Variational Quantum Eigensolver (VQE)** to compute ground states of molecules using Qiskit. VQE is a hybrid quantum-classical algorithm that variationally minimizes the expectation value of the molecular Hamiltonian.

### Features
- Molecular Hamiltonian computation (H2, LiH, etc.)
- UCCSD ansatz (Unitary Coupled Cluster Singles and Doubles)
- Classical optimization (SPSA, COBYLA)
- Simulation on classical hardware and Qiskit Aer

### Requirements
```bash
pip install qiskit qiskit-nature qiskit-algorithms pyscf matplotlib numpy
```

### Example Outputs
The repo includes convergence plots and comparisons with classical methods (HF, FCI).
