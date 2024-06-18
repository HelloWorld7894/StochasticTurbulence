"""
All visualisations are done in OpenCV (TODO: migrate to PyGame)
"""

import time

import cv2
import numpy as np
import matplotlib
matplotlib.use('TkAgg')

import math
import matplotlib.pyplot as plt

class GraphicsObject:
    def __init__(self, map_size = 1000, block = True, timestamp = 1):
        self.map_size = map_size
        self.map = np.full((map_size, map_size, 3), (255, 255, 255), dtype=np.uint8)
        self.time = timestamp * 1000
        self.block = block

    def update_particles(self, particles):
        for particle in particles:
            cv2.circle(self.map, (round(particle.position[0]), round(particle.position[1])), 8, color=particle.color, thickness=-1)

    def update_position(self, coords):
        cv2.drawMarker(self.map, coords, color=[0, 0, 255], thickness=1, 
        markerType= cv2.MARKER_TILTED_CROSS, line_type=cv2.LINE_AA,
        markerSize=5)

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
    def __init__(self):
        pass

    def plot_points(self, points):
        plt.plot(points[0], points[1])
        plt.show()

    def show(self):
        plt.show()

    def close(self):
        plt.close()

if __name__ == "__main__":
    plot_obj = PlottingObject()
    plot_obj.show()

    xpoints = np.array([0, 6, 12])
    ypoints = np.array([0, 250, 125])

    plot_obj.plot_points([xpoints, ypoints])