import sys
import os

if sys.argc == 1:
    os.system('python scratch.py < input.txt')
else:
    os.system('python solutions/{0}.py < inputs/{0}.txt'.format(sys.argv[1]))