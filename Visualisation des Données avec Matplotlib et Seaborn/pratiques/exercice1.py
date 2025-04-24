# Tracez une courbe pour la fonction y = x² pour x de 0 à 10 avec Matplotlib.
import matplotlib.pyplot as plt

# Définir les données
x = [i for i in range(11)]
y = [i**2 for i in x]
# Tracer la courbe
plt.plot(x, y, marker='o', linestyle='-', color='b')

# Ajouter un titre et des labels
plt.title("Courbe de y = x²")
plt.xlabel("Axe des X")
plt.ylabel("Axe des Y")
plt.show()