import numpy as np

def calculate_turbulence(X_prev, spd, dt, D, alpha, rand_dist_func):
    """
        Calculate turbulence stochastic way, basically an recursive function that updates particle position every time
        Args:
            X_prev = 
            spd = 
            dt = 
            D = 
            alpha = 
            rand_dist_func = random distribution function (like normal dist., exponential dist.)
    """
    return X_prev + spd * dt + ((D * dt) ** (1/alpha)) * rand_dist_func