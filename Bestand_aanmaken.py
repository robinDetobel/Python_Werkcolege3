import pandas as pd

uitgave = {'categorie': [],
           'bedrag': []
           }
awnser = "y"

while awnser.lower() == "y":
    uitgave['categorie'].append(input("Welke soort van uitgave wilt u ingeven? "))
    uitgave['bedrag'].append(input("Wat is hiervoor het bedag? "))
    awnser = input("Wilt u nog een uitgave ingeven? ")

df = pd.DataFrame(uitgave, columns=['categorie', 'bedrag'])

df.to_excel("data/test.xlsx")

uitgaven = pd.read_excel("data/test.xlsx")

max_uitgave = uitgaven['bedrag'].max()
gem_uitgave = uitgaven['bedrag'].mean()
gem_per_cat = uitgaven.groupby('categorie')['bedrag'].mean()
tot_per_cat = uitgaven.groupby('categorie')['bedrag'].sum()

print(max_uitgave)
print(gem_uitgave)
print(gem_per_cat)
print(tot_per_cat)