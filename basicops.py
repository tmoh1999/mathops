class ReelNumber:
    def __init__(self,ph,pc,si):
        self.part_whole=ph
        self.part_decimal=pc
        self.signe=si
        self.removeUnutilZeroes()
        #example nb='+'[1,2,3][1,8,4]
    def copyReelNumber(self):
        wh=self.part_whole.copy()
        dc=self.part_decimal.copy()
        si=self.signe
        nb=ReelNumber(wh,dc,si)
        return nb
    def removeUnutilZeroes(self):
        #remove zeroes from start at part_whole:[0005]
        while(len(self.part_whole)>0 and self.part_whole[0]==0):
            self.part_whole.pop(0)
        #remove zeroes from end at part_decimal:[5000]
        while(len(self.part_decimal)>0 and self.part_decimal[-1]==0):
            self.part_decimal.pop(-1)
    
    def __str__(self):
        stwh="".join(map(str,self.part_whole))
        stdc="".join(map(str,self.part_decimal))
        if stwh=="":
            stwh='0'
        if stdc=="":
            stdc='0'

        return self.signe+stwh+","+stdc

class complexNumber:
    def __init__(self,re,im):
        self.part_reel=re
        self.part_im=im
        #example complexnb='+'[1,2,3][1,8,4],,'-'[1,2,3][1,8,4]

def compareWithoutSign(nb1 : ReelNumber,nb2: ReelNumber):
    nb1.removeUnutilZeroes()
    nb2.removeUnutilZeroes()
    if len(nb1.part_whole)>len(nb2.part_whole):
        return nb1,nb2
    elif len(nb1.part_whole)<len(nb2.part_whole):
        return nb2,nb1
    else:
        for i in range(len(nb1.part_whole)):
            if nb1.part_whole[i]>nb2.part_whole[i]:
                return nb1,nb2
            elif nb1.part_whole[i]<nb2.part_whole[i]:
                return nb2,nb1
        #make decimal parts lengths equals
        l1=nb1.part_decimal.copy()
        l2=nb2.part_decimal.copy()
        if len(l1)>len(l2):
            ndiff=len(l1)-len(l2)
            for i in range(ndiff):
                l2.append(0)

        if len(l1)<len(l2):
            ndiff=len(l2)-len(l1)
            for i in range(ndiff):
                l1.append(0)

        for i in range(len(l1)):
            if l1[i]>l2[i]:
                return nb1,nb2
            elif l1[i]<l2[i]:
                return nb2,nb1
    return nb1,nb2        
def equalLengths(nb11:ReelNumber, nb22:ReelNumber):
    nb1=nb11.copyReelNumber()
    nb2=nb22.copyReelNumber()
    #whole_part
    if len(nb1.part_whole)>len(nb2.part_whole):
        ndiff=len(nb1.part_whole)-len(nb2.part_whole)            
        for i in range(ndiff):
            nb2.part_whole.insert(0,0)
    elif len(nb1.part_whole)<len(nb2.part_whole):
        ndiff=len(nb2.part_whole)-len(nb1.part_whole)            
        for i in range(ndiff):
            nb1.part_whole.insert(0,0)

    #decimal_part
    if len(nb1.part_decimal)>len(nb2.part_decimal):
        ndiff=len(nb1.part_decimal)-len(nb2.part_decimal)            
        for i in range(ndiff):
            nb2.part_decimal.append(0)
    elif len(nb1.part_decimal)<len(nb2.part_decimal):
        ndiff=len(nb2.part_decimal)-len(nb1.part_decimal)            
        for i in range(ndiff):
            nb1.part_decimal.append(0)
    return nb1,nb2        
def PosPlus(nb1:ReelNumber, nb2:ReelNumber):
    nb11,nb22=compareWithoutSign(nb1,nb2)
    nb11,nb22=equalLengths(nb11,nb22)
    sp=0
    #nb11 dec part - nb22 dec part
    dc=[]
    i=-1
    while(i>=-len(nb11.part_decimal)):
        r=nb11.part_decimal[i]+(nb22.part_decimal[i]+sp)
        if r>=10:
            sp=r//10
            r=r%10
        else:
            sp=0
        dc.insert(0,r)
        i-=1

    #nb11 whole part - nb22 whole part
    wh=[]    
    i=-1
    while(i>=-len(nb11.part_whole)):
        r=nb11.part_whole[i]+(nb22.part_whole[i]+sp)
        if r>=10:
            sp=r//10
            r=r%10
        else:
            sp=0
        wh.insert(0,r)
        i-=1
    if sp>=1:
       wh.insert(0,sp)            
    return wh,dc   

def PosMinus(nb1:ReelNumber, nb2:ReelNumber):
    nb11,nb22=compareWithoutSign(nb1,nb2)
    nb11,nb22=equalLengths(nb11,nb22)
    sp=0
    si='+'
    #nb11 dec part - nb22 dec part
    dc=[]
    i=-1
    while(i>=-len(nb11.part_decimal)):
        r=nb11.part_decimal[i]-(nb22.part_decimal[i]+sp)
        if r<0:
            sp=1
            r+=10
        else:
            sp=0
        dc.insert(0,r)
        i-=1

    #nb11 whole part - nb22 whole part
    wh=[]    
    i=-1
    while(i>=-len(nb11.part_whole)):
        r=nb11.part_whole[i]-(nb22.part_whole[i]+sp)
        if r<0:
            sp=1
            r+=10
        else:
            sp=0
        wh.insert(0,r)
        i-=1 
    return wh,dc   






nb1=ReelNumber([0,5,8,0,0],[9],'-')
nb2=ReelNumber([9,1,5,5],[8,0,0,1,4,1,2,3,0,3,0,0],'+')
nb3=ReelNumber([0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],'+')

print(nb1)
print(nb2)

print()
nbx=PosMinus(nb1,nb2)
nbx2=PosPlus(nb1,nb2)
print(nbx)
print(nbx2)
#          -1 0     
#[1,0,3][1,0,4]+
#[1,5,0][5,0,0]
#sp=0
#0-(4+sp==0)=>-4:6 sp=1
#0-(0+sp==1)=>-1:9 sp=1            
#5-(1+sp)=>3  sp=0
#0-(3+sp)=>-3:7 sp=1
#5-(0+sp)=>4 sp=0
#1-(1+sp)=>0 sp=0

#047,396        
#sp=0
#[1,5,8,9][8,6,2,4,0]
#[9,5,8,9][7,4,7,8,7]
#0+7+sp=> 7<10 => sp=0
#4+8+sp=> 12>=10 => sp=12//10=1
#2+7+sp=> 10>=10 => sp=10//10=1
#.....
#1+9+1=11
#sp=1