#how can i  use str for password than  sensetive captal word or another sensetive 
#python string
#1.python - string concatenation
#2.python - slicing string
#3.python -escape characters
#4.python - format - strings

#1.
name = input("enter your name :")
lst_name = input("Enter your lst_name:")
print(name+lst_name)
print("your name:" +  name  + "your last name :"+  lst_name + "welcom to  my app")


# #1.
import getpass
import platform

user = getpass.getuser()
info = platform.uname()

print("your divice name :" +user)
print("your information divice :" +str(info))
print(info[0])
print("your os divice :" +info[0])
print("your os version divice :" +info[2])

#2.

print("we want make strong password  please enter your idea:")
Uusername =  input("Enter your name :")
Idea =  input("Enter your Idea :")
print(" making  strong password :" + Uusername[0:4]+Idea[2:6])
# #[0:2]form zero  to  two select 
# #[3:] you dont want to print the first three letters / for  ex : hi  meraj  
# # h,i,space  are not  print **space like -  (hi-meraj) and  when  we say  3  letters  it's  mean h,i,-




#3.

#when we  want  new  line  writing  we  can  use  \n
# and  if  you  want  write   escape  \t 

print("meraj\nroozbahani \t iran ")

#for   writing  in  color  ,  we  use  the  colorama library  
from colorama import Fore,init
import time
init()
print(Fore.RED+"[1]:"+Fore.GREEN+"Meraj")
time.sleep(0.2)
print(Fore.RED+"[2]:"+Fore.GREEN+"Roozbahani")
time.sleep(0.2)
print(Fore.RED+"[3]:"+Fore.GREEN+"+9891232748213")
time.sleep(0.2)

# .........................................................
import getpass
import platform
usser = getpass.getuser()
infso = platform.uname()

print(Fore.RED+"your divice name :"+Fore.GREEN +usser)
time.sleep(0.2)
print(Fore.RED+"your information divice :"+Fore.GREEN+str(infso))
time.sleep(0.2)
print(Fore.GREEN+infso[0])
time.sleep(0.2)
print(Fore.RED+"your os divice :"+Fore.GREEN+infso[0])
time.sleep(0.2)
print(Fore.RED+"your os version divice :"+Fore.GREEN+infso[2])
time.sleep(0.2)

#4.
# #when  you  want  bold   your  text  
print("hi  \"python\"")
print("hi'python'")


#chack  your directory  with  os  library
# what is in that directory/file or anather things 

import os
os.chdir("d:")
print(os.listdir())

import os
os.listdir("OT")
print(os.listdir())



#..........................................

# IF  YOU have long  text  you can  use  """ """(3 doubel citation or 6 citation ) 

print(""" hi 
      my name is 
      meraj 
      roozbahnai""")
#...................................
# string  formating = F string 

import getpass
import platform
USER=getpass.getuser()
INFO=platform.uname()
# msg="your usernam :"+USER+  "your os name:"+INFO[0]  + "your os version :" + INFO[2]
# print(msg)
pm = """your os name : {SSD}
your os verstion : {HHD}
your username :{Username}""".format(SSD=INFO[0],HHD=INFO[2],Username=USER)
print(pm)

# and  we  can  use  f  string  like  this  ((pm=f"""your os  verstion: {INFO[2]}"""))


#STRING METHOD

#1. when  we  want to   get  a  user's username whitout using  capital letters  ==> . lower()

kname =  ("MERAJ").lower()
print(kname)   


hname=input("enter  your  name  : ").lower()
print(hname)

#2.when  we  want to   get  a  user's username with  using  capital letters  ==> . upper()

Susernam=input("Enter your name :").upper()
print(Susernam)

#3.when want  to  replace  one letter  with  another 
TTg="hi my  name ,;'is  coda  ".replace("name","namm").replace(",","").replace(";","").replace("'","")
TTg=TTg.replace("c","U")
print(TTg)

#4. when we  want  to  split a  string  into  a  list  
EAS="MY  NAME  IS  CODA ".split()
print(EAS)