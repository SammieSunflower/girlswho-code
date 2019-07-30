import music
import matplotlib.pyplot as plt
import numpy as np
#import pandas as pd
#import seaborn as sns
#from scipy import stats

i = music.get_songs()
pop = []
tempo = []

for row in i:
    #print(row["artist"]["hotttnesss"])
    d = row["artist"]["hotttnesss"]
    pop.append(d)

for row in i:
    #print(row ["song"]["tempo"])
    c = row ["song"]["tempo"]
    tempo.append(c)

#x = np.random.normal(size=100)
#sns.distplot(x);
#plt.hist(pop, bins=[0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.75, 1])
plt.title("Does the artist popularity affect the song tempo?")
plt.hist(pop, bins=[0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.75, 1], rwidth=0.8, color='y', edgecolor='orange',
              linewidth=1)
#plt.bar(pop, tempo, align='center', alpha=0.5)
plt.xlabel("Popularity")
plt.ylabel("Tempo")
plt.grid(True)
plt.show()
