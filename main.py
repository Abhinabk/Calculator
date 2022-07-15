import argparse
import sys
from simpleCalc.calc import Calculation 
from CLIParser.parser import parser


def main(argv=None):
    # argv=None helps in code testing
    result = parser(argv)
    print(result)


if __name__ == "__main__":
    main()
    