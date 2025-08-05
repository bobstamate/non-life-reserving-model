# Non-life Reserving Simulation

This project simulates non-life insurance claims using synthetic data and applies actuarial reserving techniques to estimate future claim payments.

---

## Description

The code simulates insurance claims over a 10-year period, including:

- **Claim generation** using Gamma and Pareto distributions
- **Reporting and payment delays**, drawn from exponential distributions
- Construction of a **payment triangle** based on underwriting and development years

---

## Objectives

- Simulate realistic claims data using statistical distributions
- Model delays in reporting and payments
- Build a development triangle from simulated data
- Apply actuarial techniques to estimate reserves for IBNR (Incurred But Not Reported) claims

---

## Technologies Used

- Python
- `pandas`, `numpy` – data processing & simulation
- `sklearn` – linear regression model
---