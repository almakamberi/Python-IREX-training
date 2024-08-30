import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("../day9/data/avgIQpercountry.csv")

nobel_prizes_by_continent=df.groupby("Continent")["Nobel Prices"].sum()

no_of_continents=nobel_prizes_by_continent.count()

print(no_of_continents)

colors=["gold","lightcoral","yellow","green","orage"]\

plt.figure(figsize=(10,10))

nobel_prizes_by_continent.plot(kind="pie",autopct='%1.1f%%',color=colors)

plt.show()