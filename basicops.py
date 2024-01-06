nbplus=10
class ReelNumber:
    def __init__(self,ph,pc,si):
        self.part_whole=ph
        self.part_decimal=pc
        self.signe=si
        self.removeUnutilZeroes()
        #example nb='+'[1,2,3][1,8,4]
    def changeSigneToPositif(self):
        if self.signe=='-':
            self.signe='+'    
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
def comparePosNumbers(nb1 : ReelNumber,nb2: ReelNumber):
    nb1.removeUnutilZeroes()
    nb2.removeUnutilZeroes()
    if len(nb1.part_whole)>len(nb2.part_whole):
        return 1
    elif len(nb1.part_whole)<len(nb2.part_whole):
        return -1
    else:
        for i in range(len(nb1.part_whole)):
            if nb1.part_whole[i]>nb2.part_whole[i]:
                return 1
            elif nb1.part_whole[i]<nb2.part_whole[i]:
                return -1
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
                return 1
            elif l1[i]<l2[i]:
                return -1
    return 0        

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
    return wh,dc,nb11.signe

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
    return wh,dc,nb11 

def PosMult(nb1:ReelNumber, nb2:ReelNumber):
    l1=nb1.part_whole.copy()
    l1.extend(nb1.part_decimal.copy())
    l2=nb2.part_whole.copy()
    l2.extend(nb2.part_decimal.copy())
    list_mult=[]
    nbt=len(l1)+1+len(l2)-1
    i=-1

    #do mult
    nn=0
    while(i>=-len(l1)):
        ll=[]
        j=-1
        sp=0
        while(j>=-len(l2)):
            r=l1[i]*l2[j]+sp
            if r>=10:
                sp=r//10
                r=r%10
            else:
                sp=0
            ll.insert(0,r)
            j-=1

        if sp>=1:
            ll.insert(0,sp)
        for k in range(nn):
            ll.append(0)
        ndiff=nbt-len(ll)

        for k in range(ndiff):
            ll.insert(0,0)
        list_mult.append(ll)                    
        i-=1
        nn+=1
    #sum results
    n=len(list_mult[0])
    i=-1
    sp=0
    flist=[]
    while(i>=-n):
        r=sp
        for l in list_mult:
            r+=l[i]
        if r>=10:
            sp=r//10
            r=r%10
        else:
            sp=0
        flist.insert(0,r)    
        i-=1     
    nsplit=len(nb1.part_whole)+len(nb2.part_whole)
    wh=flist[0:nsplit]
    dc=flist[nsplit:]
    return wh,dc 
def DivInt(nb1:ReelNumber,nb2:ReelNumber):
    #cmp=comparePosNumbers(nb1,nb2)
    #print("cmp==",cmp)
    number_one=ReelNumber([1],[],'+')
    number_zero=ReelNumber([],[],'+')
    number=ReelNumber([1],[],'+')
    for i in range(10):
        number2=operation(nb2,number,'*')
        cmp=comparePosNumbers(nb1,number2)
        #print(nb1,number2," cmp:",cmp)
        if cmp==-1:
            #div
            number=operation(number,number_one,'-')
            #print(nb1," // ",nb2,"  ==",number)
            #mod
            mult=operation(nb2,number,'*')
            mult.changeSigneToPositif()
            rest=operation(nb1,mult,'-')
            #print(nb1," % ",nb2,"  ==",rest)
            return number,rest
        number=operation(number,number_one,'+')
def MoveComma(nbvrg,resd):
    #print(nbvrg)
    if ',' not in resd:
        resd.append(',')
    
    vpos=resd.index(',')

    if nbvrg>0:
        p=vpos+nbvrg
        #print("  p===",p)
        if p>len(resd)-1:
            ndiff=p-(len(resd)-1)
            for k in range(ndiff):
                resd.append(0)
            vpos=resd.index(',')        
            p=vpos+nbvrg
        resd.pop(vpos)    
        resd.insert(p,',')        
    elif nbvrg<0:
        p=vpos-abs(nbvrg)
        if p<0:
            for k in range(abs(p)):
                resd.insert(0,0)                    
            vpos=resd.index(',')        
            p=vpos-abs(nbvrg)
        resd.pop(vpos)      
        resd.insert(p,',')

    vpos=resd.index(',')    
    wh=resd[:vpos]
    dc=resd[vpos+1:]
    #print()
    #print(wh,dc)
    return wh,dc
