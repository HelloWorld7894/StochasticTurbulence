from utils import calculate_turbulence, alpha_stable_dist, random_generate_color, calculate_dist, calculate_richardson_ratio
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
        self.n_sim = args["n_sim"]
        self.n_iter = args["n_iter"]
        self.n_particles = args["n_particles"]
        self.timestamp = args["timestamp"]
        self.graphing = args["run_graphing"]
        self.plotting = args["run_plotting"]
        self.non_block = args["nonblocking_graphing"]
        self.map_size = args["map_size"]
        self.sim_properties = {}
        
        for sim_property in args["simulation_properties"]:
            self.sim_properties[list(sim_property.keys())[0]] = list(sim_property.values())[0]

        #create other callback classes
        self.gui_obj = None
        self.plot_obj = None

        if self.graphing:
            self.gui_obj = GraphicsObject(map_size=self.map_size, block=self.non_block, timestamp=self.timestamp)

        if self.plotting:
            self.plot_obj = PlottingObject()

        # Assign turbulence callback
        self.turbulence_callback = None
        turbulence_name = self.sim_properties["scenario_name"]
        if turbulence_name == "turbulence-free":
            self.turbulence_callback = self.turbulence_free
        elif turbulence_name == "turbulence-box":
            self.turbulence_callback = self.turbulence_in_box
        elif turbulence_name == "turbulence-in-coffee":
            self.turbulence_callback = self.turbulence_in_coffee

        self.distances = []
        self.times = []

    def run(self):
        # Run simulation

        for i_sim in range(self.n_sim):
            self.particles = []
            self.regenerate_particles()
            self.gui_obj.erase()

            start = time.time()
            for i in range(self.n_iter):

                for particle in self.particles:
                    particle.update()

                if self.graphing:
                    #render change
                    self.gui_obj.update_particles(self.particles)
                    self.gui_obj.update_position(self.sim_properties["default_coords"])
                    self.gui_obj.show()
                else:
                    time.sleep(self.timestamp)

            end = time.time()
            elapsed_time = end - start

            particle_dist = calculate_dist(self.particles)
            print(f"distance: {particle_dist}, time: {elapsed_time}")
            self.turbulence_callback(particle_dist, self.particles, elapsed_time)

        distance_all = sum(self.distances) / len(self.distances)
        time_all = sum(self.times) / len(self.times)
        ratio = calculate_richardson_ratio(distance_all, time_all)

        print("Done!")
        print("Distance: " + str(distance_all))
        print("Time: " + str(time_all))
        print("Ratio: " + str(ratio))
        if self.graphing:
            self.gui_obj.show_loop()

        return distance_all

    def regenerate_particles(self):
        self.particles = []
        for i_particle in range(self.n_particles):
            x_p = self.sim_properties["default_coords"][0]
            y_p = self.sim_properties["default_coords"][1]

            spd1 = self.sim_properties["particle_speed"][0] #generate_random(5)
            spd2 = self.sim_properties["particle_speed"][1] #generate_random(5)

            self.particles.append(Particle((x_p, y_p), (spd1, spd2), self.timestamp, self.sim_properties["diffusion_coef"], self.sim_properties["alpha"]))

    def turbulence_free(self, distance, particles, time):
        self.distances.append(distance)
        self.times.append(time)
    def turbulence_in_box(self, distance, particles, time):
        #TODO: rework to a version that does not throw particles away but calculates it
        diff_x = abs(particles[0].position[0] - particles[1].position[0])
        diff_y = abs(particles[0].position[1] - particles[1].position[1])

        if diff_x > self.sim_properties["box_size"][0]:
            return
        if diff_y > self.sim_properties["box_size"][1]:
            return

        self.distances.append(distance)
        self.times.append(time)

class BoxApproximation(Scenario):
    def __init__(self, args):
        super().__init__(args)

    def run_approx(self):
        self.run()