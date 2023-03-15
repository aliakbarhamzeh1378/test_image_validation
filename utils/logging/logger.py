import logging
from fluent import handler

from utils.configs import config


class FluentdLogger:
    def __init__(self):
        self.fluent_handler = handler.FluentHandler(
            config.FLUENTD_TAG,
            host=config.FLUENTD_HOST,
            port=config.FLUENTD_PORT
        )
        self.logger = logging.getLogger('app')
        self.logger.setLevel(logging.INFO)
        self.logger.addHandler(self.fluent_handler)

    def log(self, message):
        print(message)
        self.logger.info(message)
