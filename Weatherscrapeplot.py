import csv
import datetime
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.finance import date2num
from matplotlib import dates

file = open('output.csv', 'r') #open the output file from weather grabbing script

data = pd.read_csv('output.csv', '\t') #read the data to a panda dataframe
times = data.Time.tolist() #grab the corresponding columns using the pd titles
temps = data.Temp.tolist()

float_times = [] #need to change times from str to floats for plotting
for item in times:
    float_times.append(date2num(datetime.datetime.strptime(item, '%d %b %I:%M %p')))
float_temps = [] #need to change temps from str to float for plotting
for t in temps: 
    float_temps.append(float(t))

#plotting section, need to remember to show the plot
ax = plt.gca() #get current axes
plt.plot(float_times, temps, color='b', linestyle='-', linewidth=2)
ax.grid(color='k', linestyle='-', linewidth=0.5)
plt.tight_layout()
plt.title('Seattle Temperatures')
plt.xlabel('Date')
plt.ylabel('Temperature in C')
#x-axes
xaxlabform = dates.DateFormatter('%d %b %I:%M %p') #set x-axis display format
ax.xaxis.set_major_formatter(xaxlabform) #apply x-axis display format
ax.xaxis.set_major_locator(dates.DayLocator())
ax.yaxis.grid(True,which='major')
#y-axes
plt.ylim(-15,30)
ax.set_yticks([-15,0,30],minor=False)
ax.set_yticks([-10,-5,5,10,15,20,25],minor=True)
ax.yaxis.grid(True,which='major')
ax.yaxis.grid(True,which='minor')

plt.show()



