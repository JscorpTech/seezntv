from typing import Generic, TypeVar
from pydantic import BaseModel

# Generik tur uchun placeholder
T = TypeVar("T")


# Wrapper modeli
class ResponseWrapper(BaseModel, Generic[T]):
    status: bool = True
    data: T
