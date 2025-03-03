from typing import Annotated
from pydantic import BaseModel, Field

API_KEY = Annotated[
    str, Field(min_length=64, max_length=80, pattern=r'^(dev|personal)\-[0-9a-f]{64}$')
]
OPTIONAL_API_KEY = Annotated[API_KEY | None, Field(default=None)]
ID = Annotated[int, Field(ge=1, strict=True)]


class APIKey(BaseModel):
    model_config = {'extra': 'ignore'}

    key: API_KEY
