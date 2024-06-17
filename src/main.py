from scenarios import turbulence_free, turbulence_in_box, turbulence_in_coffee

#some settings (TODO, rewrite them into config?)
N_ITER = 5
N_PARTICLES = 2
TIME_PAD = 1

#sim
if __name__ == "__main__":
    turbulence_free([N_ITER, N_PARTICLES, TIME_PAD])