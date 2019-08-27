#!/usr/bin/python3

import smtplib
import ssl
import check_availability
import config

with open(check_availability.current_path, 'r') as file:
  current = file.read()

#print('Read current:\n'+current)

with open(check_availability.last_path, 'r') as file:
  last = file.read()

#print('Read last:\n'+last)

if current==last:
  quit()

smtp_server = 'smtp.gmail.com'
port = 465
sender_email = config.sender_email #gmail sender address
password = config.password #gmail sender password
receiver_email = config.receiver_email #receiver email
message = 'Subject: Hamilton Pool availability at '+check_availability.current_time+'\n\n'+'Current state:\n'+current+'\nLast state:\n'+last

server = smtplib.SMTP_SSL(smtp_server, port)
server.login(sender_email, password)
server.sendmail(sender_email, receiver_email, message)
server.quit()

print('Email sent!\n')
