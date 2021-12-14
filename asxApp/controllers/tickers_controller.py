from flask import Blueprint, jsonify, request, render_template, redirect, url_for
from main import db
from models.tickers import Tickers
from schemas.ticker_schema import tickers_schema, ticker_schema
import locale
from sqlalchemy import desc 
from flask_login import login_required, current_user

tickers = Blueprint('tickers', __name__)
locale.setlocale( locale.LC_ALL, '')


@tickers.route("/tickers/", methods=["GET"])
def get_tickers():
    data = {
        "page_title": "Ticker Index",
        "tickers": tickers_schema.dump(Tickers.query.all())
    }
    headers = {
        "ticker_id": "Tickers",
        "company_name": "Company Name",
        "sector": "Category",
        "marketcap": "Market Capitalization"
    }
    for ticker in data['tickers']:
       ticker['marketcap'] = locale.currency(ticker['marketcap'], grouping=True)
    return render_template("ticker_index.html", page_data=data, headers=headers)



@tickers.route("/tickers/orderway=<string:order>&groupby=<string:group>", methods=["GET"])
def sort_tickers(order, group):
    data = {
        "page_title": "Ticker Index",
        "tickers": tickers_schema.dump(Tickers.query.order_by(getattr(getattr(Tickers,group),order)()).all()),
        #(getattr(Tickers,group)).all())
        "group": group,
        "order": order
    }
    headers = {
        "ticker_id": "Tickers",
        "company_name": "Company Name",
        "sector": "Category",
        "marketcap": "Market Capitalization"
    }
    for ticker in data['tickers']:
       ticker['marketcap'] = locale.currency(ticker['marketcap'], grouping=True)
    return render_template("ticker_index.html", page_data=data, headers=headers)

@tickers.route("/tickers/<string:ticker_id>/add", methods=["POST"])
def add_ticker(ticker_id):
    ticker = Tickers.query.get_or_404(ticker_id)
    ticker.followers.append(current_user)
    db.session.commit()
    return redirect(request.referrer)
    