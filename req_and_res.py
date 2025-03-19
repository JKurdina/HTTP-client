from typing import Dict

class HTTPRequest:
    def __init__(self, method: str, url: str, headers: Dict[str, str], body: str) -> None:
        self.method = method
        self.url = url
        self.headers = headers
        self.body = body

    def to_bytes(self) -> bytes:
        headers_str = "\r\n".join(f"{k}: {v}" for k, v in self.headers.items())
        request_line = f"{self.method} {self.url} HTTP/1.1\r\n"
        return f"{request_line}{headers_str}\r\n\r\n{self.body}".encode()

    @classmethod
    def from_bytes(cls, binary_data: bytes) -> "HTTPRequest":
        data = binary_data.decode()
        headers_end = data.find("\r\n\r\n")
        # headers = data[:headers_end]
        body = data[headers_end + 4:]
        return cls(method="GET", url="/", headers={}, body=body)


class HTTPResponse:
    def __init__(self, status_code: int, headers: Dict[str, str], body: str) -> None:
        self.status_code = status_code
        self.headers = headers
        self.body = body

    def to_bytes(self) -> bytes:
        headers_str = "\r\n".join(f"{k}: {v}" for k, v in self.headers.items())
        status_line = f"HTTP/1.1 {self.status_code}\r\n"
        return f"{status_line}{headers_str}\r\n\r\n{self.body}".encode()

    @classmethod
    def from_bytes(cls, binary_data: bytes) -> "HTTPResponse":
        data = binary_data.decode()
        status_line = data.split("\r\n")[0]
        status_code = int(status_line.split(" ")[1])
        headers_end = data.find("\r\n\r\n")
        # headers = data[:headers_end]
        body = data[headers_end + 4:]
        return cls(status_code=status_code, headers={}, body=body)