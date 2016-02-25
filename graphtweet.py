import matplotlib.animation as animation
import time
import matplotlib.pyplot as plt
from matplotlib import style

style.use("ggplot")

fig=plt.figure()
ax1=fig.add_subplot(1,1,1)

def animate(i):
	pullData = open("twitter-out.txt","r")
	#lines = pullData.split('\n')
	xar =[]
	yar=[]
	x=0
	y=0
	for l in pullData:
		x+=1
		if float(l)>0:
			y+=1
		elif float(l)<=0:
			y-=1
		xar.append(x)
		yar.append(y)
	ax1.clear()
	ax1.plot(xar,yar)
ani=animation.FuncAnimation(fig,animate,interval=1000)
plt.show()
