import numpy as np
import time

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

def scenario_main(args):
    for i in range(args[0]):
        time.sleep(args[2])
        for i_particle in range(args[1]):
            #calculate_turbulence() #TODO
            pass