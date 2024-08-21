from die import Die
from plotly.graph_objs import Bar,Layout
from plotly import offline
die_1 = Die()
die_2 = Die()
results = []
for roll_number in range(1000):
    result = die_1.roll()+die_2.roll()
    results.append(result)
freqs = []
point_number = die_1.num_sides+die_2.num_sides
for value in range(2,point_number+1):
    freq = results.count(value)
    freqs.append(freq)
x_value = list(range(2,point_number+1))
data = [Bar(x=x_value,y=freqs)]
x_name = {'title': 'Numbers', 'dtick': 1}
y_name = {'title': 'Numbers2'}
my_layout = Layout(title = 'Results of the sigma',xaxis=x_name,yaxis=y_name)
offline.plot({'data': data, 'layout': my_layout},filename='myd6.html')