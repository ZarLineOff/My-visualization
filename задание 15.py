import matplotlib.pyplot as plt
fig,ax = plt.subplots()
plt.style.use('fivethirtyeight')
x_values = range(1,5001)
y_values = [x**3 for x in x_values]
ax.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Reds,s=10)
ax.set_title("Кубы чисел от 1 до 5000", fontsize=24)
ax.set_xlabel("Кубы", fontsize=14)
ax.set_ylabel("Числа", fontsize=14)
ax.tick_params(axis='both', which='major', labelsize=14)
plt.show()