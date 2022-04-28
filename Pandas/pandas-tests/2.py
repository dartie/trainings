# import plotly
# import plotly.graph_objs as go
# import pandas as pd
#
# df = pd.read_csv('https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-andamento-nazionale/dpc-covid19-ita-andamento-nazionale.csv')
# # Create a trace
# data = [go.Scatter(
#     x=df['data'],
#     y=df['totale_positivi'],
# )]
# layout = go.Layout(
#         xaxis=dict(
#             title='Data',
#         ),
#         yaxis=dict(
#             title='Totale positivi',
#         )
#     )
# fig = go.Figure(data=data, layout=layout)
#
# plotly.offline.plot(fig,filename='positives.html')

# import plotly
# import plotly.graph_objs as go
# labels = ['home', 'transports', 'food']
# sizes = ['500', '300', '100']
#
# # Data to plot with plotly
# trace = go.Pie(labels=labels, values=sizes)
#
# div_tag = plotly.offline.plot([trace], include_plotlyjs=False,  output_type='div')
# html_content = plotly.offline.plot([trace], include_plotlyjs=True)

import pandas as pd
import plotly
import plotly.graph_objs as go

df = pd.DataFrame({
    'labels': ['home', 'transports', 'food'],
    'sizes': ['500', '300', '100']
})


# Data to plot with plotly
trace = go.Pie(labels=df["labels"], values=df["sizes"])

#div_tag = plotly.offline.plot([trace], include_plotlyjs=False,  output_type='div')
html_content = plotly.offline.plot([trace], include_plotlyjs=True, filename='test.html', auto_open=False)
print()