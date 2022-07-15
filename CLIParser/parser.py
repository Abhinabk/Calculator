import argparse
import sys
from simpleCalc.calc import Calculation 

def parser():
       # TODO parse the agument from the commandline stroe in a stack and add the values
    parser = argparse.ArgumentParser()
    parser.add_argument("exp",nargs='?', type=str,
                        help="display the expression ")

    parser.add_argument("-c", "--calc",
                        help="calculate the expression")

    args = parser.parse_args()

    result = args.exp

    if args.calc:
        result = Calculation.calculate(args.calc)

    return result