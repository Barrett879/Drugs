from flask import Flask, request, Markup, render_template, flash
import os
import json

app = Flask(__name__) 


@app.route("/")
def home():
    return render_template('home.html')

@app.route("/page1")
def page1():
    return render_template('page1.html', options = year())

@app.route("/page2")
def page2():
    return render_template('page2.html', options = year())

@app.route("/page3")
def page3():
    return render_template('page3.html', options = year())

def year():
    listOfYears = []
    with open('Drugs.json') as Drugs_data:
        years = json.load(Drugs_data)
    for year in years:
        if year["State"] == "California":
            listOfYears.append(year["Year"])
    print(listOfYears)
    options = ""
    for LOY in listOfYears:
        options += Markup("<option value=\"" + str(LOY) + "\">" + str(LOY) + "</option>")
    return options

@app.route("/year1")
def year1():
    YEAR = request.args.get('year')
    tob = []
    with open('Drugs.json') as Drugs_data:
        Totals = json.load(Drugs_data)
    for T in Totals:
        if T["State"] == "California" and T["Year"] == int(YEAR):
            tob.append(T["Totals"]["Tobacco"]["Cigarette Past Month"]["12-17"])
    options = ""
    for To in tob:
        options += Markup("<option value=\"" + str(To) + "\">" + str(To) + "</option>")
    return options
    
@app.route(

    

  
  
if __name__=="__main__":
    app.run(debug=False)
