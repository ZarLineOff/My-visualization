import csv
from datetime import datetime
from matplotlib import pyplot as plt

plt.style.use('bmh')
filename = 'C:/Users/ivann/PycharmProjects/Data visualization/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    highh = next(reader)
    dates, highs = [], []
    for row in reader:
        current_day = datetime.strptime(row[2], "%Y-%m-%d")
        try:
            high = float(row[3])
        except ValueError:
            print(f'Missing data for {current_day}')
        else:
            dates.append(current_day)
            highs.append(high)
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red')
plt.title('Осадки в Ситке', fontsize=20)
plt.xlabel('', fontsize=16)
plt.ylabel('Осадки', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=20)
fig.autofmt_xdate()
plt.show()