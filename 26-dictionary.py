# dict 
# for  ex  i  have  a list   phone  number  
#and  i wnat  send  SMS    and  say  happy persion new year  
#but among  the  number  ,  there  are  also  french  numbers  
#As  result  ,  we  can fix  this  issus  with  the  help of  dictionaries  


# the  first  method(With out  dictionaries) 
# this  method  for  a  few  user  is  ok  but  when  we  have  a  lot  of  user  the  secend  method  is  good  
from  colorama import Fore,Style,init
import time  
init ()
mylist = ["ALI","FARHAD","JACK","LOCI"]
if  mylist[0] ==  "ALI" and  mylist[1] == "FARHAD" :  
    time.sleep(0.5) 
    print(Fore.GREEN+"Happy  new year")  
    
    
# The  secend  method (with dict) 
# dictionaries  has  two  items   first is  key  &  secend  is  value  
mydict = {"Key":"Value"}
print(Fore.BLUE+str(mydict))
print(type(mydict))
# when we  use  list  and  say  s.th[0] ==>>  print(s.th[0])  
# but  in  dict we  say  s.th["KEY"] ===>>  print for  me  value     
mydictionarie = {"CODA":"UODA"}
print(Fore.YELLOW+str(mydictionarie["CODA"]))
# New  ex  of  dict 
newdict =  {"1st groupe":["Ali","Amir","Ahmad"],"2nd groupe":("mona",)}
print(Fore.WHITE+str(newdict["1st groupe"]))
print(Fore.WHITE+str(newdict["2nd groupe"]))

# pro ex  
time.sleep(0.5)
info_name = input(Fore.RED+"[+]"+Fore.GREEN+"Enter your name :\n")
time.sleep(0.5)
info_phone= input (Fore.RED+"[+]"+Fore.GREEN+"Enter your mobail  phone :\n")
time.sleep(0.5)
info_job = input(Fore.RED+"[+]"+Fore.GREEN+"what  is  your  job  :\n")
time.sleep(0.5)
info_age = input(Fore.RED+"[+]"+Fore.GREEN+"How  old  are  you  :\n")
ex_dict =  {"1st DATA":"info_name","2nd DATA":"info_phone","3th DATA":"info_job","4th DATA":"info_age"}
if ex_dict ["1st DATA"] or ex_dict["2nd DATA"] or ex_dict["3th DATA"] or ex_dict["4th DATA"]:
    print(Fore.MAGENTA+"Hi")
if ex_dict["3th DATA"] == "Programmer" or "I don't have  job ": 
    print(Fore.MAGENTA+" we  can be good  frinds  to each other ")
    
    
# Acces items with in the dict (key, value,get,.....)   
# we  have  a  lot  of  method  for  print dict 
minidict = {"Uoda":994453}
print(minidict["Uoda"]) 
print(minidict.get("Uoda"))
# show  keys =====>>>>>>
print(minidict.keys())
# show value  ======>>>>
print(minidict.values)    
    
    


