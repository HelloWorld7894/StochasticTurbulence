from utils import calculate_turbulence, generate_random, alpha_stable_dist, random_generate_color
from vis import GraphicsObject, PlottingObject

import time
import numpy as np

class Particle:
    def __init__(self, loc, v, timestamp, d_coef, alpha):
        self.position = np.array(loc)
        self.speed = np.array(v)
        self.time = timestamp
        self.d = d_coef
        self.alpha = alpha
        self.color = random_generate_color()

    def update(self):
        self.position = calculate_turbulence(self.position,
                                             self.speed,
                                             self.time,
                                             self.d,
                                             self.alpha,
                                             alpha_stable_dist)

class Scenario:
    def __init__(self, args):
        #inner functionalities
        self.scenario_args = args
        self.particles = []
        for i_particle in range(args[1]):
            x_p = generate_random(15)
            y_p = generate_random(10)
            self.particles.append(Particle((x_p, y_p), (3, 3), args[2], args[3], args[4]))

        #create other callback classes
        self.gui_obj = None
        self.plot_obj = None

        if args[6]:
            self.gui_obj = GraphicsObject()

        if args[7]:
            self.plot_obj = PlottingObject()

        # Assign turbulence callback
        self.turbulence_callback = None
        turbulence_name = args[5]
        if turbulence_name == "turbulence-free":
            self.turbulence_callback = self.turbulence_free
        elif turbulence_name == "turbulence-in-box":
            self.turbulence_callback = self.turbulence_in_box
        elif turbulence_name == "turbulence-in-coffee":
            self.turbulence_callback = self.turbulence_in_coffee

        # Run simulation
        for i in range(args[0]):
            self.turbulence_callback()
            for particle in self.particles:
                particle.update()
                print(particle.position)

            if args[6]:
                #render change
                self.gui_obj.update_particles(self.particles)
                self.gui_obj.show()
            else:
                time.sleep(args[2])

            #if args[7]:
                #render plots

        print("Done!")
        if args[6]:
            self.gui_obj.show_loop()

    def turbulence_free(self):
        pass
    def turbulence_in_box(self):
        pass
    def turbulence_in_coffee(self):
        pass