#!/usr/bin/python3

from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

webpage = "http://forecast.weather.gov/MapClick.php?lat=47.60357&lon=-122.32945"##choose webpage to visit
openpage = urlopen(webpage) ##open a link to the URL
soup = BeautifulSoup(openpage, 'html.parser') ##retrieve all the HTML code

current_conditions = soup.find(id='current-conditions')
current_headers = [cc.get_text() for cc in current_conditions.select('td')]
current_summary = soup.find(id='current_conditions-summary')
current_ctemp = current_summary.find(class_='myforecast-current-sm').get_text()
if current_ctemp.endswith('C'):
    current_ctemp = current_ctemp[:-2]
current_update = current_headers[11].strip()
if current_update.endswith('PDT'):
    current_update = current_update[:-4]
tempdata = pd.DataFrame({"Temperature":[current_ctemp],
                         "Time":[current_update],
                         })
with open('/home/jlew/Programming/Python/Webcrawler/Weather/output.csv', 'a') as file:
    tempdata.to_csv(file, sep='\t', columns=2, header=False, index=False)
                            
