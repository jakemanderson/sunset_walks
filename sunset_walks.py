'''
A Program designed to notify Jake and Alayne when they need to leave for their evening walk
in order to not be too hot, too cold, too bright, or too dark. 
'''
from datetime import date, timedelta
from suntime import Sun

import personal_info as pi


def suffix(d):
    return 'th' if 11<=d<=13 else {1:'st',2:'nd',3:'rd'}.get(d%10, 'th')

def custom_strftime(format, t):
    return t.strftime(format).replace('{S}', str(t.day) + suffix(t.day))


latitude = pi.home_latitude
longitude = pi.home_longitude

sun = Sun(latitude, longitude)

# Local time
today = date.today()
sunset_time = sun.get_local_sunset_time(today)
walk_departure_time = sunset_time - timedelta(hours=1, minutes=15)
print("Hi Sweetie! \n\n Today, {}, the sun sets at {}, so we should leave to go on our walk at {}. \n\n - JakeBot :)".
      format(custom_strftime('%B {S}, %Y', today), sunset_time.strftime('%I:%M %p'), walk_departure_time.strftime('%I:%M %p')))
