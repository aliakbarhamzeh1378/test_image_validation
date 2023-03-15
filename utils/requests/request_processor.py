from utils.logging import logger

import threading
from utils.configs import config
from deepface import DeepFace

from utils.minio_handler.minio_client import MinioClient
from utils.requests.request import Request
from utils.requests.request_queue import RequestQueue


class RequestProcessor:
    def __init__(self):
        self.request_queue = RequestQueue()
        self.logger = logger.FluentdLogger()
        self.minio_client = MinioClient()
        self.processing_threads = []
        for i in range(0, config.MAX_THREAD):
            self.processing_threads.append(threading.Thread(target=self.process_requests))
        for i in self.processing_threads:
            i.start()

    def add_request(self, token):
        request = Request(token)
        self.request_queue.add_request(request)
        self.logger.log(f"Add request with token: {request.token} to queue")

    def process_requests(self):
        while True:
            if self.request_queue.get_queue_size() == 0:
                continue

            request = self.request_queue.get_request()
            document_minio_path = request.get_document_minio_path()
            document_local_path = request.get_document_local_path()
            selfie_minio_path = request.get_selfie_minio_path()
            selfie_local_path = request.get_selfie_local_path()
            print(document_minio_path)
            print(document_local_path)
            print(selfie_minio_path)
            print(selfie_local_path)

            try:
                # Download the document image
                if not self.minio_client.download_file(document_minio_path, document_local_path):
                    self.request_queue.mark_request_as_processed()
                    continue
                self.logger.log(f"Downloaded file: {document_local_path}")

                # Download the selfie image
                if not self.minio_client.download_file(selfie_minio_path, selfie_local_path):
                    self.request_queue.mark_request_as_processed()
                    continue
                self.logger.log(f"Downloaded file: {selfie_local_path}")

                result = DeepFace.verify(img1_path=selfie_local_path, img2_path=document_local_path)
                self.logger.log(f"result files : {selfie_minio_path} and {document_minio_path} is {result}")
                # Process the downloaded files as needed (e.g., perform facial recognition)
                # ...

                # Indicate that the request has been processed
                self.request_queue.mark_request_as_processed()
                self.logger.log(f"Done :  {selfie_local_path}")

            except Exception as e:
                self.logger.log(f"Error processing request: {e}")
                self.request_queue.mark_request_as_processed()
