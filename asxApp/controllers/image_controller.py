from flask import Blueprint, request, redirect, abort, url_for, send_from_directory, current_app
from pathlib import Path
from models.users import Users
import os
import boto3
from flask_login import login_user, logout_user, login_required, current_user

user_images = Blueprint('user_images', __name__)

@user_images.route("/users/<int:id>/image/", methods=["POST"])
@login_required
def update_image(id):
    print("here")
    user = Users.query.get_or_404(id)
    if "image" in request.files:
        image = request.files["image"]
        if Path(image.filename).suffix != ".png":
            return abort(400, description="Invalid file type")
        dir_path = os.path.dirname(os.path.realpath(__file__))
        image.save(f"asxApp/static/{user.image_filename}")
        '''
        # use boto3 package to upload file to s3 bucket
        bucket = boto3.resource("s3").Bucket(current_app.config["AWS_S3_BUCKET"])
        bucket.upload_fileobj(image, user.image_filename)
        '''
        return redirect(url_for('users.user_detail'))
    return abort(400, description="No image")


