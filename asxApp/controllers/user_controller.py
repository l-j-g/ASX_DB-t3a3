from flask import Blueprint, jsonify, request, render_template, redirect, url_for, abort, flash, current_app
from main import db, lm
from models.users import Users
from schemas.user_schema import users_schema, user_schema, user_update_schema, UserSchema
from flask_login import login_user, logout_user, login_required, current_user
from marshmallow import ValidationError
import boto3
from models.tickers import Tickers

@lm.user_loader
def load_user(username):
    return Users.query.get(username)


@lm.unauthorized_handler
def unauthorized():
    return redirect('/users/login')


users = Blueprint('users', __name__)


# Route to list index of all users
@users.route("/users/", methods=["GET"])
def get_users():
    data = {
        "page_title": "User Index",
        "users": users_schema.dump(Users.query.all())
    }
    return render_template("user_index.html", page_data=data)


# Route to register a new user
@users.route("/users/register/", methods=["GET", "POST"])
def register():
    data = {"page_title": "Register a New User"}

    if request.method == "GET":
        # Render registration page
        return render_template("register.html", page_data=data)

    if request.method == "POST":
        # Create a user, log them in, redirect to user index
        #try:
        new_user = user_schema.load(request.form)
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        return redirect(url_for("users.get_users"))   
        #   except ValidationError as err:
        #    abort(422, {err})

@users.route("/users/login/", methods=["GET", "POST"])
def log_in():
    data = {"page_title": "Log in as an Existing User"}

    if request.method == "GET":
        return render_template("login.html", page_data=data)

    user = Users.query.filter_by(username=request.form["username"]).first()
    if user and user.check_password(password=request.form["password"]):
        login_user(user)
        return redirect(url_for('users.user_detail'))

    abort(401, "Login unsuccessful. Incorrect Credentials.")


# Route to log out
@users.route("/users/profile/logout", methods=["GET"])
@login_required
def log_out():
    logout_user()
    return redirect('/home')


@users.route("/users/profile/", methods=["GET", "POST"])
# This route is restriced to users that are logged in.
@login_required
def user_detail():

    if request.method == "GET":
      
        # client object communicates with our bucket
        user = Users.query.get_or_404(current_user.id)
        s3_client = boto3.client('s3')    
        # get s3 bucket name from config
        bucket_name = current_app.config["AWS_S3_BUCKET"]
        # pre-signed prevents public from being able to access files 
        image_url = s3_client.generate_presigned_url(
            'get_object',
            Params={
                'Bucket': bucket_name,
                'Key': user.image_filename
                },
            ExpiresIn=160
            ) 
        data = {
            "page_title": "Account Details",
            "user": user_schema.dump(user),
            "image": image_url
        }
        return render_template("profile.html", page_data=data)

    if request.method == "POST":
        user = Users.query.filter_by(id=current_user.id)
        updated_fields = user_schema.dump(request.form)
        # user_update_schema.validate() - to check for errors, validation checks are 
        # only used on load() by default.
        # user_update_schema has partial = True set, because we are not updating password.
        errors = user_update_schema.validate(updated_fields)

        if errors:
            raise ValidationError(message=errors)

        user.update(updated_fields)
        db.session.commit()
        return redirect(url_for("users.get_users"))



@users.route("/users/<int:id>/", methods=["GET"])
def get_user(id):
    # get this users data from the database
    user = Users.query.get_or_404(id)
    # client object communicates with our bucket
    s3_client = boto3.client('s3')    
    # get s3 bucket name from config
    bucket_name = current_app.config["AWS_S3_BUCKET"]
    # pre-signed prevents public from being able to access files 
    image_url = s3_client.generate_presigned_url(
        'get_object',
        Params={
            'Bucket': bucket_name,
            'Key': user.image_filename
        },
        ExpiresIn=160
    )
    data = {
        "page_title": "User Detail",
        "user": user_schema.dump(user),
        "image": image_url
    }
    return render_template("user_detail.html", page_data=data)

@users.route("/users/<int:id>/delete", methods=["POST"])
@login_required
def delete_user(id):
    if not current_user.id == id:
        flash("You can't do that, this isn't your profile.")
        return redirect(request.referrer)
    user = Users.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for("users.get_users"))
