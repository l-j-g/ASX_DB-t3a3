
from main import db
from flask import Blueprint

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
    from faker import Faker
    faker = Faker()

    for i in range(20):
        user = Users(faker.catch_phrase())
        db.session.add(user)

    db.session.commit()
    print("Tables seeded!")

@db_commands.cli.command("reset")
def reset_db():
    """ Drops, creates and seeds tables in one command."""
    db.drop_all()
    db.engine.execute("DROP TABLE IF EXISTS alembic_version;")
    db.create_all()
    from models.users import Users
    from faker import Faker
    faker = Faker()

    for i in range(20):
        user = Users(faker.catch_phrase())
        db.session.add(user)
    db.session.commit()
    print("Tables reset & seeded!")

@db_commands.cli.command("export")
def export_db():
    "Exports all data from database into a text document"
    # TODO : Write SQL command to dump all data to text
    pass
