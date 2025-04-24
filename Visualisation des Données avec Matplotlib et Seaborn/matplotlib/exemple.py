import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

plt.plot(x,y,marker='x', linestyle='-', color='b')
plt.title("Exemple de courbe")
plt.xlabel("Axe des X")
plt.ylabel("Axe des Y")
plt.grid(True)
plt.show()
