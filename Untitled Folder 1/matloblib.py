# import matplotlib
# print(matplotlib.__version__)

# import matplotlib.pyplot as plt

# x=[1,2,3,4]
# y=[1,4,9,16]
# plt.plot(x,y)
# plt.show()

# import matplotlib.pyplot as plt
 
# x=[0,2,4,6,8]
# y=[0,4,16,36,64]
# fig, ax=plt.subplots()
# ax.plot(x,y,marker='o',label="Data Points")
# ax.set_title("Basic Components of Matplotlub Figure")
# ax.set_xlabel("X-axis")
# ax.set_ylabel("Y-axis)")
# plt.show()


# import matplotlib.pyplot as plt
# import numpy as np
# xpoints = np.array([0,6])
# ypoints = np.array([3,10])
# plt.plot(xpoints,ypoints)
# plt.show()


# import matplotlib.pyplot as plt
# import numpy as np

# x=np.linspace(0,10,100)
# y=np.sin(x)

# plt.plot(x,y,label='sin(x)',color='blue',linestyle='--')
# plt.title('Line plot of sin(x)')
# plt.xlabel("X-axis")
# plt.ylabel('Y-axis')
# plt.legend()
# plt.grid(True)
# plt.show()


# import matplotlib.pyplot as plt
# x=[1,2,3,4,5]
# y=[5,7,9,11,13]
# plt.scatter(x,y)
# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np
# x = np.random.rand(50)
# y= np.random.rand(50)
# plt.scatter(x,y,color='green',alpha=0.7)
# plt.title('scatter plot of random points')
# plt.xlabel("X-axis")
# plt.ylabel('Y-axis')
# plt.show()

# import matplotlib.pyplot as plt
# categories=['A','B','C','D']
# values=[3,7,2,5]
# plt.bar(categories,values)
# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np 
# categories=['A','B','C','D']
# values =[10,20,15,25]
# plt.bar(categories,values,color='orange')
# plt.title('Bar Plot Ex')
# plt.xlabel('Categories')
# plt.ylabel('Values')
# plt.show()


# import matplotlib.pyplot as plt
# import numpy as np 
# data=np.random.randn(1000)
# plt.hist(data,bins=30)
# plt.show()

# import matplotlib.pyplot as plt
# labels=['Python','Java','c++','js']
# sizes=[40,30,20,10]
# plt.pie(sizes,labels=labels,autopct='%1.1f%%')
# plt.show()


# import numpy as np
# import matplotlib.pyplot as plt 

# x=np.linspace(0,10,100)
# y1=np.sin(x)
# y2=np.cos(x)

# plt.plot(x,y1,label='sin(x)',color='red',linewidth=2,marker='o')
# plt.plot(x,y1,label='cos(x)',color='blue',linestyle='dotted')
# plt.title('Customized line Plot')
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
# plt.legend()
# plt.grid(True,linestyle='--',color='gray',alpha=0.6)
# plt.show()


import numpy as np
import matplotlib.pyplot as plt 

x=np.arrange(0.0,2.0,0.01)
y=1+ np.sin(2*np.p1*x)

fig