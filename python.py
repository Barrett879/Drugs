from flask import Flask, request, Markup, render_template, flash
import os
import json

app = Flask(__name__) 

@app.route('/')
def home():
    return render_template('home.html', options=get_state_options())

@app.route('/funFact')

  
  
if __name__=='__main__':
    app.run(debug=True)
