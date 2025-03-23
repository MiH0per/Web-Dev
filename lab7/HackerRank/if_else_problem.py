#https://www.hackerrank.com/challenges/py-if-else/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys

n = int(input())

if(n%2 == 1):
    print("Weird")
elif(n in range(2, 6)):
    print("Not weird")
elif(n in range(6, 21)):
    print("Weird")
else:
    print("Weird")
    
