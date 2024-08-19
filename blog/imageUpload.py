import boto3
from django.conf import settings

class UploadImageToS3Mixin:
    def upload_image_to_s3(image, folder='images'):
        s3 = boto3.client(
            's3',
            
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
            region_name=settings.AWS_S3_REGION_NAME
        )
        file_name = "f{folder}/{image.name}"
        s3.upload_fileobj(image, settings.AWS_STORAGE_BUCKET_NAME, file_name, ExtraArgs={'ContentType': image.content_type})

        image_url = f"https://{settings.AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com/{file_name}"
        return image_url