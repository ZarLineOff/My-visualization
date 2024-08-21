import csv
from datetime import datetime
from matplotlib import pyplot as plt

filename = 'C:/Users/ivann/PycharmProjects/Data visualization/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    hurrent = next(reader)
    dates, highs, lows = [], [], []
    for row in reader:
        dates.append(datetime.strptime(row[2], '%Y-%m-%d'))
        highs.append(int(row[5]))
        lows.append(int(row[6]))
plt.style.use('bmh')
fig,ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, lows, highs, facecolor='blue', alpha=0.6)
plt.title('Температура в Ситке', fontsize=24)
plt.ylabel('Температура(F)', fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=14)
fig.autofmt_xdate()
plt.show()