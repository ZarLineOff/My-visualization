import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename = 'C:/Users/ivann/PycharmProjects/Data visualization/death_valley_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2],"%Y-%m-%d")
        try:
            high = int(row[4])
            low = int(row[5])
        except ValueError:
            print(f'Missing data for {current_date}')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
plt.style.use('bmh')
fig,ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha= 0.5)
plt.plot(dates, lows, c='blue', alpha= 0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.2)
title = 'Daily high and low temperatures - 2018\nDeath Valley, CA'
plt.title(title, fontsize = 20)
plt.xlabel('', fontsize = 16)
fig.autofmt_xdate()
plt.ylabel('Temperature (F)', fontsize = 16)
plt.tick_params(axis='both', which = 'major', labelsize = 16)
ax.set_ylim(10,140)
plt.show()