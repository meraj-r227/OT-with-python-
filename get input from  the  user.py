# how  to  make  password  list   ==> for  ex  generate a  password list using the  obtiained  username and  phon number.
from colorama import Fore

import os
os.system("cls")
import time
phone =  int(input(Fore.GREEN+"[+]"+Fore.WHITE+"enter  your  phone  number :"))
print(Fore.GREEN+"your phone  number :" )
time.sleep(0.2)
print(Fore.WHITE+str(phone))
time.sleep(0.2)
print(Fore.RED+"verification  code sent ")
time.sleep(0.2)