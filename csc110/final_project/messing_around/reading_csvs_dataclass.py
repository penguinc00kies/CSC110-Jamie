"""reading csv files using csv and dataclass, then graphing using the dataclass"""

from dataclasses import dataclass
import plotly.graph_objects as go
import csv


@dataclass
class City:
    """A data type representing a city and its coordinates on a map
    """
    name: str
    lat: float
    lon: float


def process_row(row: list[str]) -> City:
    """Convert a row of city data to City object.
    """
    return City(row[0], float(row[2]), float(row[3]))


with open('../data/2014_us_cities.csv') as file:
    reader = csv.reader(file)
    headers = next(reader)
    data = []
    # process only the first 10 rows of the csv file
    for _ in range(0, 10):
        data.append(process_row(next(reader)))

# traces require lists or dataframe columns, so I can't use a for loop to iterate through each city
# in data one at a time and add_trace, so I'm making 3 lists that each contain all of the latitudes,
# longitudes, and names of each city in data
latitudes = [city.lat for city in data]
longitudes = [city.lon for city in data]
names = [city.name for city in data]
fig1 = go.Figure()

fig1.add_trace(go.Scattergeo(
    locationmode='USA-states',
    lon=longitudes,
    lat=latitudes,
    text=names,
    marker=dict(
        size=20,
        color="royalblue",
        line_color='rgb(40,40,40)',
        line_width=0.5,
        sizemode='area'
    ),
    name='10 Cities'))

fig1.update_layout(
    title_text='2014 US city populations<br>(Click legend to toggle traces)',
    showlegend=True,
    geo=dict(
        scope='usa',
        landcolor='rgb(217, 217, 217)',
    )
)

# the final graph should be identical to reading_csvs_pandas.py
fig1.show()
