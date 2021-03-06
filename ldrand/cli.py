"""
Basic command line interface
"""
import os
from typing import List

from ldrand.linker import process_linker
from ldrand.constants import BIN_PATH, VERSION


def run(args: List[str]):
    """
    Processes the arguments and calls the linker wrapper
    :param args: arguments to process
    """
    process_linker(args)


def runp():
    """
    Outputs the path to the ``bin`` folder
    """
    print(BIN_PATH)


def runv():
    """
    Outputs program version
    """
    print(VERSION)
