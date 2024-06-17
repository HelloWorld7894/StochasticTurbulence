from utils import calculate_turbulence
import time

class Scenario:
    def __init__(self, args):
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

        for i in range(args[0]):
            time.sleep(args[2])
            self.turbulence_callback()
            for i_particle in range(args[1]):
                #calculate_turbulence() #TODO
                pass

    def turbulence_free(self):
        print("Free!")
    def turbulence_in_box(self):
        print("Not so free!")
    def turbulence_in_coffee(self):
        print("R O T U N D")