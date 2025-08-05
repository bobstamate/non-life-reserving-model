import numpy as np
import pandas as pd

# Set random seed for reproducibility
np.random.seed(42)

# Parameters
years = list(range(2015, 2025))  #  10 years simulation
lambda_claims = 100              # Avg claims/year
gamma_alpha = 2
gamma_beta = 3000
pareto_alpha = 2.5
pct_catastrophic = 0.05

# Collect the data
claims_data = []

for year in years:
    n_claims = np.random.poisson(lambda_claims)
    for _ in range(n_claims):
        claim_type = "catastrophic" if np.random.rand() < pct_catastrophic else "moderate"
        if claim_type == "moderate":
            severity = np.random.gamma(shape=gamma_alpha, scale=gamma_beta)
        else:
            u = np.random.rand()
            xm = 10_000
            severity = xm / (1 - u)**(1 / pareto_alpha)

        claims_data.append({
            "underwriting_year": year,
            "claim_type": claim_type,
            "severity": severity
        })

# Transform in DataFrame
claims_df = pd.DataFrame(claims_data)

# Add delays for reporting and payment of claims
report_lambda = 1.2  # λ for reporting delay (avg months)
payment_lambda = 0.18  # λ for payment delay (avg months) => the smaller λ gets, the bigger the avg payment delay

claims_df["report_delay_months"] = np.random.exponential(scale=1/report_lambda, size=len(claims_df)).round().astype(int)
claims_df["payment_delay_months"] = np.random.exponential(scale=1/payment_lambda, size=len(claims_df)).round().astype(int)

# we compute the years of reporting and payment of a claim
claims_df["report_year"] = claims_df["underwriting_year"] + (claims_df["report_delay_months"] // 12)
claims_df["payment_year"] = claims_df["underwriting_year"] + (claims_df["payment_delay_months"] // 12)

current_year = 2025
claims_df = claims_df[claims_df["payment_year"] <= current_year]  # limit to the current year since we don't know when the claims from the previous underwriting year(s) will be reported/paid

# Result
print(claims_df.head())

# We compute development year as a diff between payment year and underwriting year
claims_df["development_year"] = claims_df["payment_year"] - claims_df["underwriting_year"]

# we aggregate the sum of claims for each pair of underwriting year and development year
triangle = claims_df.pivot_table(
    index="underwriting_year",
    columns="development_year",
    values="severity",
    aggfunc="sum",
    fill_value=0
).sort_index() # 0 = same year

# Display of table
print(triangle)