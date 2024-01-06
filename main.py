from basicops import *

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
nb1=ReelNumber([1],[2],'+')
nb2=ReelNumber([6],[0],'-')

nb3=ReelNumber([2],[7,1],'+')
nb4=ReelNumber([8],[0,0,0,0,0,0,0,0,0,0,0,0],'+')

nb5=ReelNumber([2],[7,1],'-')
nb6=ReelNumber([1,0],[0,0,0,0,0,0,0,0,0,0,0,0],'-')

nb7=ReelNumber([1],[0],'-')
nb8=ReelNumber([7],[0,0,0,0,0,0,0,0,0,0,0,0],'+')


PosIntPow(nb1,nb2)
PosIntPow(nb3,nb4)
PosIntPow(nb5,nb6)
x=PosIntPow(nb7,nb8)
