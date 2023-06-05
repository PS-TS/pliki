import matplotlib.pyplot as plt
sizes = [15.70,25.58,16.86,21.51,12.79,7.56]
sizes2 = [20.37,17.59,9.72,19.91,15.74,16.67]
labes = ["A","B","C","D","E","F"]
colors = ['brown','pink','bisque','lightgreen','brown','blue']
explode = [0,0.1,0,0,0,0]
plt.subplot(2,2,1)
plt.title("Lewa Góra")
plt.pie(sizes, explode=explode,labels=labes,colors=colors,autopct='%1.2f%%',startangle=50)
plt.subplot(2,2,4)
plt.title("Prawa Dół")
plt.pie(sizes2, explode=explode,labels=labes,colors=colors,autopct='%1.2f%%',startangle=50)
plt.axis('equal')
plt.savefig("zad1.jpg")
plt.show()