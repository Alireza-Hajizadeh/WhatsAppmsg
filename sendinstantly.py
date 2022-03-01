#Alireza-Hajizadeh
#send whatsapp msg instantly in python 
from WhatsAppmsg import sendwhatmsg_instantly
from WhatsAppmsg import pg

number = input("Enter your number (+989999999999) : ")
msg = input("Enter your messeage : ")
timeleft = input("Enter your Time left : ")

sendwhatmsg_instantly(number , msg, timeleft)
wait_time: int = 1500
pg.press("enter")