"""reading csv files using Pandas dataframes, then graphing using the dataframe"""

import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv('../data/2014_us_cities.csv')
df = df[0:10]

fig1 = go.Figure()

fig1.add_trace(go.Scattergeo(
    locationmode='USA-states',
    lon=df['lon'],
    lat=df['lat'],
    text=df['name'],
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

# the final graph should be identical to reading_csvs_dataclass.py
fig1.show()
