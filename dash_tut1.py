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
app.layout = html.Div("Dash Tutorial")

# to run the app with debuger
if __name__ == '__main__':
    app.run_server(debug=True)
    