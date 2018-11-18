#!/usr/bin/python3
import smtplib
server = smtplib.SMTP('smtp.gmail.com', 578)
server.login("kpeddaboina@gmail.com", "Oxalic_336")
msg = "Hello!" 
server.sendmail("kishanpeddaboina@gmail.com", "peddaboinakishan@gmail.com", msg)