def PosDiv(nb1:ReelNumber,nb2:ReelNumber,nbplus):
    l1=nb1.part_whole.copy()
    l1.extend(nb1.part_decimal.copy())
    l2=nb2.part_whole.copy()
    l2.extend(nb2.part_decimal.copy())
    number_zero=ReelNumber([],[],'+')

    # print()
    # print()
    # print("nb1,nb2:",nb1,nb2)
    # print("l1,l2:",l1,l2)
    # print()

    resd=[]

    if len(l1)<len(l2):
        npd=len(l1)
    else:
        npd=len(l2)    
    l11=[]
    for k in range(npd):
        l11.append(l1.pop(0))
    # print("  l1,l11,l2:",l1,l11,l2)
    cpt=1
    while(True):
        # print()
        # print("cpt:")
        nb11=ReelNumber(l11.copy(),[],'+')
        nb22=ReelNumber(l2.copy(),[],'+')
        cmp=comparePosNumbers(nb11,nb22)
        #loop until can devide
        # print("  l1,l11,l2:",l1,l11,l2)
        # print("  resd:",resd)
        
        while cmp<0:
            # print("  loop:")
            if len(l1)>0:
                if cpt==1:
                    l11.append(l1.pop(0))
                else:
                    l11.append(l1.pop(0))  
                    resd.append(0)  
            else:
                l11.append(0)

                if "," not in resd:
                    resd.append(0)
                    resd.append(",")
                else:
                    resd.append(0)
            nb11=ReelNumber(l11.copy(),[],'+')
            nb22=ReelNumber(l2.copy(),[],'+')
            cmp=comparePosNumbers(nb11,nb22)
            # print("     l1,l11,l2:",l1,l11,l2)
            # print("     resd:",resd)        
            # print("     cmp",cmp)
            if comparePosNumbers(nb11,number_zero)==0 and len(l1)==0 and ',' in resd:
                nbvrg=-len(nb1.part_decimal)+len(nb2.part_decimal)
                return MoveComma(nbvrg,resd)
                # print()
                # print(nb1," / ",nb2," = ",resd)
                # return 
            
        # print()
        # print()
        # print("  l1,l11,l2:",l1,l11,l2)
        # print("  resd:",resd)
        nb11=ReelNumber(l11.copy(),[],'+')
        nb22=ReelNumber(l2.copy(),[],'+')
        d,r=DivInt(nb11,nb22)
        d.removeUnutilZeroes()
        r.removeUnutilZeroes()
        resd.extend(d.part_whole)
        if comparePosNumbers(r,number_zero)==0 and len(l1)==0:
            break
        l11=[]

        if len(l1)>0: 
            if len(r.part_whole)>0:
                l11.extend(r.part_whole)
                l11.append(l1.pop(0))
            
            else:
                l11.append(0)
                l11.append(l1.pop(0))    
        else:
            if ',' not in resd:
                resd.append(',')    
            l11.extend(r.part_whole)
            l11.append(0)

        # print("  rest:",r.part_whole,"div:",d.part_whole)
        # print("  l1,l11,l2:",l1,l11,l2)
        # print("  resd:",resd)
            
        
        cpt+=1     
        if ',' in resd:
            k=resd.index(',')
            if len(resd[k+1:])>=nbplus:
                break
        if cpt>=nbplus:
            break    
    nbvrg=-len(nb1.part_decimal)+len(nb2.part_decimal)
    return MoveComma(nbvrg,resd)
    # print()    
    # print(nb1," / ",nb2," = ",resd)
