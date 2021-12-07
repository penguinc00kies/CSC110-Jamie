"""test file for using plotly's graph objects
original source code from https://plotly.com/python/bubble-maps/

additional references for scattergeo sourced from here
https://plotly.com/python-api-reference/generated/plotly.express.scatter_geo
https://plotly.com/python/reference/scattergeo/
"""

import plotly.graph_objects as go

import pandas as pd

# converts the csv file into the data frame
df = pd.read_csv('../data/2014_us_cities.csv')
# return the header of the dataframe
df.head()

# a dataframe is a 2-dimensional data structure with three key parts: rows, columns, and data
# for the purposes of storing a csv, just imagine that the dataframe is an array columns with the
# same name as the csv headers and the same number of rows in the csv

# appending a new column within the dataframe, combiding data from other columns
df['text'] = df['name'] + '<br>Population ' + (df['pop'] / 1e6).astype(str) + ' million'
# top 2 populated cities, top 3-10 populated cities, etc...
limits = [(0, 2), (3, 10), (11, 20), (21, 50), (50, 3000)]
colors = ["royalblue", "crimson", "lightseagreen", "orange", "lightgrey"]
cities = []
scale = 5000

# you can either index a dataframe like df[column] or df[column][row]
# the first option will return every single row in the column
# the second option is self explanatory, it works just like nested list indexing

fig = go.Figure()

for i in range(len(limits)):
    lim = limits[i]
    # df_sub is not essentially a subset set of df, containing rows lim[0] inclusive to lim[1] exclusive
    df_sub = df[lim[0]:lim[1]]
    # trace is just the name for a collection of data and the specifications of how the data will be plotted
    # a scatergeo is an acceptable parameter since it's a trace
    fig.add_trace(go.Scattergeo(
        # determines the set of locations used to match entries in locations to regions on the map
        # not necessary if you already have latitude and longitude
        # locationmode='USA-states',
        # lon, lat, and text can each either take a list OR a Pandas series of values, and each
        # element per dataset is linked to the other two at the same indexes
        lon=df_sub['lon'],
        lat=df_sub['lat'],
        text=df_sub['text'],
        # marker
        marker=dict(
            # size can take a number or an array of numbers
            size=df_sub['pop'] / scale,
            color=colors[i],
            line_color='rgb(40,40,40)',
            line_width=0.5,
            sizemode='area'
        ),
        # name of the trace(in this case, the same name will apply to multiple data points)
        name='{0} - {1}'.format(lim[0], lim[1])))

fig.update_layout(
    title_text='2014 US city populations<br>(Click legend to toggle traces)',
    showlegend=True,
    geo=dict(
        scope='usa',
        landcolor='rgb(217, 217, 217)',
    )
)

fig.show()
