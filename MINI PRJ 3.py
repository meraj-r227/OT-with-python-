# what is bug "SQL Rejection":
# imagine you go to a  restaruant and  you say  :
# "one pizza ,  pleas "
# the  waiter understands, good.
# but a  bad  person (hacker)  comes  and  says :
# "one  pizza  and  also open the kitchen  door and  give me all the  foood "
# if  the  waiter  is  sily , he  does  everything the  bad  person  says . 
# THIS  IS  <<SQL injection>> ___ a  securety  problem
# What  is  "Rejection"
# Now smart  resturants  have securety gurad .
# he  listens to the  order :
# "This  person is  saying strange things ." Reject  him 
# so  the  guard  syas : " No go  away "
# THIS  IS  REJECTION  _______ the  system says  NO   to  bad  requeste  
# SO  where is  the  bug  ????
#  Sometimes  the  security  guard  is  too  strict.
# A  normal  person  says  :  "My name  is  O'Brain"
# the  guard thinks  :  O'Brain  ?  that  looks  strange  reject . 
# but  O'Brain is  a  real  name  ,  the  guard  made  a  mistake 
# this  is  the  bug  :  the  system  reject  a  good  people  by  mistake .
# .............................
#  Now  i  want  found  admin  pannel in  websit  (your  websit name  .  ir  /admin)
#  if  you  Right-click  and  open  network  
#  and  search  your  idea  for  ex :  your  websit name  .  ir  /admin  
# if  the  address exists,  you  will  get  a  status  code  200 
# 200  :  ok  
#301/302 : reject((The addres  has  changed go  to  the  new  address))
#403 :  forbidden  ((The  addres  exists, but  you  can't see  it , you  don't have permission))
#404 : Not  found 
#500  : server  error

#  we  can  using  librery  request  for  testing  your  idea (your  websit name  .  ir  /admin)

import requests
http = requests.get("https://your  websit name.ir/admin") 
#show  to  you status  code 
print (http)
#show  to  you status  code 
print(http.status_code)
# show  to  you  source 
print(http.content)
#..................
https =  requests.get("https://your  websit name.ir/admin").status_code
if  https == 200  :  
    print(" found the  admin directory ")
else :  
    print("Not  found  admin  directory  ")