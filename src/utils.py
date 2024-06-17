import numpy as np
import scipy
import random
import yaml

#variables
already_generated_colors = []

def generate_random(high, low = 0):
    return np.random.randint(low, high)

def alpha_stable_dist(alpha = 2/3, beta = 0.5): #TODO
    distribution = scipy.stats.levy_stable(alpha, beta)
    return distribution.rvs()

def calculate_turbulence(X_prev, spd, dt, D, alpha, rand_dist_func):
    """
        Calculate turbulence stochastic way, basically an recursive function that updates particle position every time
        Args:
            X_prev = 
            spd = 
            dt = 
            D = 
            alpha = 
            rand_dist_func = random distribution function (like normal dist., exponential dist. and alpha-stable dist.)
    """
    res = X_prev + spd * dt + ((D * dt) ** (1/alpha)) * rand_dist_func()
    return res

def random_generate_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    if (r, g, b) not in already_generated_colors:
        already_generated_colors.append((r, g, b))
    else:
        random_generate_color()

    return (r, g, b)

def read_config(path):
    with open(path) as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
            exit(1)