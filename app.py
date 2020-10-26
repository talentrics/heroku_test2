from flask import Flask,render_template,request,redirect
from dash.react import Dash

import pandas as pd
from threading import Thread
import simplejson as json
import requests
import datetime
import jinja2

from bokeh.embed import server_document, components 
from bokeh.layouts import column
from bokeh.models import ColumnDataSource, HoverTool, TextInput, CustomJS
from bokeh.io import curdoc
from bokeh.plotting import figure, output_file, show
from bokeh.server.server import Server
from bokeh.themes import Theme

app = Flask(__name__)

app.vars={}

@app.route('/')
def main():
	return redirect("/index")

@app.route('/index', methods=['GET'])
def index():
   return render_template('index.html')

@app.route('/about')
def about():
   return render_template('/about.html')

@app.route('/talentrics')
def talentrics():
   return render_template('/talentrics.html')

@app.route('/danielbmacdonald')
def danielbmacdonald():
   return render_template('/danielbmacdonald.html')

@app.route('/github')
def github():
   return render_template('/github.html')

@app.route('/guide')
def guide():
   return render_template('/guide.html')

@app.route('/tutorial')
def tutorial():
   return render_template('/tutorial.html')

@app.route('/graph', methods=['POST'])
def graph():

    return 'Hello Flask app'

app = dash.Dash(
    __name__,
    server=server,
    routes_pathname_prefix='/dash/'
)

app.layout = html.Div("My Dash app")

if __name__ == '__main__':
    app.run_server(debug=True)
   
   return render_template('graph.html', script=script, div=div)

if __name__ == '__main__':
   app.run(port=33507)