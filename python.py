from flask import Flask, request, Markup, render_template, flash
import os
import json

app = Flask(__name__) 


@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/page1")
def page1():
    return render_template('page1.html')

@app.route("/page2")
def page2():
    return render_template('page2.html')

@app.route("/page3")
def page3():
    return render_template('page3.html')

@app.route("/year")
def year():
    listOfYears = []
    with open('Drugs.json') as Drugs_data:
        years = json.load(Drugs_data)
    print(years)

    

  
  
if __name__=="__main__":
    app.run(debug=False)
