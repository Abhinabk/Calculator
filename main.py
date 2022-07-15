import argparse
from simpleCalc.calc import Calculation 
import argparse 


def main():
    # TODO parse the agument from the commandline stroe in a stack and add the values

    parser = argparse.ArgumentParser()
    parser.add_argument('add_ip',type=str,help='adds input')
    args = parser.parse_args()
    Calculation.add(args.add_ip)
    # print(vars(args))

if __name__ == "__main__":
    main()