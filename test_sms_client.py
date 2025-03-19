import pytest
from req_and_res import HTTPRequest
from unittest.mock import patch, MagicMock
from send_sms import send_sms
from req_and_res import HTTPResponse


@pytest.fixture
def config():
    return {
        "sms_service": {
            "url": "http://127.0.0.1:4010",
            "username": "test_user",
            "password": "test_password"
        }
    }


def test_send_sms(config):
    sender = "+123456789"
    recipient = "+987654321"
    text = "Hello, World!"

    with patch("socket.socket") as mock_socket:

        mock_socket_instance = MagicMock()
        mock_socket.return_value.__enter__.return_value = mock_socket_instance


        mock_response = HTTPResponse(
            status_code=200,
            headers={},
            body='{"status": "success", "message_id": "123456"}'
        )
        mock_socket_instance.recv.return_value = mock_response.to_bytes()

        send_sms(config, sender, recipient, text)

        mock_socket.assert_called_once()

        mock_socket_instance.connect.assert_called_once_with(("127.0.0.1", 4010))

        mock_socket_instance.send.assert_called_once()

        mock_socket_instance.recv.assert_called_once()

def test_http_request_to_bytes():
    headers = {
        "Host": "example.com",
        "Content-Type": "application/json"
    }
    body = '{"key": "value"}'
    request = HTTPRequest(
        method="POST",
        url="/test",
        headers=headers,
        body=body
    )

    expected_bytes = (
        b"POST /test HTTP/1.1\r\n"
        b"Host: example.com\r\n"
        b"Content-Type: application/json\r\n"
        b"\r\n"
        b'{"key": "value"}'
    )

    assert request.to_bytes() == expected_bytes

def test_http_response_from_bytes():
    binary_data = (
        b"HTTP/1.1 200 OK\r\n"
        b"Content-Type: application/json\r\n"
        b"\r\n"
        b'{"status": "success"}'
    )

    response = HTTPResponse.from_bytes(binary_data)

    assert response.status_code == 200
    assert response.body == '{"status": "success"}'
