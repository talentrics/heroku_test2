from flask import Flask,render_template,request,redirect
import dash

import pandas as pd
from threading import Thread
import simplejson as json
import requests
import datetime
import jinja2

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

@app.route('/graph')
def graph():
   return render_template('/graph.html')

if __name__ == '__main__':
   app.run(port=33507)