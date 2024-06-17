"""
All visualisations are done in OpenCV (TODO: migrate to PyGame)
"""

import cv2
import numpy as np
import matplotlib

class GraphicsObject:
    def __init__(self, map_size = 1000, timestamp = 1):
        self.map = np.full((map_size, map_size, 3), (255, 255, 255), dtype=np.uint8)
        self.time = timestamp * 1000

    def update_particles(self, particles):
        for particle in particles:
            cv2.circle(self.map, (round(particle.position[0]), round(particle.position[1])), 3, color=particle.color, thickness=-1)

    def show(self):
        cv2.imshow("graphics", self.map)
        cv2.waitKey(self.time)

    def show_loop(self):
        cv2.imshow("graphics", self.map)
        if cv2.waitKey(0) == ord('q'):
            exit(0)

class PlottingObject:
    pass