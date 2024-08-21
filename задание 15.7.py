from die import Die
from plotly.graph_objs import Bar,Layout
from plotly import offline

die_1 = Die()
die_2 = Die()
die_3 = Die()
results = []
for roll_number in range(50000):
    result = die_1.roll() + die_2.roll() + die_3.roll()
    results.append(result)
freqs = []
max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
for value in range(3,max_result+1):
    freq = results.count(value)
    freqs.append(freq)
x_values = list(range(3,max_result+1))
data = [Bar(x=x_values, y = freqs)]
x_axis_config = {'title': 'Number of the roll', 'dtick': 1}
y_axis_config = {'title': 'Frequencions'}
my_layout = Layout(title='Results of the bim bim bam bam', xaxis=x_axis_config,yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='15.7.html')