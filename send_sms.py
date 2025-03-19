import base64
import socket
import logging
from urllib.parse import urlparse
from req_and_res import HTTPRequest, HTTPResponse

logger = logging.getLogger(__name__)


def send_sms(config, sender, recipient, text):

    parsed_url = urlparse(config["sms_service"]["url"])
    host = parsed_url.hostname
    port = parsed_url.port

    body = f'{{"sender": "{sender}", "recipient": "{recipient}", "message": "{text}"}}'
    logger.info(f"Тело запроса: {body}")

    username = config["sms_service"]["username"]
    password = config["sms_service"]["password"]

    credentials = f"{username}:{password}"
    encoded_credentials = base64.b64encode(credentials.encode()).decode()

    headers = {
        "Host": host,
        "Content-Type": "application/json",
        "Content-Length": str(len(body)),
        "Authorization": f"Basic {encoded_credentials}"
    }

    request = HTTPRequest(
        method="POST",
        url="/send_sms",
        headers=headers,
        body=body
    )

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.send(request.to_bytes())

        response_data = s.recv(4096)
        response = HTTPResponse.from_bytes(response_data)

        logger.info(f"Код статуса: {response.status_code}")
        logger.info(f"Тело ответа: {response.body}")

        print(f"Status Code: {response.status_code}")
        print(f"Response Body: {response.body}")