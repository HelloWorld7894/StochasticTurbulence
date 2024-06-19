from scenarios import Scenario, BoxApproximation
from utils import read_config
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-c", "--config")

#sim
if __name__ == "__main__":
    args = parser.parse_args()
    config_file = read_config(args.config)

    #Type 1
    scenario = Scenario(config_file)
    scenario.run()

    #Type 2    
    #scenario = BoxApproximation(config_file)
    #scenario.run()