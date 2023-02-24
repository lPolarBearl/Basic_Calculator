import math
Number_1 = int(input("What one number? "))
Number_2 = int(input("What two number? "))
def Exp(a,b): #exponent
    out = a
    for _ in range(b-1):
        out *=a
    return out
WhatNeed = int(input("1. + 2. - 3. X 4. / 5. Exponentiation (Number_2: Degree). 6. Square root (Number_1);"))
if WhatNeed == 1:
    print(Number_1 + Number_2)
elif WhatNeed == 2:
    print(Number_1 - Number_2)
elif WhatNeed == 3:
    print(Number_1 * Number_2)
elif WhatNeed == 4:
    print(Number_1 / Number_2)
elif WhatNeed == 5:
    print(Exp(Number_1,Number_2))
elif WhatNeed == 6:
    print(math.sqrt(Number_1))
else:
    print("Unknown operation")
