import matplotlib.pyplot as plt
fig, ax = plt.subplots()
x_values = list(range(1,1001))
plt.style.use('seaborn-v0_8')
y_values = [x**2 for x in x_values]
ax.scatter(x_values,y_values,c = y_values,cmap=plt.cm.Blues,s = 10)
ax.set_title('Square Number', fontsize = 24)
ax.set_xlabel('Value', fontsize = 24)
ax.set_ylabel('Square of Value', fontsize = 14)
ax.tick_params(axis='both', which='major',labelsize = 14)
ax.axis([0,1100,0,1100000])
plt.savefig('square_plot.png',bbox_inches = 'tight')
plt.show()