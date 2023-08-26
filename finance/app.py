import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
import requests
import sqlite3


from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    user_id = session["user_id"]

    # Get user's stocks and shares
    stocks = db.execute(
        "SELECT symbol, SUM(shares) as total_shares FROM transactions WHERE user_id = :user_id GROUP BY symbol HAVING total_shares > 0",
        user_id=user_id,
    )

    # Get user's cash balance
    cash = db.execute("SELECT cash FROM users WHERE id = :user_id", user_id=user_id)[0][
        "cash"
    ]

    # Initialize variables for total values
    total_value = cash
    grand_total = cash

    # Iterate over stocks and add price and total value
    for stock in stocks:
        quote = lookup(stock["symbol"])
        stock["name"] = quote["name"]
        stock["price"] = quote["price"] * stock["total_shares"]
        stock["value"] = stock["price"]
        total_value += stock["value"]
        grand_total += stock["value"]

    return render_template(
        "index.html",
        stocks=stocks,
        cash=cash,
        total_value=total_value,
        grand_total=grand_total,
    )


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""

    if request.method == "POST":
        # Ensure symbol and shares were submitted
        symbol = request.form.get("symbol")
        shares = request.form.get("shares")

        if not symbol:
            return apology("must provide symbol", 400)
        if not shares:
            return apology("must provide shares", 400)
        if not shares.isdigit() or int(shares) <= 0:
            return apology("invalid number of shares", 400)

        # Look up stock quote
        quote_data = lookup(symbol)
        if quote_data is None:
            return apology("invalid symbol", 400)

        # Calculate total cost of the purchase
        price_per_share = quote_data["price"]
        total_cost = price_per_share * int(shares)

        # Query database for user's cash
        user_cash = db.execute(
            "SELECT cash FROM users WHERE id = ?", session["user_id"]
        )[0]["cash"]

        # Check if user can afford the purchase
        if total_cost > user_cash:
            return apology("can't afford", 403)

        # Update user's cash and add transaction to history
        db.execute(
            "UPDATE users SET cash = cash - ? WHERE id = ?",
            total_cost,
            session["user_id"],
        )
        db.execute(
            "INSERT INTO transactions (user_id, symbol, shares, price) VALUES (?, ?, ?, ?)",
            session["user_id"],
            symbol,
            int(shares),
            price_per_share,
        )

        # Redirect user to home page
        flash("Bought!")
        return redirect("/")

    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    user_id = session["user_id"]

    transactions = db.execute(
        "SELECT symbol, shares, price, timestamp FROM transactions WHERE user_id = ? ORDER BY timestamp DESC",
        user_id,
    )

    return render_template("history.html", transactions=transactions)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


# Define the quote route
@app.route("/quote", methods=["GET", "POST"])
def quote():
    if request.method == "POST":
        symbol = request.form.get("symbol")
        if symbol:
            quote_data = lookup(symbol)
            if quote_data:
                return render_template(
                    "quoted.html", symbol=symbol, latest_price=quote_data["price"]
                )
            else:
                error_message = "Failed to fetch stock quote. Please try again."
                return (
                    render_template("quote.html", error_message=error_message),
                    400,
                )  # Return 400 for Bad Request
        else:
            error_message = "Please enter a stock symbol."
            return (
                render_template("quote.html", error_message=error_message),
                400,
            )  # Return 400 for Bad Request
    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 400)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 400)

        # Ensure password confirmation was submitted
        elif not request.form.get("confirmation"):
            return apology("must confirm password", 400)

        # Ensure password and confirmation match
        elif request.form.get("password") != request.form.get("confirmation"):
            return apology("passwords must match", 400)

        # Check if username already exists
        existing_user = db.execute(
            "SELECT * FROM users WHERE username = :username",
            username=request.form.get("username"),
        )
        if existing_user:
            return apology("username already exists", 400)

        # Generate password hash
        password_hash = generate_password_hash(request.form.get("password"))

        # Insert user into the database
        result = db.execute(
            "INSERT INTO users (username, hash) VALUES (:username, :password_hash)",
            username=request.form.get("username"),
            password_hash=password_hash,
        )

        # Log the user in automatically after registration
        session["user_id"] = result

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("register.html")


def get_user_by_username(username):
    conn = sqlite3.connect("finance.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    user = cursor.fetchone()
    conn.close()
    return user


def get_user_portfolio(user_id):
    conn = sqlite3.connect("finance.db")
    cursor = conn.cursor()
    cursor.execute("SELECT symbol, shares FROM portfolio WHERE user_id = ?", (user_id,))
    portfolio = {symbol: shares for symbol, shares in cursor.fetchall()}
    conn.close()
    return portfolio


def update_user_cash(user_id, new_cash_balance):
    conn = sqlite3.connect("finance.db")
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE users SET cash = ? WHERE id = ?", (new_cash_balance, user_id)
    )
    conn.commit()
    conn.close()


def update_user_portfolio(user_id, symbol, new_shares):
    conn = sqlite3.connect("finance.db")
    cursor = conn.cursor()

    if new_shares <= 0:
        cursor.execute(
            "DELETE FROM portfolio WHERE user_id = ? AND symbol = ?", (user_id, symbol)
        )
    else:
        cursor.execute(
            "UPDATE portfolio SET shares = ? WHERE user_id = ? AND symbol = ?",
            (new_shares, user_id, symbol),
        )

    conn.commit()
    conn.close()


def add_transaction(user_id, symbol, shares, transaction_type, price):
    conn = sqlite3.connect("finance.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO transactions (user_id, symbol, shares, type, price) VALUES (?, ?, ?, ?, ?)",
        (user_id, symbol, shares, transaction_type, price),
    )
    conn.commit()
    conn.close()


# Routes


@app.route("/sell", methods=["GET", "POST"])
def sell():
    error_message = None

    if request.method == "POST":
        symbol = request.form.get("symbol")
        shares = int(request.form.get("shares"))

        user = get_user_by_username(session["username"])
        portfolio = get_user_portfolio(user["id"])

        if symbol in portfolio and portfolio[symbol] >= shares:
            stock_data = lookup(symbol)
            price = stock_data["price"]

            earnings = price * shares

            update_user_cash(user["id"], user["cash"] + earnings)
            update_user_portfolio(user["id"], symbol, portfolio[symbol] - shares)

            add_transaction(user["id"], symbol, shares, "sell", price)

            return redirect(url_for("index"))
        else:
            error_message = "Not enough shares to sell."

    return render_template("sell.html", error_message=error_message)


if __name__ == "__main__":
    app.run(debug=True)
