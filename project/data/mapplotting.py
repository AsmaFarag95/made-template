import plotly.express as px
import plotly.express as px2
import pandas as pd
import sqlite3

#read sqlite results into pandas DF
con = sqlite3.connect("wroclaw_nuremberg_public_transport.sqlite")
wroclawDataFrame = pd.read_sql_query("SELECT * from wroclaw_data", con)
nurembergDataFrame = pd.read_sql_query("SELECT * from nuremberg_data", con)
con.close()

color_scale = [(0, 'purple'), (1,'green')]
fig = px.scatter_mapbox(nurembergDataFrame, 
                        lat="latitude", 
                        lon="longitude", 
                        hover_name="Betriebszweig", 
                        hover_data=["Betriebszweig"],
                        color="Betriebszweig",
                        color_continuous_scale=color_scale,
                        
                        zoom=9, 
                        height=500,
                        width=500)
fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()
color_scale = [(0, 'purple'), (1,'green')]
fig2 = px2.scatter_mapbox(wroclawDataFrame.head(1000), 
                        lat="latitude", 
                        lon="longitude", 
                        hover_name="Betriebszweig", 
                        hover_data=["Betriebszweig"],
                        color="Betriebszweig",
                        color_continuous_scale=color_scale,
                        zoom=9, 
                        height=500,
                        width=500)
fig2.update_layout(mapbox_style="open-street-map")
fig2.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig2.show()