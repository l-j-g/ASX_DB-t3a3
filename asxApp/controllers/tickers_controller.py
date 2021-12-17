from flask import Blueprint, jsonify, request, render_template, redirect, url_for
from schemas.user_schema import UserSchema
from main import db
from models.tickers import Tickers
from models.users import Users
from schemas.ticker_schema import tickers_schema, ticker_schema
from schemas.user_schema import users_schema, user_schema
import locale
from sqlalchemy import desc, func
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


# "user": UserSchema.dump(current_user)

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

@tickers.route("/tickers/<string:ticker_id>/info", methods=["GET"])
def get_info(ticker_id):
    ticker = Tickers.query.get_or_404(ticker_id)
#    followers = db.session.query(func.count(Tickers.followers).filter(Tickers.ticker_id == ticker_id))
#    print(followers)
#    followers = ticker_schema.dump(followers)
#    print(followers)
#    print(type(Tickers.followers))
    data = {
    "page_title": "Ticker Info",
    "ticker": ticker_schema.dump(ticker),
    "followers": db.session.query(
        Tickers.followers).filter(
            Tickers.ticker_id == ticker_id
            ).count()
    }
    
#    print(data['ticker'])


    return render_template("ticker_info.html", page_data=data)


@tickers.route("/tickers/<string:ticker_id>/add", methods=["GET"])
@login_required
def add_ticker(ticker_id):
    ticker = Tickers.query.get_or_404(ticker_id)
    ticker.followers.append(current_user)
    db.session.commit()
    return redirect(request.referrer)
    
@tickers.route("/tickers/<string:ticker_id>/remove", methods=["GET"])
@login_required
def remove_ticker(ticker_id):
    ticker = Tickers.query.get_or_404(ticker_id)
    ticker.followers.remove(current_user)
    db.session.commit()
    return redirect(request.referrer)