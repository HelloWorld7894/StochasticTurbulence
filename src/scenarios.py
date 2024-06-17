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
        #argument variables
        self.n_iter = args["n_iter"]
        self.n_particles = args["n_particles"]
        self.timestamp = args["timestamp"]
        self.graphing = args["run_graphing"]
        self.plotting = args["run_plotting"]
        self.sim_properties = {}
        
        for sim_property in args["simulation_properties"]:
            self.sim_properties[list(sim_property.keys())[0]] = list(sim_property.values())[0]

        #inner functionalities
        self.scenario_args = args
        self.particles = []
        for i_particle in range(self.n_particles):
            x_p = generate_random(15)
            y_p = generate_random(10)
            self.particles.append(Particle((x_p, y_p), (3, 3), self.timestamp, self.sim_properties["diffusion_coef"], self.sim_properties["alpha"]))

        #create other callback classes
        self.gui_obj = None
        self.plot_obj = None

        if self.graphing:
            self.gui_obj = GraphicsObject()

        if self.plotting:
            self.plot_obj = PlottingObject()

        # Assign turbulence callback
        self.turbulence_callback = None
        turbulence_name = self.sim_properties["scenario_name"]
        if turbulence_name == "turbulence-free":
            self.turbulence_callback = self.turbulence_free
        elif turbulence_name == "turbulence-in-box":
            self.turbulence_callback = self.turbulence_in_box
        elif turbulence_name == "turbulence-in-coffee":
            self.turbulence_callback = self.turbulence_in_coffee

        # Run simulation
        for i in range(self.n_iter):
            self.turbulence_callback()
            for particle in self.particles:
                particle.update()
                print(particle.position)

            if self.graphing:
                #render change
                self.gui_obj.update_particles(self.particles)
                self.gui_obj.show()
            else:
                time.sleep(args[2])

            #if self.plotting:
                #render plots

        print("Done!")
        if self.graphing:
            self.gui_obj.show_loop()

    def turbulence_free(self):
        pass
    def turbulence_in_box(self):
        pass
    def turbulence_in_coffee(self):
        pass