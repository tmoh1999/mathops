class ReelNumber:
    def __init__(self,ph,pc,si):
        self.part_whole=ph
        self.part_decimal=pc
        self.signe=si
        #example nb='+'[1,2,3][1,8,4]
class complexNumber:
    def __init__(self,re,im):
        self.part_reel=re
        self.part_im=im
        #example complexnb='+'[1,2,3][1,8,4],,'-'[1,2,3][1,8,4]