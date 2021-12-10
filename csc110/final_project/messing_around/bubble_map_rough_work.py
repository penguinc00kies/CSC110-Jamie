"""display a bubble map with color-coded bubbles corresponding to a state's political leaning
and size proportionate to the increase in hate crimes"""

import plotly.graph_objects as go
import csv
import pandas as pd


def process_row(row: list[str], state_colour: dict[str, str]) -> None:
    """Convert a row to a mapping of a state and its colour
    """
    state_colour[row[0]] = row[1]


with open('../data/state_colour_data.csv') as file:
    reader = csv.reader(file)
    headers = next(reader)
    state_colour = {}

    for row in reader:
        process_row(row, state_colour)

coordinates = pd.read_csv('../data/2014_us_cities.csv')
hate_crime_data = pd.read_csv('../data/hate_crime_data.csv')
# instantiate a new column called colour, I just needed to assign it placeholder dummy values
hate_crime_data['colour'] = hate_crime_data['US City']
# instantiate a new column called lat, I just needed to assign it placeholder dummy values
hate_crime_data['lat'] = hate_crime_data['US City']
# instantiate a new column called lon, I just needed to assign it placeholder dummy values
hate_crime_data['lon'] = hate_crime_data['US City']

# searches coordinates for cities that are also in hate_crime_data, and then assigns the
# corresponding latitudes and longitudes from coordinates to the matching city in hate_crime_data
for i in range(hate_crime_data.__len__()):
    for j in range(coordinates.__len__()):
        if hate_crime_data['US City'][i] == coordinates['name'][j]:
            hate_crime_data['lat'][i] = coordinates['lat'][j]
            hate_crime_data['lon'][i] = coordinates['lon'][j]

# assigns each city in hate_crime_data it's proper colour(ie, political leaning) by indexing the
# dictionary state_colour
for i in range(hate_crime_data.__len__()):
    # this line will throw a warning, but the code still works as indented
    hate_crime_data['colour'][i] = state_colour[hate_crime_data['US State'][i]]

fig = go.Figure()

fig.add_trace(go.Scattergeo(
    lon=hate_crime_data['lon'],
    lat=hate_crime_data['lat'],
    text=hate_crime_data['US City'],
    marker=dict(
        size=15,
        color=hate_crime_data['colour'],
        line_color='rgb(40,40,40)',
        line_width=0.5,
        sizemode='area'
    ),
    name='US City'))

fig.update_layout(
    title_text='US City Colours<br>(Click legend to toggle traces)',
    showlegend=True,
    geo=dict(
        scope='usa',
        landcolor='rgb(217, 217, 217)',
    )
)

fig.show()
