import smtplib as smt
import random

SENDER = 'sender@gmail.com'
PW = 'this is password'
RECIPIENT = 'recipient@yahoo.com'

with smt.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(SENDER, PW)
        connection.sendmail(from_addr=SENDER, 
                            to_addrs=RECIPIENT, 
                            msg=f'Subject:Daily Motivation\n\nBody'
                            )