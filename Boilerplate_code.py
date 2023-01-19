#Importing flask module in the project
from flask import Flask, render_template

#Create an object of the Flask class
app = Flask(__name__)

#The route() function of the Flask class 
@app.route("/anything")

#‘/’ URL is bound with first_flask function.
def first_webpage():

    name = "Flask"
    return render_template("anything.html", index_variable = name)

#run the application on local server
app.run(debug=True)
