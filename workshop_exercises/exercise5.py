import bokeh.sampledata
bokeh.sampledata.download()
#We are using sample data from Bokeh, located here
# https://github.com/bokeh/bokeh/tree/master/bokeh/sampledata

from bokeh.plotting import figure, show, output_file
from bokeh.sampledata.us_counties import data as counties
from bokeh.sampledata.us_states import data as states
from bokeh.sampledata.unemployment import data as unemployment

del states["HI"]
del states["AK"]

EXCLUDED = ("ak", "hi", "pr", "gu", "vi", "mp", "as")

state_xs = [states[code]["lons"] for code in states]
state_ys = [states[code]["lats"] for code in states]

#Get the longitudes and latitudes for each county
county_xs=[counties[code]["lons"] for code in counties if counties[code]["state"] not in EXCLUDED]
county_ys=[counties[code]["lats"] for code in counties if counties[code]["state"] not in EXCLUDED]

county_colors = []
for county_id in counties:
    if counties[county_id]["state"] in EXCLUDED:
        continue
    try:
        rate = unemployment[county_id]
        idx = int(rate/6)
        county_colors.append(colors[idx])
    except KeyError:
        county_colors.append("black")

#Lesson 4: Add Title, toolbar, determine size
p = figure(title="US Unemployment 2009", toolbar_location="left",
           plot_width=1100, plot_height=700)
show(p)
