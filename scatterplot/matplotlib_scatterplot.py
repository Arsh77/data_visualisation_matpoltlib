import matplotlib.pyplot as plt
x=[1,2,3,10,8,9,5]
y=[1,2,3,4,5,6,7]

plt.scatter(x,y , label = 'scatter' , color='g' ,s=25, marker='x')

plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title('Scatter plot')
plt.legend()
plt.show()
