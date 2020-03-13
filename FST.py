# import the fst module
from nltk.draw import *
from nltk.nltk_contrib.fst.fst import *

# FST class with recognize function
class myFST(FST):    
    def recognize(self, iput, oput):

        # insert your codes here
        #self.inp = iput.split()
        #self.outp = oput.split()
        self.inp = list(iput)
        self.outp = list(oput)
        #f.transduce("abc")        
        
        if list(oput) == f.transduce(list(iput)):
            #print(" ".join(f.transduce(iput.split())))        
            return True
        else:
            return False

f = myFST('Assignment')


def convert():
     
    inpt = input("Enter sheep language to be converted to cow language(i.e:baaa!): \n\nSheep language: " )
    
    # use the nltk transduce function    
    print("Cow language: ","".join(f.transduce(inpt)))


def accept_reject():
    
    inp  = input("\nEnter input to be checked: ")
    outp = "".join(f.transduce(inp))
    
    print("Sheep language: ", inp)
    print("Cow language: ", outp)

    # use the recognize function defined in myFST
    # if f.recognize(inp, outp):
    if f.recognize(inp, outp):
        print("\nAccept")
    else:    
        print("\nReject")
             
# add the states in the FST
for i in range(1,5):
    f.add_state(str(i)) # add states '1' .. '4'

# add initial state
f.initial_state = '1' # -> 1

# add all transitions
f.add_arc('1', '2', ('b'), ('m')) # 1 -> 2 [b:m]
f.add_arc('2', '2', ('a'), ('o')) # 2 -> 2 [a:o]
f.add_arc('2', '3', ('a'), ('o')) # 2 -> 3 [a:o]
f.add_arc('3', '4', ('!'), ('!')) # 3 -> 4 [!:!]

# add final/accepting state
f.set_final('4') # 4 ->

convert()
accept_reject()    
    

