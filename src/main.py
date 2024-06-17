from scenarios import Scenario

#some settings (TODO, rewrite them into config?)
N_ITER = 5
N_PARTICLES = 2
TIMESTAMP = 1
DIFFUSION_COEF = 3
SCENARIO_NAME = "turbulence-free"
ALPHA = 2/3 #to simulate turbulent environment
RUN_GRAPHING = True
RUN_PLOTTING = True

#sim
if __name__ == "__main__":
    Scenario([N_ITER, N_PARTICLES, TIMESTAMP, DIFFUSION_COEF, ALPHA, SCENARIO_NAME, RUN_GRAPHING, RUN_PLOTTING])