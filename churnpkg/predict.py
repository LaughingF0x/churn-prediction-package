import pandas as pd

def churn_probability_for_customer(df: pd.DataFrame, customer_id: int) -> float:
    """
    Returns the churn probability for exactly one customer_id.
    Requires columns: CustomerId, churn_probability
    """
    required = {"CustomerId", "churn_probability"}
    missing = required - set(df.columns)
    if missing:
        raise KeyError(f"Dataset is missing required columns: {sorted(missing)}")

    if not (df["CustomerId"] == customer_id).any():
        raise ValueError(f"CustomerId {customer_id} does not exist in the dataset.")

    prob = df.loc[df["CustomerId"] == customer_id, "churn_probability"].iloc[0]

    if pd.isna(prob):
        raise ValueError(f"Churn probability is missing for CustomerId {customer_id}.")

    return float(prob)