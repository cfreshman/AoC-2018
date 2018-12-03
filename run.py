import sys
import os

if len(sys.argv) < 2:
    os.system('python scratch.py input.txt')
elif sys.argv[1] == 'test':
    os.system('python scratch.py test.txt')
elif sys.argv[1] == 'save':
    os.system('python scratch.py input.txt')
    os.system('cp scratch.py solutions/{0}.py && mv input.txt inputs/{0}.txt'.format(sys.argv[2]))
else:
    os.system('python solutions/{0}.py inputs/{0}.txt'.format(sys.argv[1]))
