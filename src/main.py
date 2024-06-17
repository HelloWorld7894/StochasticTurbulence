from scenarios import Scenario
from utils import read_config
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-c", "--config")

#sim
if __name__ == "__main__":
    args = parser.parse_args()
    config_file = read_config(args.config)

    Scenario(config_file)