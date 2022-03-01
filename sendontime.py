#Alireza-Hajizadeh
#send whatsapp msg instantly in python 
from WhatsAppmsg import sendwhatmsg
from WhatsAppmsg import pg

number = input("Enter your number (+989999999999) : ")
msg = input("Enter your messeage : ")
settimeh = int(input("Enter your Time hour : "))
settimem = int(input("Enter your Time minute  : "))
 
sendwhatmsg(number , msg, settimeh,settimem)
wait_time: int = 1500
pg.press("enter")
