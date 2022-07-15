import argparse
import sys
from simpleCalc.calc import Calculation 
import argparse 


def main():
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

    print(result)


if __name__ == "__main__":
    main()
    