def PosDiv2(nb1:ReelNumber,nb2:ReelNumber,nbplus):
    l1=nb1.part_whole.copy()
    l1.extend(nb1.part_decimal.copy())
    l2=nb2.part_whole.copy()
    l2.extend(nb2.part_decimal.copy())
    number_zero=ReelNumber([],[],'+')

    # print()
    # print()
    # print("nb1,nb2:",nb1,nb2)
    # print("l1,l2:",l1,l2)
    # print()

    npd=len(l2)
    resd=[]
 

    while(True):
        print()
        print("cpt:")
        l11=[]
        if npd>len(l1):
            ndiff=npd-len(l1)
            for k in range(ndiff):
                l1.append(0)
            if "," not in resd:
                resd.append(0)
                resd.append(",")
                ndiff-=1
            for k in range(ndiff):
                resd.append(0)

        print("  l1,l11,l2:",l1,l11,l2)
        print("  resd:",resd)
        for k in  range(npd):
            l11.append(l1.pop(0))
        print("  l1,l11,l2:",l1,l11,l2)
        print("  l11:",l11)
        print("  resd:",resd)

        nb11=ReelNumber(l11.copy(),[],'+')
        nb22=ReelNumber(l2.copy(),[],'+')
        cmp=comparePosNumbers(nb11,nb22)
        if cmp<0:
            if len(l1)>0:
                l11.append(l1.pop(0))
            else:    
                l11.append(0)
                if "," not in resd:
                    resd.append(0)
                    resd.append(",")
                else:
                    resd.append(0)
        print("  l1,l11,l2:",l1,l11,l2)
        print("  l11:",l11)
        print("  resd:",resd)
        nb11=ReelNumber(l11.copy(),[],'+')
        nb22=ReelNumber(l2.copy(),[],'+')
        d,r=DivInt(nb11,nb22)
        d.removeUnutilZeroes()
        r.removeUnutilZeroes()
        
        if len(d.part_whole)>0:
            resd.extend(d.part_whole)
        else:
            resd.append(0)    
        print("  rest:",r.part_whole,"div:",d.part_whole)
        print("  l1,l11,l2:",l1,l11,l2)
        print("  resd:",resd)
        
        if comparePosNumbers(r,number_zero)==0 and len(l1)==0:
            break
        
        if len(l1)>0: 
            if len(r.part_whole)>0:
                l1=r.part_whole+l1
            else:
                l1.insert(0,0)    
        else:
            if ',' not in resd:
                resd.append(',')    
            l1=r.part_whole
            l1.append(0)

        print("  l1,l11,l2:",l1,l11,l2)
        if ',' in resd:
            k=resd.index(',')
            if len(resd[k+1:])>=nbplus:
                break

      



def operation(nb1:ReelNumber,nb2:ReelNumber,oper):
    
    if oper=='+':
        if nb1.signe==nb2.signe :
            wh,dc,si=PosPlus(nb1,nb2)
        else:
            wh,dc,nbsi=PosMinus(nb1,nb2)
            si=nbsi.signe
        return ReelNumber(wh,dc,si)     
    if oper=='-':
        if nb1.signe!=nb2.signe :
            #+5-(-6)=5+6=11
            #-5-(+6)=-5-6=-11                
            wh,dc,_=PosPlus(nb1,nb2)
            si=nb1.signe
        else:
            #+5-(+6)=5-6=-1
            #-5-(-6)=-5+6=1              
            wh,dc,nbsi1=PosMinus(nb1,nb2)
            if comparePosNumbers(nbsi1,nb1)==0:
                si=nbsi1.signe
            elif comparePosNumbers(nbsi1,nb2)==0:
                if nb2.signe=='+':
                    si='-'
                else:
                    si='+'
        return ReelNumber(wh,dc,si)        
    if oper=='*':
        wh,dc=PosMult(nb1,nb2)
        if nb1.signe==nb2.signe :
            si='+'
        else:
            si='-'
        return ReelNumber(wh,dc,si)
    if oper=='/':
        global nbplus
        wh,dc=PosDiv(nb1,nb2,nbplus)
        if nb1.signe==nb2.signe :
            si='+'
        else:
            si='-'
        # print()
        # print(nb1," / ",nb2," = ",ReelNumber(wh,dc,si))    
        # print()
        return ReelNumber(wh,dc,si)
    
    return None    






nb1=ReelNumber([9],[5,3,5,3],'-')
nb2=ReelNumber([0],[7,9],'-')
nb3=ReelNumber([1],[0],'+')
nb4=ReelNumber([2],[3,0,0,0,0,0,0,0,0,0,0,0],'+')
nb5=ReelNumber([1],[0,5,7],'+')
nb6=ReelNumber([1,2],[3,0,0,0,0,0,5,0,0,0,0,0],'+')


nbplus=15

operation(nb1,nb2,"/")
operation(nb3,nb4,"/")
operation(nb5,nb6,"/")

nb1=ReelNumber([3,9,4,9,6,1,1,0,3],[0],'-')
nb2=ReelNumber([2,4,0],[0,5,6],'-')
nb3=ReelNumber([9],[0,4,2],'+')
nb4=ReelNumber([8],[5,1,7],'+')
nb5=ReelNumber([1,5,0],[8,4,2],'+')
nb6=ReelNumber([0],[1,0,0,0,0,0,0,0,0,0,0,0],'+')


operation(nb1,nb2,"/")
operation(nb3,nb4,"/")
operation(nb5,nb6,"/")

operation(nb2,nb1,"/")
operation(nb4,nb3,"/")
operation(nb6,nb5,"/")


operation(nb2,nb3,"/")
operation(nb1,nb3,"/")
operation(nb1,nb5,"/")


operation(nb2,nb4,"/")
operation(nb4,nb6,"/")
operation(nb3,nb5,"/")