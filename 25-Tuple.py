#Tuples  like  list  
# but Tuple items are ordered , unchangeable, and allow duplicate values
from  colorama  import  Fore,Style, init
import time
init()
myTuple =  ("Coda","Uoda")
print(Fore.BLUE+str(myTuple))
print(Fore.GREEN+str(type(myTuple)))
myList  = ["Coda","Uoda"]
print(Fore.GREEN+str(type(myList)))
Tuple_ex1 = ("F&G",)
print(Fore.BLUE+str(Tuple_ex1[0]))
print(Fore.GREEN+str(type(Tuple_ex1)))
if "F&G" in Tuple_ex1:
    print(Fore.WHITE+str("True"))
#This  isn't Tuple  :>>>>>
NotTuple =  ("F&G") 
print(Fore.GREEN+str(type(NotTuple)))
#Tuple processing volume is  more  optimal  than a  list  and  takes  Up  less  memory 

#WE  can change  tuple  to  list  and  use  append ,  ........
Tupleica =  ("Metalica","Radiohead")
listica = list(Tupleica) 
listica.append("No clear  mind ")
print(Fore.MAGENTA+str(listica))