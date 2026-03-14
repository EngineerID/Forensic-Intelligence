import numpy as np
import pandas as pd
from scipy.stats import norm

class SovereignAssetValuator:
    """
    Sovereign Asset & Liability Management (SALM) Engine.
    Now integrated with Graph-derived 'Value at Risk' (VaR) metrics.
    """
    
    def __init__(self, asset_name, initial_value, target_roi=0.24):
        self.asset_name = asset_name
        self.initial_value = initial_value
        self.target_roi = target_roi 

    def calculate_governance_penalty(self, total_lag_days, value_at_risk):
        """
        Translates Graph bottlenecks into a basis-point penalty.
        Penalty = (Total Lag / 365) * (VaR / Initial Value)
        """
        # Normalizing the impact of administrative friction on the discount rate
        impact_ratio = value_at_risk / self.initial_value
        time_decay = total_lag_days / 365
        
        # Returns penalty in decimal form (e.g., 0.02 for 200 bps)
        return round(impact_ratio + time_decay, 4)

    def monte_carlo_simulation(self, iterations=10000, institutional_risk_factor=0.15):
        """
        Simulates yield outcomes based on 'Institutional Decay' markers.
        """
        mu = self.target_roi 
        sigma = institutional_risk_factor 
        
        simulated_returns = np.random.normal(mu, sigma, iterations)
        
        return {
            "mean_expected_roi": np.mean(simulated_returns),
            "value_at_risk_95": np.percentile(simulated_returns, 5),
            "confidence_interval": (np.percentile(simulated_returns, 2.5), 
                                   np.percentile(simulated_returns, 97.5))
        }

    def calculate_sovereign_npv(self, cash_flows, discount_rate, total_lag_days, value_at_risk):
        """
        The 'Fiduciary Hammer': Adjusts NPV based on real-time Graph bottlenecks.
        """
        penalty = self.calculate_governance_penalty(total_lag_days, value_at_risk)
        adjusted_rate = discount_rate + penalty
        
        npv = sum(cf / (1 + adjusted_rate)**i for i, cf in enumerate(cash_flows))
        return npv, penalty

# --- CONNECTED EXECUTION ---
if __name__ == "__main__":
    # Context: A $100M Sovereign Infrastructure Project
    valuator = SovereignAssetValuator("Strategic Asset Alpha", initial_value=100_000_000)
    
    # Data derived from the Cypher 'Forensic Leakage' Query
    graph_lag_days = 23 
    graph_var = 340_000 # Cumulative value at risk from bottlenecks
    
    # Standard discount rate (e.g., WACC)
    base_discount = 0.08 
    projected_cash_flows = [0, 20M, 25M, 30M, 35M] # 5-year outlook

    npv, penalty_bps = valuator.calculate_sovereign_npv(
        projected_cash_flows, base_discount, graph_lag_days, graph_var
    )
    
    print(f"--- Fiduciary Audit: {valuator.asset_name} ---")
    print(f"Institutional Bottleneck Penalty: {penalty_bps * 10000:.0f} bps")
    print(f"Risk-Adjusted Sovereign NPV: ${npv:,.2f}")
    
    if penalty_bps > 0.05:
        print("ALERT: FIDUCIARY BREACH THRESHOLD MET. INITIATING STRUCTURAL DEFENSE.")