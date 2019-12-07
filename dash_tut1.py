import dash
import dash_core_components as dcc
import dash_html_components as html

'''
Dash Tutorial - Sentdex - Simple App

The Dash application is simply speaking a Flask application exported to web
browser using React and JS
The layout of the application can be edited with .css files
'''

# to start and app
app = dash.Dash()

# to setup the layout
# app.layout = html.Div("Dash Tutorial")
# html div can store a list of html tags
app.layout = html.Div(children=[
    # each child is within new line = first is h1 header tag
    html.H1('Dash tutorials'),
    # the chart is invoked using the dcc elemnts - Graph
    dcc.Graph(id='example',
        # figure data, layout and other properties are stored below
        figure={
            'data' : [
                # explored different types of charts - line, point
                {'x':[1,2,3,4,5], 'y':[200, 400, 230, 300, 350],
                    'type':'line', 'name':'boats'},
                {'x':[1,2,3,4,5], 'y':[100, 230, 130, 150, 180],
                    'type':'line', 'name':'cars'},
                {'x':[3.5,5], 'y':[250,250],
                    # played a bit with customization of chart series
                    'mode':'markers', 'name':'points', 'marker': {
                        'size':12,
                        'symbol':'hexagon2'
                    }}
                ],
            'layout': {
                'title':'Example of simple line chart',
                # adjusted a bit layout - froze the yaxis with specific range
                'yaxis': {
                    'title': {
                        'text':'Units'
                    },
                    'range':[0, 500],
                    'fixedrange':True
                }
            }
        })])

# to run the app with debuger
if __name__ == '__main__':
    app.run_server(debug=True)

# dash application will be run on the computer it's on with port 8050