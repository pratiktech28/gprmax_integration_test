[![Integration Test CI](https://github.com/pratiktech28/gprmax_integration_test/actions/workflows/integration.yml/badge.svg)](https://github.com/pratiktech28/gprmax_integration_test/actions/workflows/integration.yml)

<img width="412" height="225" alt="download" src="https://github.com/user-attachments/assets/0191f5d7-407a-4217-b9c4-023a624c7d1d" />            <img width="225" height="225" alt="download" src="https://github.com/user-attachments/assets/556ce370-2f83-47c5-8a2c-642ebc10e113" />

![download](https://github.com/user-attachments/assets/fe13b6ac-7631-4a8f-afe9-45c6aae90ab1)

#  gprMax Automated Integration & Fidelity Testing

> **Standardizing EM Simulation Validation through Automated CI/CD & Geometric Integrity Gates.**

This repository serves as the **Proof of Concept (PoC)** for the GSoC '26 proposal: "CI/CD + Physics Automation for gprMax." It bridges the gap between raw simulation output and scientific accuracy by implementing a fully automated validation pass.

---

## 🚀 The Core Workflow
This project simulates a complete user workflow in a single automated pass:
1. **Model Execution:** Dynamically provisions a Python environment to run gprMax models.
2. **Output Extraction:** Programmatically extracts simulation results from `.out` files.
3. **Fidelity Verification:** Compares live results against a **'Golden Reference'** dataset.

## 🛠️ Key Technical Features

### 1. Continuous Integration (GitHub Actions)
The workflow doesn't just run code; it builds the environment:
* **Dynamic Provisioning:** Automatically installs gprMax directly from the source repository.
* **Environment Locking:** Ensures reproducibility across different runner architectures.

### 2. Regression Testing (NRMSE Logic)
To ensure scientific integrity, we implement **Normalized Root Mean Square Error (NRMSE)** calculations.
* **Logic:** If the deviation between the live simulation and the Golden Reference exceeds the precision threshold ($\pm 0.001$m), the build fails.
* **Goal:** Catch regressions in the simulation engine before they reach production.

### 3. Geometric Fidelity
* Automated validation of geometric models to ensure spatial accuracy in EM simulations.

---

## 📊 Proof of Implementation
* **Terminal Output:** End-to-end synchronization verified between the engine and validation logic.
* **Integration Tests:** Verifying data flow from solver to post-processor.

---

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **Automation:** GitHub Actions
* **Physics Engine:** gprMax (Source-built)
* **Math/Stats:** NumPy (for NRMSE calculation), Matplotlib (for visualization)

---

## 📂 Repository Structure
* `scripts/`: Integration and regression testing logic.
* `.github/workflows/`: CI configuration for automated environment setup.
* `data/`: Golden Reference datasets for validation.
