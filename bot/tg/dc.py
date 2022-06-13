from typing import Optional
from pydantic import BaseModel, Field


class MessageFrom(BaseModel):
    id: int
    first_name: str
    last_name: Optional[str]
    username: str


class Chat(BaseModel):
    id: int
    type: str
    first_name: Optional[str]
    last_name: Optional[str]
    username: Optional[str]
    title: Optional[str]


class Message(BaseModel):
    message_id: int
    from_: MessageFrom = Field(..., alias='from')
    chat: Chat
    text: Optional[str]

    class Config:
        allow_population_by_field_name = True


class UpdateObj(BaseModel):
    update_id: int
    message: Message


class GetUpdatesResponse(BaseModel):
    ok: bool
    result: list[UpdateObj]


class SendMessageResponse(BaseModel):
    ok: bool
    result: Message