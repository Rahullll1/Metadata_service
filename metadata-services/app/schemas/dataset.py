from typing import List
from pydantic import BaseModel


class ColumnCreate(BaseModel):
    name: str
    data_type: str


class DatasetCreate(BaseModel):
    fqn: str
    source_type: str
    columns: List[ColumnCreate]


class ColumnResponse(BaseModel):
    name: str
    data_type: str

    class Config:
        from_attributes = True


class DatasetResponse(BaseModel):
    fqn: str
    source_type: str
    columns: List[ColumnResponse]

    class Config:
        from_attributes = True
