import sys
from argparse import ArgumentParser
from importlib.metadata import version


def entry_point():
    parser = ArgumentParser()
    parser.add_argument("-v", "--version", action="store_true")

    args = parser.parse_args()

    if args.version:
        print(version("gha_python_packaging_demo"))
        sys.exit()
