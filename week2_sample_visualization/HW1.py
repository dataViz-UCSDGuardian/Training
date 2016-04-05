import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import openpyxl

# Adult and airfoils dataset are taken from UCI ML Repository

#********************
#   Bar Plot
#********************
data = pd.read_csv('adult.test.txt',
                    skiprows=2,
                    error_bad_lines=False,
                    header = None,
                    delimiter=',',
                    usecols=[0,9]) # Taking only two features

# Cleaning up data  - using only first 20 rows.
new_data =  data.iloc[:20]
age = pd.to_numeric(new_data[0])
sex = []
for i in new_data[9]:
    sex.append(str(i))

# Setting the figure size and removing the margins
plt.figure(figsize=(11, 9))
ax = plt.subplot(111)
ax.spines["top"].set_visible(False)
ax.spines["bottom"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)
ax.get_xaxis().tick_bottom()
ax.get_yaxis().tick_left()

# Bar plot using seaborn
fig1 = sns.barplot(sex, age, palette="Blues")
plt.xlabel('Gender', fontsize = 15)
plt.ylabel('Age', fontsize = 15)
plt.title('Age comparison by Gender', fontsize = 20)
plt.show(fig1)

#********************
#   Bubble Plot
#********************
# Preprocessing data
data = pd.read_csv('airfoil_self_noise.dat.txt',
                    delimiter='\t',
                    skiprows=0,
                    error_bad_lines=False,
                    header = None)
new_data = data.iloc[:120] #using first 120 rows

# Choosing three attributes for our graph
angle_of_attack = new_data[1]
sound_pressure_level = new_data[5]
velocity = new_data[3]

mpl_fig_bubble = plt.figure(figsize=(10, 8))
ax = mpl_fig_bubble.add_subplot(111)

scatter = ax.scatter(
    sound_pressure_level,   # x location
    angle_of_attack,        # y location
    c='blue',               # color of the bubble
    s = [20*n for n in range(len(velocity))],
    linewidths=2,           #size of border line
    edgecolor='w',          #color of border line
    alpha=0.5               #how see-through the bubbles are
)
plt.xlim(110, 120)

plt.title("Sound Pressure vs Angle of attack of airfoils", fontsize = 20)
plt.xlabel("Sound Pressure Level", fontsize=15)
plt.ylabel("Angle of Attack (in degrees)", fontsize=15)
plt.show()
