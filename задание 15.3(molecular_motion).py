import matplotlib.pyplot as plt
from random_walk import RandomWalk
"""Построение случайного блуждания"""
while True:
    rw = RandomWalk(5000)
    rw.fill_walk()
    """Нанесение точек на диаграмму"""
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(15,9),dpi=100)
    point_numbers = range(rw.num_points)
    plt.plot(rw.x_values, rw.y_values, linewidth=1)
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    ax.scatter(0,0,c='green',edgecolors='none',s=100,linewidth = 1)
    ax.scatter(rw.x_values[-1],rw.y_values[-1],c='red',edgecolors='none',s=100,linewidth = 1)
    plt.show()
    keep_running = input('Make another walk(y/n)?:')
    if keep_running == 'n':
        break