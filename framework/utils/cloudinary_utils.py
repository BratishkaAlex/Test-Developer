import cloudinary.uploader

from framework.utils.logger import info
from resources import cloudinary_config


def cloudinary_authorize():
    info("Save config to cloudinary")
    cloudinary.config(cloud_name=cloudinary_config.CLOUD_NAME, api_key=cloudinary_config.API_KEY,
                      api_secret=cloudinary_config.API_SECRET)


def cloudinary_upload_file(path_to_uploaded_file: str, public_id: str):
    info("Upload local file on cloudinary")
    cloudinary.uploader.upload(path_to_uploaded_file, public_id=public_id)


def get_link_to_download_from_cloudinary(public_id: str) -> str:
    info("Getting link to download file from cloudinary")
    return cloudinary.utils.cloudinary_url(public_id)[0]
