import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import pandas as pd

def generate_formatted_dataframe(csv_filename, index_col="Index"):
  df = pd.read_csv(csv_filename, index_col=index_col)

  gen = pd.DataFrame()
  for index, row in df.iterrows():
    for column_name, value in row.iteritems():
      # Find if index or column_name is the Number Row
      data = {}
      data['Voltage'] = value
      if str(column_name).isdigit():
        data['Number Row'] = column_name
        data['Letter Row'] = index
        gen = gen.append(data, ignore_index=True)
      elif str(index).isdigit():
        data['Number Row'] = index
        data['Letter Row'] = column_name
        gen = gen.append(data, ignore_index=True)
      else:
        print("Error: No label that is a number")
      
  return gen

def generate_numpy(csv_filename, index_col="Index"):
  df = pd.read_csv(csv_filename, index_col=index_col)
  z = df.values
  sh_x, sh_y = z.shape
  x, y = np.linspace(0, sh_x, sh_x), np.linspace(0, sh_y, sh_y)
  return (x, y, z,)


def scatter_plot(df):
  fig = px.scatter_3d(df, x='Letter Row', y='Number Row', z='Voltage', opacity=0.7)
  return fig

def surface_plot(x, y, z, title="Voltage vs 2D Position"):
  fig = go.Figure(data=[go.Surface(z=z, x=x, y=y)])
  fig.update_layout(title=title, autosize=False,
                    margin=dict(l=65, r=50, b=65, t=90))
  return fig