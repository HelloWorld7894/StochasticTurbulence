from scenarios import Scenario

#some settings (TODO, rewrite them into config?)
N_ITER = 5
N_PARTICLES = 2
TIME_PAD = 1
SCENARIO_NAME = "turbulence-free"

#sim
if __name__ == "__main__":
    Scenario([N_ITER, N_PARTICLES, TIME_PAD, SCENARIO_NAME])