# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from openapi_server.models.chat import Chat


class BaseChatApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseChatApi.subclasses = BaseChatApi.subclasses + (cls,)
    async def chat(
        self,
    ) -> Chat:
        ...
