from typing import Annotated, Optional, Literal, Union
from pydantic import BaseModel, Field

ID = Annotated[str, Field(pattern=r'[0123456789abcdef]{24}')]
