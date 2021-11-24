from market import app
from flask import render_template
from market.models import Item

@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"

@app.route("/t")
def hello_worldt():
    return render_template("home.html")

@app.route("/about/<user>")
def about_page(user):
    return f'<h1>about {user}</h1>'

@app.route("/market")
def market():
    items = Item.query.all()
    return render_template("market.html", items = items)