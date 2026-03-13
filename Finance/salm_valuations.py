import numpy as np
import pandas as pd
from scipy.stats import norm

class SovereignAssetValuator:
    """
    Sovereign Asset & Liability Management (SALM) Engine
    Implements Risk-Adjusted NPV for large-scale territorial assets.
    """
    
    def __init__(self, asset_name, initial_value, target_roi=0.24):
        self.asset_name = asset_name
        self.initial_value = initial_value
        self.target_roi = target_roi # Based on Ambient Systems 24% ROI model

    def monte_carlo_simulation(self, iterations=10000, institutional_risk_factor=0.15):
        """
        Simulates yield outcomes based on 'Institutional Decay' markers.
        institutional_risk_factor: Higher values represent administrative bottlenecks.
        """
        # Mean return set at target ROI, volatility influenced by institutional risk
        mu = self.target_roi 
        sigma = institutional_risk_factor 
        
        simulated_returns = np.random.normal(mu, sigma, iterations)
        
        results = {
            "mean_expected_roi": np.mean(simulated_returns),
            "value_at_risk_95": np.percentile(simulated_returns, 5),
            "confidence_interval": (np.percentile(simulated_returns, 2.5), 
                                   np.percentile(simulated_returns, 97.5))
        }
        return results

    def calculate_adjusted_npv(self, cash_flows, discount_rate, governance_penalty):
        """
        Calculates NPV while applying a 'Governance Penalty' for 
        administrative lags identified in the Digital Twin (PVN Model).
        """
        adjusted_rate = discount_rate + governance_penalty
        npv = sum(cf / (1 + adjusted_rate)**i for i, cf in enumerate(cash_flows))
        return npv

# --- MOCK EXECUTION FOR PORTFOLIO PREVIEW ---
if __name__ == "__main__":
    # Example: 5,600 km2 Territorial Plot or Vertical Farm Portfolio
    valuator = SovereignAssetValuator("Regional Asset Alpha", initial_value=100000000)
    
    print(f"--- Simulation for {valuator.asset_name} ---")
    sim = valuator.monte_carlo_simulation(institutional_risk_factor=0.12)
    print(f"Mean Expected ROI: {sim['mean_expected_roi']:.2%}")
    print(f"95% Confidence Interval: [{sim['confidence_interval'][0]:.2%}, {sim['confidence_interval'][1]:.2%}]")