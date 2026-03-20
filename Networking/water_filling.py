import numpy as np

def water_filling(power_budget: float, noise_levels: np.ndarray):
    """
    Classic water-filling power allocation for parallel channels
    (Max-Min fairness / capacity maximization analogy)
    """
    n = len(noise_levels)
    sorted_idx = np.argsort(noise_levels)
    sorted_noise = noise_levels[sorted_idx]
    
    power = np.zeros(n)
    remaining = power_budget
    
    for i in range(n):
        level = sorted_noise[i]
        channels_left = n - i
        water_level = level + remaining / channels_left
        
        if i < n-1 and water_level > sorted_noise[i+1]:
            continue
            
        for j in range(i, n):
            alloc = max(0, water_level - sorted_noise[j])
            power[sorted_idx[j]] = alloc
            remaining -= alloc * (n - j)
        break
    
    return power

# Example
if __name__ == "__main__":
    noise = np.array([1.0, 2.0, 5.0, 10.0])  # different channel noise
    budget = 20.0
    alloc = water_filling(budget, noise)
    print("Noise levels:   ", noise)
    print("Power allocation:", np.round(alloc, 2))
    print("Total power used:", alloc.sum())