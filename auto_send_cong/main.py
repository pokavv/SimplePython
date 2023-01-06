import pandas as pd
import datetime as dt
import smtplib as smt
import random

SENDER = 'sender@gmail.com'
PW = 'this is password'

today = dt.datetime.now()
today_tuple = (today.month, today.day)
print(f'오늘은 {today.month}월 {today.day}일입니다.')

data = pd.read_csv('auto_send_cong/birthdays.csv')
birthday = {(row['month'], row['day']):row for (index, row) in data.iterrows()}

if today_tuple in birthday:
    letter_path = f'auto_send_cong/letter_templates/letter_{random.randint(1, 3)}.txt'

    with open(letter_path) as letter:
        birthday_person = birthday[today_tuple]
        content = letter.read()
        content = content.replace('[NAME]', birthday_person['name'])
        name = birthday_person['name']
    
    print(f'오늘은 {name} 님의 생일입니다. 축하 메일을 보냅니다!')

    with smt.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(SENDER, PW)
        connection.sendmail(from_addr=SENDER, 
                            to_addrs=birthday_person['email'], 
                            msg=f'Subject:Happy Birthday!!\n\n{connection}'
                            )