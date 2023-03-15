import uuid
from typing import Union

from flask import Flask
from flasgger import Swagger

from utils.configs import config
from utils.requests.request_processor import RequestProcessor
from pydantic import BaseModel

# Create a Flask application
app = Flask(__name__)
swagger = Swagger(app)

# Create a RequestProcessor object
request_processor = RequestProcessor()


# Define a request endpoint that adds a token to the request queue
@app.get("/request/")
def request_files():
    """
    Add a token to the request queue.

    ---
    responses:
      200:
        description: A message indicating that the request has been added to the queue.
    """
    # Generate a new token for this request

    # Add the token to the request queue
    token = "10"
    request_processor.add_request(token)

    # Return a message indicating that the request has been added to the queue
    return f"Request added to queue: {token}"


if __name__ == '__main__':
    app.run(port=config.FLASK_PORT)
