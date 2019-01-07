from plotly.offline import iplot, init_notebook_mode
import plotly.graph_objs as go
import plotly.io as pio

import os
import numpy as np

from .models import *

import csv
from django.shortcuts import get_list_or_404, get_object_or_404

class Survey:
    self.Survey_id = None
    self.title = None
    self.x = None
    self.y = None
    self.z = None

    def __init__(self, survey_id):
        init_notebook_mode(connected=True)

        if not os.path.exists('images'):
            os.mkdir('images')

    def to_csv():
        pass

    def three_dim():
        fig = go.Figure()
        layout = go.Layout(title=title)
        data = go.Data()
        pass

class Profile:
    self.Profile_id = None
    self.tile = None
    self.x = None
    self.y = None

    def __init__(self, profile_id):
        init_notebook_mode(connected=True)

        if not os.path.exists('images'):
            os.mkdir('images')
        
        if not os.path.exists('csv'):
            os.mkdir('csv')

        self.Profile_id = profile_id

    def to_csv(title, true_distance, true_elevation):
        self.title = title
        self.x = list(true_distance)
        self.y = list(true_elevation)

        with open("csv/" + self.title, newline='') as csvfile:
            write = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
            for x, y in map(None, self.x, self.y):
                if x == None:
                    x = 0
                if y == None:
                    y = 0
                write.writerow([x, y])


    def two_dim():
        layout = go.Layout(title=title, xaxis={'title':'Elevation'}, yaxis={'title':'Distance'})

        trace0 = go.Scatter(x=np.asarray(self.x), y=np.asarray(self.y), fill='tonexty', mode='lines', name='lines')

        fig = go.Figure(data=[trace0], layout=layout)
        pio.write_image(fig, "images/" + title)