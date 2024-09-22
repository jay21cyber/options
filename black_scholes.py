import streamlit as st
import numpy as np
from scipy.stats import norm

# Black-Scholes formula for call/put pricing
def black_scholes(S, K, T, r, sigma, option_type="call"):
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)

    if option_type == "call":
        price = S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    else:
        price = K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)

    return price

# Streamlit interface
st.title("Black-Scholes Option Pricing")

# User inputs for option parameters
S = st.number_input("Current Asset Price (S)", min_value=0.0, value=100.0)
K = st.number_input("Strike Price (K)", min_value=0.0, value=100.0)
T = st.number_input("Time to Maturity (Years, T)", min_value=0.01, value=1.0)
r = st.number_input("Risk-Free Interest Rate (r) in %", min_value=0.0, value=5.0) / 100
sigma = st.number_input("Volatility (σ) in %", min_value=0.0, value=20.0) / 100

# Option type selection (Call or Put)
option_type = st.selectbox("Option Type", ("Call", "Put"))

# Calculate option price based on Black-Scholes
if st.button("Calculate Price"):
    price = black_scholes(S, K, T, r, sigma, option_type.lower())
    st.write(f"The Black-Scholes {option_type} option price is: {price:.2f}")
