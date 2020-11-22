# Author: Christine Okubo
# Date: 11-16-20
# Input: : Sample 1 data, Sample 2 data, flag (1 = classical KS and 2 = total KS)
# Output: 1) max distance between the two cumulative sample distributions OR
# 2) total difference between the two sample distributions.

def kolmogorovSmirnov (x1, x2, flag):
    import numpy as np
    x1_array = np.array(x1)
    x2_array = np.array(x2)
    combined_array = np.concatenate((x1_array, x2_array), axis=None)
    
    from statsmodels.distributions.empirical_distribution import ECDF
    x1_ecdf = ECDF(x1_array)
    x2_ecdf = ECDF(x2_array)
    
    if flag == 1:
        max = 0
        for i in combined_array:
            if abs(x1_ecdf(i) - x2_ecdf(i)) >= max:
                max = abs(x1_ecdf(i) - x2_ecdf(i))
        return max
    
    elif flag == 2:
        max_value = np.max(combined_array)
        min_value = np.min(combined_array)
        
        x_range = max_value - min_value
        
        total = 0
        value = min_value
        for i in range(1000):
            total += abs(x1_ecdf(value) - x2_ecdf(value))
            value += x_range / 1000
        return total / 1000
        
    else: 
        print("Please input valid flag (1 or 2).")