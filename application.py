import sys

"""
Launches a development server on localhost. You can look at this address in your browser to get the results.
"""

sys.argv = ["runserver"]

execfile("manage.py")
