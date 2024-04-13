from flask import Flask, render_template, request, url_for
from flask_pymongo import PyMongo
from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, SelectField, DateField
import requests
from decimal import Decimal

app = Flask(__name__)
app.config["SECRET_KEY"] = "include_a_strong_secret_key"
app.config[
    "MONGO_URI"] = "mongodb+srv://jsuar264:3XyO078R2MsoLiSk@cluster0.aeonij7.mongodb.net/db?retryWrites=true&w=majority&appName=Cluster0"
mongo = PyMongo(app)


class Expenses(FlaskForm):
    description = StringField('Description')
    category = SelectField('Category', choices=[('Rent', 'Rent'), ('Electricity', 'Electricity'), ('Water', 'Water'),
                                                ('Internet', 'Internet'), ('Insurance', 'Insurance'),
                                                ('Restaurants', 'Restaurants'), ('Groceries', 'Groceries'),
                                                ('Gas', 'Gas'), ('College', 'College'), ('Party', 'Party'),
                                                ('Mortgage', 'Mortgage'), ])
    cost = DecimalField('Cost')
    currency = SelectField('Currency', choices=[
        ('USD', 'US Dollar'), ('EUR', 'Euro'), ('BRL', 'Brazilian Real'),
        ('COP', 'Colombian Peso'), ('MXN', 'Mexican Peso')
    ])
    date = DateField('Date', format='%Y-%m-%d')


def get_total_expenses(category):
    expenses = mongo.db.expenses.find({'category': category})
    total = sum(float(expense['cost']) for expense in expenses)
    return total


def currency_converter(cost, currency):
    api_key = "54d9ded593788f334337e926ac758752"
    url = f"http://api.currencylayer.com/live?access_key={api_key}&currencies={currency}&source=USD&format=1"
    data = requests.get(url).json()

    if currency == "USD":
        return cost

    quotes_key = f"USD{currency}"
    usd_rate = Decimal(str(data.get('quotes', {}).get(quotes_key, 0)))
    if usd_rate == 0:
        print(f"Conversion rate for {currency} not found or API call failed.")
        return None

    converted_cost = cost / usd_rate
    return round(converted_cost, 2)


@app.route('/')
def index():
    my_expenses = mongo.db.expenses.find()
    total_cost = 0
    for i in my_expenses:
        total_cost += float(i["cost"])
    categories = mongo.db.expenses.distinct("category")
    expensesByCategory = [(category, get_total_expenses(category)) for category in categories]
    print("Expenses by category:", expensesByCategory)  # Debug print
    return render_template("index.html", expenses=total_cost, expensesByCategory=expensesByCategory)


@app.route('/addExpenses', methods=["GET", "POST"])
def addExpenses():
    expenseForm = Expenses()
    if request.method == "POST" and expenseForm.validate_on_submit():
        converted_cost = currency_converter(
            expenseForm.cost.data,
            expenseForm.currency.data
        )
        mongo.db.expenses.insert_one({
            'description': expenseForm.description.data,
            'category': expenseForm.category.data,
            'cost': str(converted_cost),
            'currency': 'USD',
            'date': expenseForm.date.data.strftime('%Y-%m-%d')
        })
        return render_template("expenseAdded.html")
    return render_template("addExpenses.html", form=expenseForm)


app.run()
