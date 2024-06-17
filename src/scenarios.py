from utils import calculate_turbulence, generate_random
import time

class Particle:
    def __init__(self, loc, v):
        self.position = loc

    def update(self):
        loc_updated = (self.position[0] + 1, self.position[1] + 1)
        self.position = loc_updated

class Scenario:
    def __init__(self, args):
        #inner functionalities
        self.particles = []
        for i_particle in range(args[1]):
            x_p = generate_random(15)
            y_p = generate_random(10)
            self.particles.append(Particle((x_p, y_p), 3))

        self.scenario_args = args

        # Assign turbulence callback
        self.turbulence_callback = None
        turbulence_name = args[3]
        if turbulence_name == "turbulence-free":
            self.turbulence_callback = self.turbulence_free
        elif turbulence_name == "turbulence-in-box":
            self.turbulence_callback = self.turbulence_in_box
        elif turbulence_name == "turbulence-in-coffee":
            self.turbulence_callback = self.turbulence_in_coffee

        # Run simulation
        for i in range(args[0]):
            time.sleep(args[2])
            self.turbulence_callback()
            for particle in self.particles:
                particle.update()
                print(particle.position)

    def turbulence_free(self):
        pass
    def turbulence_in_box(self):
        pass
    def turbulence_in_coffee(self):
        pass