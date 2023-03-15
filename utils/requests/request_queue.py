from utils.configs import config
from utils.logging import logger
from queue import Queue

from utils.requests.request import Request


class RequestQueue:
    def __init__(self):
        self.queue = Queue(config.QUEUE_SIZE)
        self.logger = logger.FluentdLogger()

    def add_request(self, token):
        request = Request(token)
        self.queue.put(request)
        self.logger.log(f"Added request with token: {request.token}")

    def get_request(self):
        request = self.queue.get()
        self.logger.log(f"Retrieved request with token: {request.token}")
        return request

    def mark_request_as_processed(self):
        self.queue.task_done()

    def get_queue_size(self):
        size = self.queue.qsize()
        self.logger.log(f"Request queue size: {size}")
        return size
