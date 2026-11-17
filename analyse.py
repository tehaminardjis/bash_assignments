import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Lecture du fichier CSV
data = pd.read_csv("resultats/mesures.csv")

# Afficher les 5 premières lignes
print(data.head())

# Calculer la moyenne
moyenne = data["Concentration"].mean()
print("Moyenne :", moyenne)

# Moyenne d'une colonne
print(data["Concentration"].mean())

# Visualiser les résultats
sns.lineplot(x="Temps", y="Concentration", data=data)
plt.show()

# Graphique de dispersion
sns.scatterplot(x="Temps", y="Concentration", data=data)
plt.show()
