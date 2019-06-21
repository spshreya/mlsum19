import matplotlib.pyplot as plt
x=[2,3]
y=[9,5]
x1=[4,3,8]
y1=[2,9,7]
plt.xlabel('time')
plt.ylabel('speed')
plt.bar(x1,y1,label='water')
plt.bar(x,y,label='speed')
plt.grid(color='green')
plt.legend()
plt.xlim(0,12)
plt.ylim(0,15)
