from flask import Flask, render_template
import csv

app = Flask(__name__)
@app.route("/home")
def index():
  with open('Untitled.csv') as csv_file:
    data = csv.reader(csv_file, delimiter=',')
    first_line = True
    places = []
    for row in data:
      if not first_line:
        places.append({
            
          "States": row[0],
          "Capital": row[1],
          "Language":row[2]

        })
      else:
        first_line = False
    
  return render_template("home.html", xlog=places, len_xlog=len(places))
@app.route('/')
def projectexpo():
    return render_template('home.html', name='Nick')