import argparse
import sys
from simpleCalc.calc import Calculation 

def parser(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument("exp",nargs='?', type=str,
                        help="display the expression ")

    parser.add_argument("-c", "--calc",
                        help="calculate the expression")
    # uses syste.arg if None
    args = parser.parse_args(argv)

    result = args.exp

    if args.calc:
        result = Calculation.calculate(args.calc)

    return result