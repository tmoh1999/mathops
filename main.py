from basicops import *
from advancedops import *
import math
import time
import matplotlib.pyplot as plt

##NOTE:Devision Test
# nb1=ReelNumber([9],[5,3,5,3],'-')
# nb2=ReelNumber([0],[7,9],'-')
# nb3=ReelNumber([1],[0],'+')
# nb4=ReelNumber([2],[3,0,0,0,0,0,0,0,0,0,0,0],'+')
# nb5=ReelNumber([1],[0,5,7],'+')
# nb6=ReelNumber([1,2],[3,0,0,0,0,0,5,0,0,0,0,0],'+')




# nb1=ReelNumber([3,9,4,9,6,1,1,0,3],[0],'-')
# nb2=ReelNumber([2,4,0],[0,5,6],'-')
# nb3=ReelNumber([9],[0,4,2],'+')
# nb4=ReelNumber([8],[5,1,7],'+')
# nb5=ReelNumber([1,5,0],[8,4,2],'+')
# nb6=ReelNumber([0],[1,0,0,0,0,0,0,0,0,0,0,0],'+')

# operation(nb1,nb2,"/")
# operation(nb3,nb4,"/")
# operation(nb5,nb6,"/")


# operation(nb1,nb2,"/")
# operation(nb3,nb4,"/")
# operation(nb5,nb6,"/")

# operation(nb2,nb1,"/")
# operation(nb4,nb3,"/")
# operation(nb6,nb5,"/")


# operation(nb2,nb3,"/")
# operation(nb1,nb3,"/")
# operation(nb1,nb5,"/")


# operation(nb2,nb4,"/")
# operation(nb4,nb6,"/")
# operation(nb3,nb5,"/")
        
##NOTE:Power test
# nb1=ReelNumber([1],[2],'+')
# nb2=ReelNumber([6],[0],'-')

# nb3=ReelNumber([2],[7,1],'+')
# nb4=ReelNumber([8],[0,0,0,0,0,0,0,0,0,0,0,0],'+')

# nb5=ReelNumber([2],[7,1],'-')
# nb6=ReelNumber([1,0],[0,0,0,0,0,0,0,0,0,0,0,0],'-')

# nb7=ReelNumber([1],[0],'-')
# nb8=ReelNumber([7],[0,0,0,0,0,0,0,0,0,0,0,0],'+')


# PosIntPow(nb1,nb2)
# PosIntPow(nb3,nb4)
# PosIntPow(nb5,nb6)
# x=PosIntPow(nb7,nb8)

# ##NOTE: TEst facto
# number=ReelNumber([0],[],'+')
# for i in range(100):
#     fact=facto(number)
#     print()
#     print(number," ! =",fact)
#     number=operation(number,ReelNumber([1],[],'+'),'+')

##Test Expo
a=0.0964036
b=1.52997
c=0.5
s=0
for x in range(1,40+1):
    s+=(a*x*x+b*x+c)
print("ssss:",s)
print()
x=ReelNumber([1,0,0,0],[],'-')
t=time.time()
e,xz=expo(x,2000,600)

n=len(e.part_decimal)
nb=n//5
for i in range(nb):
    start=i*5
    print(e.part_decimal[start:start+5])
    print()

print("exp(",x,")==",e)


print()
print(" len(part whole)=",len(e.part_whole))
print(" len(part dec)=",len(e.part_decimal))

print()
print("TIME:: ",time.time()-t) 

n=600//50 +1
ll=[i  for i in range(1,n)]
a=0.0964036
b=1.52997
c=0.5
ll2=[a*math.pow(x,2)+b*x+c for x in ll]

xz2=list(zip(ll,ll2))
xz3=list(zip(ll,ll))

plt.scatter(*zip(*xz))
plt.scatter(*zip(*xz2))
plt.scatter(*zip(*xz3))

plt.show()
# x=ReelNumber([1,6],[],'+')
# print("exp(",x,")==",expo(x))
# print()
# print()
# print("TIME:: ",time.time()-t)

# x=ReelNumber([5,5],[],'+')
# print("exp(",x,")==",expo2(x))
# print()
# print()
# print("TIME:: ",time.time()-t)

# x=ReelNumber([3],[],'-')
# print("exp(",x,")==",expo2(x))
# print()
# print()
# print("TIME:: ",time.time()-t)

# x=ReelNumber([1,5],[0],'-')
# print("exp(",x,")==",expo2(x))
# print()
# print()
# print("TIME:: ",time.time()-t)

# x=ReelNumber([5,5],[1,2,3],'+')
# print("exp(",x,")==",expo2(x))
# print()
# print()
# print("TIME:: ",time.time()-t)

# x=ReelNumber([3,0],[5,5],'-')
# print("exp(",x,")==",expo2(x))
# print()
# print()
# print("TIME:: ",time.time()-t)

