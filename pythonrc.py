# Place something like the following in your ~/.bashrc
# export PYTHONSTARTUP="/home/brandyn/projects/pythonrc/pythonrc.py"
print("# Brandyn's pythonrc.py - The following has been executed for you")
___commands = """import hadoopy, os, sys, glob, Image, cv, json
import cPickle as pickle
import numpy as np"""
print(___commands)
exec(___commands)
del ___commands
