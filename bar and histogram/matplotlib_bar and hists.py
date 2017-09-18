import matplotlib.pyplot as plt

plt.bar([1,3,5,7,9],[5,2,7,8,2],label='bar_1' , color='g')
plt.bar([2,4,6,8,10],[8,6,2,5,6],label='bar_2',color='r' )
plt.legend()
plt.xlabel('bar width')
plt.ylabel('bar height')
plt.title('bar graph')
plt.show()

# for histograms

population_ages=[22,55,62,45,21,22,34,42,42,4,99,102,110,120,121,122,130,111,115,112,80,75,65,54,44,43,42,48]
bins=[0,10,20,30,40,50,60,70,80,90,100,110,120,130]
plt.hist(population_ages,bins,histtype='bar',rwidth=0.8)

plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title('Histogram')
plt.legend()
plt.show()
