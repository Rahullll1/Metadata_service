from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base


class ColumnMeta(Base):
    __tablename__ = "columns"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(100), nullable=False, index=True)
    data_type = Column(String(50), nullable=False)

    dataset_id = Column(Integer, ForeignKey("datasets.id"), nullable=False)

    dataset = relationship("Dataset", back_populates="columns")
