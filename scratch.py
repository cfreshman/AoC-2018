import math
import re
import hashlib
import json
import copy
from collections import Counter

import sys
with open(sys.argv[1]) as file:
    lines = file.read().splitlines()

