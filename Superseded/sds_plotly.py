import pandas as pd
import plotly.graph_objects as go
import numpy as np
from mycolorpy import colorlist as mcp
print()

#Education


#Ocean Data Specialists
#Measured vs hindcasted? with map? 


#Design Criteria
#EVA?


#Installation Modelling
#subplots of pie chat + plume + yearly runs



#Installation Strategy
#start date sensitivity
colourmap_continuous = mcp.gen_color(cmap="viridis",n=10)

df_sds = pd.read_excel('/Users/jontypedersen/Library/CloudStorage/OneDrive-SharedLibraries-ODSL/Projects - Documents/RND - Research and Development/P-RND-ODSL-45136 website plots/SDS_plot.xlsx',
                       skiprows=10,
                       )


fig = go.Figure()
fig.add_trace(go.Scatter(x=df_sds['DateTime'], y=df_sds['P10'], fill='tozeroy'))

fig.show()

#Research & Development