from pydantic import BaseModel, IPvAnyAddress, HttpUrl


class HTTPServerTestConfig(BaseModel):
    port: int
    address: IPvAnyAddress


class HTTPClientTestConfig(BaseModel):
    url: HttpUrl
    timeout: float = 120.0
