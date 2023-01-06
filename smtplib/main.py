import smtplib as smt
import datetime as dt
import random

SENDER = 'sender@gmail.com'
PW = 'this is password'
RECIPIENT = 'recipient@yahoo.com'

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 4:
    with open('smtplib/quotes.txt') as quote:
        all_quotes = quote.readlines()
        quote = random.choice(all_quotes)
    print(quote)
    
    with smt.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(SENDER, PW)
        connection.sendmail(from_addr=SENDER, 
                            to_addrs=RECIPIENT, 
                            msg=f'Subject:Daily Motivation\n\n{quote}'
                            )