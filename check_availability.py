#!/usr/bin/python3

import datetime
import os
import requests
from os import path
import config

current_time=str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

print('--------------------------------------')
print(current_time)

def create_file(pth):
  if not path.exists(pth):
    with open(pth, 'w') as file:
      file.write('')
    print('File '+pth+' created!')

current_path = config.path+'/current.txt'
last_path = config.path+'/last.txt'

create_file(current_path)
create_file(last_path)

headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36'}
payload = {'form1': 'form1', 'form1:j_id_jsp_1457171577_15:0:j_id_jsp_1457171577_18': 'Make a Reservation', 'javax.faces.ViewState': 'j_id1:j_id2'}

with requests.session() as session:
  session.get('https://secure.emybill.com/parks/reservation/base/TravisHamilton/publicSite/main.faces')
  request=session.post('https://secure.emybill.com/parks/reservation/base/TravisHamilton/publicSite/main.faces', data=payload, headers=headers)
  data=session.get('https://secure.emybill.com/parks/reservation/calendar?visible=true&shelter=Hamilton%20Pool%20Preserve&start=2019-08-15&end=2019-10-13')
  #change start and end date if needed

#dates to check
dates = config.dates

available = ''

for entry in data.json():
  if 'Available' in entry['title']:
    if entry['start'][5:10] in dates:
      available+=entry['start']+' '+entry['title']+'\n'

print('Availability:')
print(available)

os.remove(last_path)
os.rename(current_path, last_path)

with open(current_path, 'w') as file:
  file.write(available)
