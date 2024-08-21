import matplotlib.pyplot as plt
from random_walk import RandomWalk
while True:
    rw = RandomWalk(5000)
    rw.fill_walk()
    plt.style.use('classic')
    fig, ax = plt.subplots()
    x_values = list(range(rw.x_values))
    ax.scatter(rw.x_values, rw.y_values, c=x_values, cmap=plt.cm.Blues, s=1)
    ax.get_xaxis().set_visible(False)
