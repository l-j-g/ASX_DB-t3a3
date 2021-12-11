from flask import Blueprint, request, redirect, abort, url_for, send_from_directory, current_app
from pathlib import Path
from models.users import Users
import os
import boto3

user_images = Blueprint('user_images', __name__)

@user_images.route("/users/<int:id>/image/", methods=["POST"])
def update_image(id):
    user = Users.query.get_or_404(id)
    if "image" in request.files:
        image = request.files["image"]
        if Path(image.filename).suffix != ".png":
            return abort(400, description="Invalid file type")

        # use boto3 package to upload file to s3 bucket
        bucket = boto3.resource("s3").Bucket(current_app.config["AWS_S3_BUCKET"])
        bucket.upload_fileobj(image, user.image_filename)

        return redirect(url_for("users.get_user", id=id))
    return abort(400, description="No image")


