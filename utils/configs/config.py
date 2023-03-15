import os

MINIO_ENDPOINT = os.environ.get('MINIO_ENDPOINT', 'localhost:9000')
MINIO_ACCESS_KEY = os.environ.get('MINIO_ACCESS_KEY', 'minioadmin')
MINIO_SECRET_KEY = os.environ.get('MINIO_SECRET_KEY', 'minioadmin')
MINIO_BUCKET_NAME = os.environ.get('MINIO_BUCKET_NAME', 'bucket')

FLASK_PORT =  int(os.environ.get('FLASK_PORT', "8001"))
FLUENTD_HOST = 'fluentd-server'
FLUENTD_PORT = 24224
FLUENTD_TAG = 'app.log'
QUEUE_SIZE = int(os.environ.get('QUEUE_SIZE', '10'))
MAX_THREAD = int(os.environ.get('MAX_THREAD', '10'))
TEMP_DIR_PATH = os.environ.get('TEMP_DIR_PATH', 'temp')
