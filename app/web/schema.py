from pydantic import BaseModel


class AddCity(BaseModel):
    added: list[str]
    exist: list[str]
