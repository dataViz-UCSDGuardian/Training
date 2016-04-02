import openpyxl
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('Crimes.csv', sep=',')

df = df.drop(df.index[0])  # drop first row (US totals)
df = df[df['murder'] < 11] # remove outliers
print(df)

mpl_fig_bubble = plt.figure()         # (!) set new mpl figure object
ax = mpl_fig_bubble.add_subplot(111)  # add axis

plt.axis([0,11,200,1280])
plt.xlabel('Murders per 100,000 population')
plt.ylabel('Burglaries per 100,000 population')

#Lesson 4: Plot
scatter = ax.scatter(
    df['murder'],           # x location
    df['burglary'],         # y location
    c=df['larceny_theft'],  # color of the bubble
    s=np.sqrt(df['population']), #radius circle
    linewidths=2,           #size of border line
    edgecolor='w',          #color of border line
    alpha=0.6               #how see-through the bubbles are
)

#Lesson 5: Add labels
for i_X, X in df.iterrows():
    plt.text(
        X['murder'],
        X['burglary'],
        X['state'][0:8], # only the first 8 letters
        size=8,
        horizontalalignment='center'
    )

plt.title("Murders vs Burgalaries in the US by State in 2005", fontsize = 20)
plt.show()
