import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from robot_localisation.main import main


def run():
    """Entry point for the application script"""
    main()
