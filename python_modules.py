######  *** MODULES ***   #######
#these are files-pyhton definitions & statements

#syntax
#import module_name------import
#module_name.function_name()-----calling

from day12_functions import *
print(add(1,23))
print(multi(3,24))
print(expo(2,4))
print(sub(1,23))



###### *** MATH Module *** ######
from math import *

print(sqrt(25))#5
print(tan(90))
print(sin(180))
print(pi)#3.14
print(cbrt(27))#3.0
print(remainder(5,2))#1
print(factorial(5))#120
print(gcd(5,10,15,25))#5
print(perm(5,2))#20
print(ceil(5.7))#6
print(fabs(4.9))#4.9
print(floor(4.9))#4
print(fmod(5,2))#1.0
print(remainder(5,2))#1.0
print(modf(3.4))#(0.399999,3.0)---fractional part,integer part
print(trunc(4.5))#4

list_1 = [1,2,3,4,5]
list_2 = [6,7]
print(fsum(list_1))#15
print(fsum(range(11)))#0+1+2+3+4+5+6+7+8+9+10
print(prod(list_1))#1*2*3*4*5

##### *** RANDOM Module *** #####
from random import *


print(randrange(100))#1-99,stop value
print(randrange(1,10,5))#only eligible nos are 1,6 because of step 5, so chooses btw 1 and 6
print(randint(1,3))#--both ends include
list_1 = [1,3,5,7,9,11]
print(choice(list_1))#to choose from sequences
#print(shuffle(list_1))---3.11 version removed
print(random())#Return the next random floating-point number in the range 0.0 <= X < 1.0
print(uniform(2.1,10.1))#Return a random floating-point number N such that a <= N <= b



##### ***** DATETIME Module ***** ######
from datetime import *

print(datetime(2025,1,17,23,14,27,55))
now = datetime.now()
print(now)


#### **** OS Module **** ####

import os
print(os.getcwd())

### *** SYS Modle *** ###
'''
This module provides access to some variables used or maintained by the interpreter 
and to functions that interact strongly with the interpreter.
It is always available. Unless explicitly noted otherwise, all variables are read-only
'''
import sys
print(sys.byteorder)#little/big
print(sys.builtin_module_names)
print(sys.call_tracing(min,(56,55)))
print(sys.copyright)

import sys
sys.path.insert(0,r"path")






