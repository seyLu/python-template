#!/usr/bin/env python

"""Docstring for script."""

__author__ = "seyLu"
__github__ = "github.com/seyLu"

__licence__ = "MIT"
__version__ = "0.0.1"
__maintainer__ = "seyLu"
__status__ = "Prototype"

import logging
from logging.config import fileConfig
from pathlib import Path

Path("logs").mkdir(exist_ok=True)
fileConfig("logging.ini")


if __name__ == "__main__":
    """
    Insert script here.
    """
    logging.info("Script working fine.")
