
from main import db
import csv
from flask import Blueprint
import os
from dotenv import load_dotenv

db_commands = Blueprint("db-custom", __name__)


@db_commands.cli.command("create")
def create_db():
    """ Creates all necessary tables"""
    db.create_all()
    print("Tables Created!")


@db_commands.cli.command("drop")
def drop_db():
    """ Deletes all data in tables"""
    db.drop_all()
    db.engine.execute("DROP TABLE IF EXISTS alembic_version;")
    print("Tables deleted")


@db_commands.cli.command("seed")
def seed_db():
    """ Seeds the database with user data"""
    from models.users import Users
    from models.tickers import Tickers, Info
    from faker import Faker
    faker = Faker()

#    for i in range(20):
#        user = Users(faker.catch_phrase())
#        db.session.add(user)
    with open('./asxApp/data/ASX_Listed_Companies_04-11-2021_04-29-57_AEDT.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = next(reader)
        for i in range(3):
            csv_line = next(reader)
            ticker_id = csv_line[0]
            ticker = Tickers(csv_line[0],csv_line[1],csv_line[3],csv_line[4])
            db.session.add(ticker)

            with open(f'./asxApp/data/{ticker_id}.AX/{ticker_id}.AX_info.csv') as info:
                reader = csv.reader(info, delimiter=',')
                header = next(reader)
                titles = []
                values = []
                for line in reader:
                    titles.append(line[0])
                    values.append(line[1])
                info = Info(titles,values)
    
    db.session.commit()
    print("Tables seeded!")

@db_commands.cli.command("reset")
def reset_db():
    """ Drops, creates and seeds tables in one command."""
    db.drop_all()
    db.engine.execute("DROP TABLE IF EXISTS alembic_version;")
    db.create_all()

    from models.tickers import Tickers
    print("Tables reset & seeded!")
    with open('./asxApp/data/ASX_Listed_Companies_04-11-2021_04-29-57_AEDT.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = next(reader)
        for i in range(3):
            csv_line = next(reader)
            ticker_id = csv_line[0]
            ticker = Tickers(csv_line[0],csv_line[1],csv_line[3],csv_line[4])
            db.session.add(ticker)
    # cash_flow = Cashflow.cashflow()
    db.session.commit()
    print("Tables seeded!")

@db_commands.cli.command("export")
def export_db():
    "Exports all data from the database into a text document"
    load_dotenv()
    user = os.environ.get('DB_USER') 
    password = os.environ.get('DB_PASS') 
    database = os.environ.get('DB_NAME') 
    domain = os.environ.get('DB_DOMAIN')
    os.system(f"pg_dump --dbname=postgresql://{user}:{password}@{domain}/{database} -f dump")  
