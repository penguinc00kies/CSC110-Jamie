"""test file for using plotly's bubble maps"""

import plotly.express as px

df = px.data.gapminder().query("year==2007")
fig = px.scatter_geo(df, locations="iso_alpha", color="continent",
                     hover_name="country", size="pop",
                     projection="eckert6")
fig.show()
