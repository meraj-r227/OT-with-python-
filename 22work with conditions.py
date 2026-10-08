#if/ condtion  
import getpass
import  platform
from colorama import Fore,init
import time
init()
User = getpass.getuser()
time.sleep(0.5)
print(Fore.GREEN+"User:"+Fore.RED+User)
Info = platform.uname()
time.sleep(0.5)
print(Info[0])
time.sleep(0.5)
print(Info[1])
time.sleep(0.5)
print(Info[2])
if Info[0] == "Windows":
    time.sleep(0.5)
    print(Fore.GREEN+"your device is  true ")
    time.sleep(0.5)
if Info[0] == "Mac":
    time.sleep(0.5)
    print(Fore.GREEN+"your device is  False ")
    time.sleep(0.5)
    
else:
    print("impossible")
    

#level 2  

W = float(input("Enter your weight:"))
H = float(input("Enter your height:"))   
if W < 50:
    if H > 180:
        time.sleep(0.5)
        print(Fore.YELLOW+"Your are Under weight ")
        # elif: if the  previous condtition is not true , check this new condition 
        #else : if  the  previous  condition  is  not  true ,  do this instead
        
elif W >= 50: 
    if H <= 180:
        time.sleep(0.5)
        print(Fore.YELLOW+"Your are Over weight ")
    
    else:
        time.sleep(0.5)
        print(Fore.YELLOW+"your weight is  normal ")    
        
        
        
#level 3 
name =  input ("Enter your name :")
Username = input("Enter your name :")
Password = input("Enter your Password :")       
if Username == "coda"  and Password == "uoda" :
    time.sleep(0.5)
    print(Fore.BLUE+f"welcom {name}")
else :
    print("Not true")
        
        
#level  4
# we  have  opreator  (in)
# see  that sth on the sth  
# for  ex 
Location = str(input("What's your 20 :"))
if "Tehran" in  Location :
    print("Hello")
# if you  write "Tehranjjjjjjjjjjj" again  say  hello  because we see  a Tehran  in  this context
        
Information = str(input("What's the 411 :")) #what's the update 
if "No news yet " not in  Information :
    print("ok")
            