from die import Die
from plotly.graph_objs import Bar, Layout
from plotly import offline

die_1 = Die()
die_2 = Die()
results = []
for roll_number in range(50000):
    roll = die_2.roll() + die_1.roll()
    results.append(roll)
freqs = []
max_results = die_2.num_sides + die_1.num_sides
for value in range(2,max_results+1):
    count = results.count(value)
    freqs.append(count)
x_values = list(range(2,max_results+1))
data = [Bar(x=x_values,y=freqs)]
x_axis_config = {'title': 'My results', 'dtick': 1}
y_axis_config = {'title': 'Numbers'}
my_layout = Layout(title='Max results', xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6.html')