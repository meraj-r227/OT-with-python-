#how can i  use str for password than  sensetive captal word or another sensetive 
#python string
#1.python - string concatenation
#2.python - slicing string
#3.python -escape characters
#4.python - format - strings

#1.
# name = input("enter your name :")
# lst_name = input("Enter your lst_name:")
# print(name+lst_name)
# print("your name:" +  name  + "your last name :"+  lst_name + "welcom to  my app")


# #1.
# import getpass
# import platform

# user = getpass.getuser()
# info = platform.uname()

# print("your divice name :" +user)
# print("your information divice :" +str(info))
# print(info[0])
# print("your os divice :" +info[0])
# print("your os version divice :" +info[2])

#2.

# print("we want make strong password  please enter your idea:")
# Username =  input("Enter your name :")
# Idea =  input("Enter your Idea :")
# print(" making  strong password :" + Username[0:4]+Idea[2:6])
# #[0:2]form zero  to  two select 
# #[3:] you dont want to print the first three letters / for  ex : hi  meraj  
# # h,i,space  are not  print **space like -  (hi-meraj) and  when  we say  3  letters  it's  mean h,i,-




#3.

#when we  want  new  line  writing  we  can  use  \n
# and  if  you  want  write   escape  \t 

# print("meraj\nroozbahani \t iran ")

#for   writing  in  color  ,  we  use  the  colorama library  
# from colorama import Fore,init
# import time
# init()
# print(Fore.RED+"[1]:"+Fore.GREEN+"Meraj")
# time.sleep(0.2)
# print(Fore.RED+"[2]:"+Fore.GREEN+"Roozbahani")
# time.sleep(0.2)
# print(Fore.RED+"[3]:"+Fore.GREEN+"+9891232748213")
# time.sleep(0.2)

# .........................................................
# import getpass
# import platform
# user = getpass.getuser()
# info = platform.uname()

# print(Fore.RED+"your divice name :"+Fore.GREEN +user)
# time.sleep(0.2)
# print(Fore.RED+"your information divice :"+Fore.GREEN+str(info))
# time.sleep(0.2)
# print(Fore.GREEN+info[0])
# time.sleep(0.2)
# print(Fore.RED+"your os divice :"+Fore.GREEN+info[0])
# time.sleep(0.2)
# print(Fore.RED+"your os version divice :"+Fore.GREEN+info[2])
# time.sleep(0.2)

#4.
# #when  you  want  bold   your  text  
# print("hi  \"python\"")
# print("hi'python'")


#chack  your directory  with  os  library
# what is in that directory/file or anather things 

# import os
# os.chdir("d:")
# print(os.listdir())

# import os
# os.listdir("black  python")
# print(os.listdir())