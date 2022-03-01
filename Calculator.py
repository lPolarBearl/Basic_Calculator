# Basic calculator
Number_1 = int(input("What one number? "))
Number_2 = int(input("What two number? "))
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
WhatNeed = int(input("1. + 2. - 3. X 4. / ;" ))
if WhatNeed == 1:
    Plus()
    
elif WhatNeed == 2:
    Minus()
elif WhatNeed == 3:
    X()
elif WhatNeed == 4:
    Dellint()
else:
    print("Unknown opiration.")