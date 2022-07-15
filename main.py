import argparse
import sys
from simpleCalc.calc import Calculation 
from CLIParser.parser import parser


def main():
    result = parser()
    print(result)


if __name__ == "__main__":
    main()
    