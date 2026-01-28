#script checking if virtual environment is active#
import sys

if sys.prefix != sys.exec_prefix:
    print("Virtual environment is active.")
else:
    print("Virtual environment is not active.")