#!/usr/bin/python3
import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("kpeddaboinam@gmail.com", "*******")
server.ehlo()
server.ehlo
msg = "Hello!" 
server.sendmail("kpeddaboinam@gmail.com", "peddaboinakishan@gmail.com", msg)
server.close()
