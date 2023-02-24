Number_1 = int(input("What one number? "))
Number_2 = int(input("What two number? "))
import math
# Functions
def Plus():
   if WhatNeed == 1:
    print(Number_1 + Number_2)
def Minus():
    print(Number_1 - Number_2)
def Dellint():
    print(Number_1 / Number_2)
def X():
    print(Number_1 * Number_2)
def Exp(a,b):
    out = a
    for _ in range(b-1):
        out *=a
    return out
def SQRT(a):
    return math.sqrt(a)
WhatNeed = int(input("1. + 2. - 3. X 4. / 5. Exponentiation (Number_2: Degree). 6. Square root (Number_1);"))
if WhatNeed == 1:
    Plus()
elif WhatNeed == 2:
    Minus()
elif WhatNeed == 3:
    X()
elif WhatNeed == 4:
    Dellint()
elif WhatNeed == 5:
    print(Exp(Number_1,Number_2))
elif WhatNeed == 6:
    print(SQRT(Number_1))
else:
    print("Unknown operation")
