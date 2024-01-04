class ReelNumber:
    def __init__(self,ph,pc,si):
        self.part_whole=ph
        self.part_decimal=pc
        self.signe=si
        self.removeUnutilZeroes()
        #example nb='+'[1,2,3][1,8,4]
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

        if self.signe=='-':
            return self.signe+stwh+","+stdc
        else:
            return stwh+","+stdc
                   

class complexNumber:
    def __init__(self,re,im):
        self.part_reel=re
        self.part_im=im
        #example complexnb='+'[1,2,3][1,8,4],,'-'[1,2,3][1,8,4]

nb1=ReelNumber([0,0,0,5,5,5,0,0],[0,0,0,5,5,1,2,3,0,0,0,0],'-')
nb2=ReelNumber([0,2,0,6,8,9,0,0],[0,0,0,1,4,1,2,3,0,3,0,0],'+')
nb3=ReelNumber([0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0],'+')
print(nb1)
print(nb2)
print(nb3)
print([1,2,3][-3])
#[1,2,3][1,8,4]+
#[0,0,0][5,0,0]        
        