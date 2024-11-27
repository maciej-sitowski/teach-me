from typing import Generic, TypeVar, List
from pydantic.generics import GenericModel
from fastapi import Query


T = TypeVar("T")

class PaginatedResponse(GenericModel, Generic[T]):
    items: List[T]
    total: int
    limit: int
    offset: int

def get_pagination_params(
    limit: int = Query(10, ge=1),  # Default: 10 items per page
    offset: int = Query(0, ge=0),  # Default: Start from the first item
):
    return limit, offset