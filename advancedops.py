from basicops import *
import time
import math
def facto(n:ReelNumber):
    number_zero=ReelNumber([],[],'+')
    number_one=ReelNumber([1],[],'+')
    number=ReelNumber(n.part_decimal.copy(),[],'+')
    cmp=comparePosNumbers(number_zero,number)
    #print()
    if cmp==0:
        #calc fact
        cmp=comparePosNumbers(number_zero,n)
        if cmp==0:
            #0!
            #print(n," ! = ",number_one)
            return number_one
        else:
            #1!
            cmp=comparePosNumbers(number_one,n)
            if cmp==0:
                #print(n," ! = ",number_one)
                return number_one
            else:
                #n!
                fact=ReelNumber([2],[],'+')
                f=ReelNumber([3],[],'+')
                cmp=comparePosNumbers(f,n)
                while(cmp<=0):
                    fact=operation(fact,f,'*')
                    f=operation(f,number_one,'+')
                    cmp=comparePosNumbers(f,n)
                    # print("Loop:")
                    # print("  f:",f)
                    # print("  fact:",fact)
                #print(n," ! = ",fact)
                return fact



    else:
        print()
        print("Math Error : can't calculate fact of float")    


def expo(x1:ReelNumber,nbtimes=100,nbplus=200,nbplus2=600):
    number_one=ReelNumber([1],[],'+')
    x=x1.copyReelNumber()
    if x.signe=='-':
        x.signe='+'
    

    n=ReelNumber([],[],'+')
    res=ReelNumber([1],[],'+')
    un=number_one.copyReelNumber()

    
    t=time.time()
    list_t=[]
    list_i=[]
    cpt=1
    for i in range(nbtimes+1):

        n=operation(n,number_one,'+')
        #print("n==",n)
        alpha=operation(x,n,'/',nbplus)
        #print("  alpha==",alpha)
        un=operation(un,alpha,'*')
        #print("  un==",un)
        
        if len(un.part_decimal)>nbplus:
            un.part_decimal=un.part_decimal[:nbplus]
        res=operation(res,un,'+')
        if (i+1) % 50==0:
            t1=time.time()-t
            list_t.append(int(t1))
            list_i.append(cpt)
            cpt+=1
            print(i,"  TIME:",t1)
            print()
            print("    ->>>  len(part whole)=",len(res.part_whole))
            print("    ->>>  len(part dec)=",len(res.part_decimal))
            print("      ->>>   ",res)
            print()
            print()
            t=time.time()
    if x1.signe=='-':
        res=operation(number_one,res,'/',nbplus2)
    elif len(res.part_decimal)>nbplus:
        res.part_decimal=res.part_decimal[:nbplus]
    print(list_i)
    print(list_t)
    return res,list(zip(list_i,list_t))    

#exp(-x^2) integral
def expointeg(x:ReelNumber,nbtimes=100,nbplus=200):
    number_one=ReelNumber([1],[],'+')
    

    n=ReelNumber([],[],'+')
    res=x.copyReelNumber()
    un=x.copyReelNumber()

    
    t=time.time()
    list_t=[]
    list_i=[]
    cpt=1
    cf=ReelNumber([1],[],'-')
    cf=operation(cf,x,'*')
    cf=operation(cf,x,'*')

    for i in range(nbtimes+1):
        
        
        b1=ReelNumber([2],[],'+')
        c=ReelNumber([3],[],'+')
        b1=operation(b1,n,'*')
        a1=operation(b1,number_one,'+')
        b1=operation(b1,c,'+')

        b2=operation(n,number_one,'+')

        b=operation(b1,b2,'*')
        
        a=operation(cf,a1,'*')
        # print()
        # print()
        # print("a==",a)
        # print("b==",b)

        alpha=operation(a,b,'/',nbplus)
        # print("alpha==",alpha)


        un=operation(un,alpha,'*')
        # print("  un==",un)
        # print(un)
        n=operation(n,number_one,'+')

        if len(un.part_decimal)>nbplus:
            un.part_decimal=un.part_decimal[:nbplus]
        res=operation(res,un,'+')
        if (i) % 50==0:
            t1=time.time()-t
            list_t.append(int(t1))
            list_i.append(cpt)
            cpt+=1
            print(i,"  TIME:",t1)
            print()
            print("    ->>>  len(part whole)=",len(res.part_whole))
            print("    ->>>  len(part dec)=",len(res.part_decimal))
            print("      ->>>   ",res)
            print()
            print()
            t=time.time()
        # print(res)

    if len(res.part_decimal)>nbplus:
        res.part_decimal=res.part_decimal[:nbplus]
    return res

def expintegral2(x):
    res=0
    for i in range(10):
        cf=2*i+1
        a=math.pow(-1,i)*math.pow(x,cf)

        b=cf*math.factorial(i)


        res+=(a/b)
        # print("res2:",res)
    return res    

    