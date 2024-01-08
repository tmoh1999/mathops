from basicops import *
from advancedops import *
import math
import time
import matplotlib.pyplot as plt

##Test integral of expo(-x^2)
x1=ReelNumber([1,5],[],'+')
x2=ReelNumber([1,5],[],'-')

t=time.time()

r1=expointeg(x1,2000,200)
r2=expointeg(x2,2000,200)
rf=operation(r1,r2,'-')
# n=len(e.part_decimal)
# nb=n//5
# for i in range(nb):
#     start=i*5
#     print(e.part_decimal[start:start+5])
#     print()

print("expintegral(",x1,")==",r1)
print()
print("expintegral(",x2,")==",r2)
print()
print()
print("Final Integral==  expintegral(",x1,")-expintegral(",x2,") ====",rf)
print()


#print("expintegral(",x,")==",expintegral2(1))


# print()
# print(" len(part whole)=",len(e.part_whole))
# print(" len(part dec)=",len(e.part_decimal))

print()
print("TIME:: ",time.time()-t) 



