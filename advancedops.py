from basicops import *

def facto(n:ReelNumber):
    number_zero=ReelNumber([],[],'+')
    number_one=ReelNumber([1],[],'+')
    number=ReelNumber(n.part_decimal.copy(),[],'+')
    cmp=comparePosNumbers(number_zero,number)
    print()
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
    