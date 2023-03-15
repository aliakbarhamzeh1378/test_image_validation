from utils.logging import logger
from utils.configs import config
from minio import Minio
from minio.error import S3Error


class MinioClient:
    def __init__(self):
        self.minio_client = Minio(
            endpoint=config.MINIO_ENDPOINT,
            access_key=config.MINIO_ACCESS_KEY,
            secret_key=config.MINIO_SECRET_KEY,
            secure=False
        )
        self.logger = logger.FluentdLogger()

    def download_file(self, object_name, file_path):
        try:
            self.minio_client.fget_object(config.MINIO_BUCKET_NAME, object_name, file_path)
            self.logger.log(f"Downloaded file: {object_name}")
            return True
        except S3Error as e:
            self.logger.log(f"Error downloading file: {e}")
            return False
