from plotly.offline import iplot, init_notebook_mode
import plotly.graph_objs as go
import plotly.io as pio

import os
import numpy as np

init_notebook_mode(connected=True)

if not os.path.exists('images'):
    os.mkdir('images')

class plot:

    def two_dim(title, x, y)
        fig = go.Figure();
        layout = go.Layout(title=title, xaxis={'title':'Elevation'}, yaxis={'title':'Distance'})
        data = go.Data()
        pio.write_image(fig, title);