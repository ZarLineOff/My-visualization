from die import Die
from plotly.graph_objs import Bar,Layout
from plotly import offline
die = Die()
results = []
for roll_number in range(1000):
    result = die.roll()
    results.append(result)
freqs = []
for value in range(1,die.num_sides+1):
    freq = results.count(value)
    freqs.append(freq)
x_vaule = list(range(1,die.num_sides+1))
data = [Bar(x=x_vaule,y=freqs)]
x_axis_cing = {'title': 'Result'}
y_axis_cing = {'title': 'Freq'}
my_layout = Layout(title='TResults of rolling one D6 1000 times', xaxis=x_axis_cing,yaxis=y_axis_cing)
offline.plot({'data': data, 'layout': my_layout}, filename='myd6.html')