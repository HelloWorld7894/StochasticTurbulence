"""
All visualisations are done in OpenCV (TODO: migrate to PyGame)
"""

import cv2
import numpy as np
import matplotlib
import math

class GraphicsObject:
    def __init__(self, map_size = 1000, block = True, timestamp = 1):
        self.map_size = map_size
        self.map = np.full((map_size, map_size, 3), (255, 255, 255), dtype=np.uint8)
        self.time = timestamp * 1000
        self.block = block

    def update_particles(self, particles):
        for particle in particles:
            cv2.circle(self.map, (round(particle.position[0]), round(particle.position[1])), 8, color=particle.color, thickness=-1)

    def show(self):
        cv2.imshow("graphics", self.map)
        if self.block:
            cv2.waitKey(math.floor(self.time))
        else:
            cv2.waitKey(0)


    def show_loop(self):
        cv2.imshow("graphics", self.map)
        if cv2.waitKey(0) == ord('q'):
            exit(0)
    
    def erase(self):
        self.map = np.full((self.map_size, self.map_size, 3), (255, 255, 255), dtype=np.uint8)

class PlottingObject:
    pass