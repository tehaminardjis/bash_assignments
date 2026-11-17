import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Lecture du fichier CSV
data = pd.read_csv("results.csv")

# Afficher les 5 premières lignes
print(data.head())

# Calculer la moyenne
moyenne = data["Concentration"].mean()
print("moyenne :", moyenne)

# Graphique de dispersion
sns.scatterplot(x="Temps", y="Concentration", data=data)
plt.show()

# Visualiser les résultats
sns.lineplot(x="Temps", y="Concentration", data=data)
plt.show()
