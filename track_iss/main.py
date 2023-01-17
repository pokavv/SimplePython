import requests
import smtplib
import time
from datetime import datetime

MY_LAT = 36.609554
MY_LONG = 127.515285
MY_EMAIL = 'thisisid@gmail.com'
MY_PASSWORD = 'thisispassword'

def isOverhead():
    response = requests.get(url='http://api.open-notify.org/iss-noew.json')
    response.raise_for_status()
    data = response.json()

    iss_lat = float(data['iss_position']['latitude'])
    iss_long = float(data['iss_position']['longitude'])

    if MY_LAT - 5 <= iss_lat <= MY_LAT + 5 and MY_LONG - 5 <= iss_long <= MY_LONG + 5:
        return True

def isNight():
    parameters = {
        'lat': MY_LAT,
        'lng': MY_LONG,
        'formatted': 0,
    }

    response = requests.get(url='http://api.open-notify.org/iss-noew.json', params=parameters)
    response.raise_for_status()
    data = response.json()

    sunrise = int(data['result']['sunrise'].split('T')[1].split(':')[0])
    sunset = int(data['result']['sunset'].split('T')[1].split(':')[0])

    time_now = datetime.now().hour
    if time_now >= sunset or time_now <= sunrise:
        return True

while True:
    time.sleep(60)
    if isOverhead() and isNight():
        connection = smtplib.SMTP('smtp.gmail.com')
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg='Subject:Look up ISS\n\nISS is above you in the sky.\nISS 위성이 당신의 머리 위 밤하늘에 지나가고 있습니다.'
        )