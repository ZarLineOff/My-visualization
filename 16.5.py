import csv
from datetime import datetime
from matplotlib import pyplot as plt

filename = 'C:/Users/ivann/PycharmProjects/Data visualization/death_valley_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    station, tobs = [], []
    for row in reader:
        stations = row[1]
        tob = row[6]
        station.append(stations)
        tobs.append(tob)
plt.style.use('bmh')
fig, ax = plt.subplots()
ax.plot(tobs, c='red')
ax.plot(stations, c='green')
plt.title('Осадки', fontsize=24)
plt.ylabel('кол-во', fontsize=10)
plt.xlabel('сигма', fontsize=16)
fig.autofmt_xdate()
plt.show()