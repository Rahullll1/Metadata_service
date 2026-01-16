from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base


class Dataset(Base):
    __tablename__ = "datasets"

    id = Column(Integer, primary_key=True, index=True)

    # Fully Qualified Name: connection.db.schema.table
    fqn = Column(String(255), unique=True, nullable=False, index=True)

    # Source system type (MySQL / PostgreSQL / MSSQL)
    source_type = Column(String(50), nullable=False)

    # One-to-many relationship with columns
    columns = relationship(
        "ColumnMeta",
        back_populates="dataset",
        cascade="all, delete-orphan",
    )
