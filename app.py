from flask import Flask, render_template

app = Flask(__name__)

SALES = [{
    'id':1,
    'name': 'Sony',
    'price': '1000',
    'quantity': 10,
    'totalprice': '10000'
},
{
    'id':2,
    'name': 'Sony',
    'price': '1000',
    'quantity': 5,
    'totalprice': '5000'
},
{
    'id':3,
    'name': 'Philips',
    'price': '800',
    'quantity': 6,
    'totalprice': '4800'
},
{
    'id':4,
    'name': 'Apple',
    'price': '1400',
    'quantity': 2,
    'totalprice': '2800'
}]


@app.route("/")
def hello():
    return render_template("home.html", sales=SALES)

if __name__ == "__main__":
        app.run(host = "0.0.0.0", debug=True)