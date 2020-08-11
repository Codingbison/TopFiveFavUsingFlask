from Sports_app import app
from flask import render_template

# home route
@app.route('/')
def home():
    item_dict = {1: "Sami Hyypia", 2: "Harry Kewell", 3:"Stephane Henchoz", 4:"Jerzy Dudek", 5:"Markus Babbel"}
    return render_template("home.html", item_dict=item_dict)

