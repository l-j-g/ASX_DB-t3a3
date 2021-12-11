from flask import Blueprint, jsonify, request, render_template, redirect, url_for
from main import db
from models.tickers import Tickers
from schemas.ticker_schema import tickers_schema, ticker_schema

tickers = Blueprint('tickers', __name__)


@tickers.route("/tickers/", methods=["GET"])
def get_tickers():
    data = {
        "page_title": "Ticker Index",
        "tickers": tickers_schema.dump(Tickers.query.all())
    }
    return render_template("ticker_index.html", page_data=data)


@tickers.route("/tickers/", methods=["POST"])
def create_ticker():
    new_ticker = ticker_schema.load(request.form)
    db.session.add(new_ticker)
    db.session.commit()
    return jsonify(ticker_schema.dump(new_ticker))


@tickers.route("/tickers/<string:ticker_id>/", methods=["GET"])
def get_ticker(ticker):
    ticker = Tickers.query.get_or_404(ticker_id)
    return jsonify(ticker_schema.dump(ticker))


@tickers.route("/tickers/<string:ticker_id>/", methods=["PUT", "PATCH"])
def update_user(ticker_id):

    ticker = Tickers.query.filter_by(ticker_id=ticker)

    updated_fields = ticker_schema.dump(request.json)
    if updated_fields:
        ticker.update(updated_fields)

        db.session.commit()
    return jsonify(ticker_schema.dump(ticker.first()))


@tickers.route("/tickers/<int:id>/", methods=["DELETE"])
def delete_ticker(id):
    ticker = Tickers.query.get_or_404(id)
    db.session.delete(ticker)
    db.session.commit()
    return jsonify(ticker_schema.dump(ticker))

# Route to register a new user
@tickers.route("/tickers/register/", methods=["GET", "POST"])
def register():
#    data = {"page_title": "Register a New User"}

#    if request.method == "GET":
        # Render registration page
#        return render_template("register.html", page_data=data)

    if request.method == "POST":
        # Create a user, log them in, redirect to user index
        new_ticker = ticker_schema.load(request.form)
        db.session.add(new_ticker)
        db.session.commit()
        return redirect(url_for("tickers.get_tickers"))

'''
@users.route('/favicon.ico')
# Display tab icon
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),'favicon.ico', mimetype='image/vnd.microsoft.icon')
'''