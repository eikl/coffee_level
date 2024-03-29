
from bokeh.themes import Theme
from bokeh.plotting import figure, show
import pandas as pd
from bokeh.sampledata import download
from bokeh.embed import components
from bokeh.io import curdoc
from bokeh.models import Range1d, LinearAxis
from bokeh.models import DatetimeTickFormatter, NumeralTickFormatter
import datetime as dt
import sql_queries

def plot():
    # Prepare some data

    df = sql_queries.get_level_data()
    df2 = sql_queries.get_atm_data()

    x = pd.to_datetime(df["date"])
    y = df["level"]
    y = y.rolling(window=10).median()
    y2 = df2["voc"]
    y22 = df2["rh"]
    x2 = df2["date"]
    # Create a new plot with a dark background
    p = figure(x_axis_label='Aika', 
               y_axis_label='VOC indeksi',
               x_axis_type = 'datetime',
               width=700,
               height=400,
               background_fill_color = '#2f3640',
               border_fill_color = '#2f3640',
               outline_line_color = '#2f3640',
               y_range = Range1d(0,500),
               active_drag = None,
               active_scroll = None,
               active_tap = None
               )
    
    print(p.xaxis[0].formatter)
    # Add a line renderer with legend and line thickness
    p.xaxis[0].formatter = DatetimeTickFormatter(minsec='%H:%M:%S',hourmin='%H:%M:%S',seconds='%H:%M:%S',
                                                 minutes = '%H:%M:%S')

    
    p.line(x2, y2, line_width=2, line_color="#f5f6fa",legend_label="VOC indeksi")

    p.extra_y_ranges['rh'] = Range1d(0,100)
    p.line(x2, y22, color="orange", y_range_name="rh",legend_label="RH")

    ax2 = LinearAxis(y_range_name="rh", axis_label="RH (%)")
    ax2.axis_label_text_color ="navy"
    p.add_layout(ax2, 'right')


    p.yaxis[0].formatter = NumeralTickFormatter(format='0.00')
    p.toolbar_location = None
    p.toolbar.logo = None
    p.xaxis.major_label_text_color='white'
    p.yaxis.major_label_text_color='white'
    p.xgrid.visible = False
    p.ygrid.visible = True
    p.axis.major_label_text_color= "white"
    p.xaxis.axis_label_text_color ="white"
    p.yaxis.axis_label_text_color="white"
    p.xaxis.axis_line_color = "white"
    p.yaxis.axis_line_color= "white"

    p.legend.location = "top_left"
    p.legend.label_text_font = "times"
    p.legend.label_text_font_style = "italic"
    p.legend.label_text_color = "white"

    p.legend.border_line_width = 3
    p.legend.border_line_color = None
    p.legend.border_line_alpha = 0.8
    p.legend.background_fill_color = "navy"
    p.legend.background_fill_alpha = 0
    # Generate the components of the plot
    script, div = components(p)
    return script,div
