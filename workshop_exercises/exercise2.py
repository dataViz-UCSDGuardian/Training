import matplotlib.pyplot as plt
import plotly.plotly as py
import pandas as pd

# Read the data into a pandas DataFrame.
gender_degree_data = pd.read_csv("http://www.randalolson.com/wp-content/uploads/percent-bachelors-degrees-women-usa.csv")
plt.figure(figsize=(12, 14))

##Lesson 2- Format the plot image pt 1
# Remove the plot frame lines. They are unnecessary chartjunk.
ax = plt.subplot(111)
ax.spines["top"].set_visible(False)
ax.spines["bottom"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_visible(False)

#Let's see what the figure looks like

ax.get_xaxis().tick_bottom()
ax.get_yaxis().tick_left()

plt.ylim(0, 90)
plt.xlim(1968, 2014)
plt.yticks(range(0, 91, 10), [str(x) + "%" for x in range(0, 91, 10)], fontsize=14)
plt.xticks(fontsize=14)

tableau20 = [(31, 119, 180), (174, 199, 232), (255, 127, 14), (255, 187, 120),
             (44, 160, 44), (152, 223, 138), (214, 39, 40), (255, 152, 150),
             (148, 103, 189), (197, 176, 213), (140, 86, 75), (196, 156, 148),
             (227, 119, 194), (247, 182, 210), (127, 127, 127), (199, 199, 199),
             (188, 189, 34), (219, 219, 141), (23, 190, 207), (158, 218, 229)]
for i in range(len(tableau20)):
    r, g, b = tableau20[i]
    tableau20[i] = (r / 255., g / 255., b / 255.)

print (tableau20)
majors = ['Health Professions', 'Public Administration', 'Education', 'Psychology',
          'Foreign Languages', 'English', 'Communications\nand Journalism',
          'Art and Performance', 'Biology', 'Agriculture',
          'Social Sciences and History', 'Business', 'Math and Statistics',
          'Architecture', 'Physical Sciences', 'Computer Science',
          'Engineering']

for rank, column in enumerate(majors):
    # Plot each line separately with its own color, using the Tableau 20
    # color set in order.
    plt.plot(gender_degree_data.Year.values,
            gender_degree_data[column.replace("\n", " ")].values,
            lw=2.5, color=tableau20[rank])

for rank, column in enumerate(majors):
    plt.plot(gender_degree_data.Year.values,
             gender_degree_data[column.replace("\n", " ")].values,
             lw=2.5, color=tableau20[rank])
y_pos = gender_degree_data[column.replace("\n", " ")].values[-1] - 0.5
plt.text(2011.5, y_pos, column, fontsize=14, color=tableau20[rank])
for rank, column in enumerate(majors):
    # Plot each line separately with its own color, using the Tableau 20
    # color set in order.
    plt.plot(gender_degree_data.Year.values,
            gender_degree_data[column.replace("\n", " ")].values,
            lw=2.5, color=tableau20[rank])

    # Add a text label to the right end of every line. Most of the code below
    # is adding specific offsets y position because some labels overlapped.
    y_pos = gender_degree_data[column.replace("\n", " ")].values[-1] - 0.5
    if column == "Foreign Languages":
        y_pos += 0.5
    elif column == "English":
        y_pos -= 0.5
    elif column == "Communications\nand Journalism":
        y_pos += 0.75
    elif column == "Art and Performance":
        y_pos -= 0.25
    elif column == "Agriculture":
        y_pos += 1.25
    elif column == "Social Sciences and History":
        y_pos += 0.25
    elif column == "Business":
        y_pos -= 0.75
    elif column == "Math and Statistics":
        y_pos += 0.75
    elif column == "Architecture":
        y_pos -= 0.75
    elif column == "Computer Science":
        y_pos += 0.75
    elif column == "Engineering":
        y_pos -= 0.25

    # Again, make sure that all labels are large enough to be easily read
    # by the viewer.
    plt.text(2011.5, y_pos, column, fontsize=14, color=tableau20[rank])

plt.text(1995, 93, "Percentage of Bachelor's degrees conferred to women in the U.S.A."
       ", by major (1970-2012)", fontsize=17, ha="center")

plt.text(1966, -8, "Data source: nces.ed.gov/programs/digest/2013menu_tables.asp"
       "\nAuthor: Randy Olson (randalolson.com / @randal_olson)"
       "\nNote: Some majors are missing because the historical data "
       "is not available for them", fontsize=10)

plt.show()
