from pydantic import BaseModel


class LineageCreate(BaseModel):
    upstream_fqn: str
    downstream_fqn: str
