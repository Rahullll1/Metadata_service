from sqlalchemy import Column, Integer, ForeignKey, UniqueConstraint

from app.database import Base


class Lineage(Base):
    __tablename__ = "lineage"

    id = Column(Integer, primary_key=True, index=True)

    upstream_id = Column(
        Integer,
        ForeignKey("datasets.id", ondelete="CASCADE"),
        nullable=False,
    )

    downstream_id = Column(
        Integer,
        ForeignKey("datasets.id", ondelete="CASCADE"),
        nullable=False,
    )

    __table_args__ = (
        UniqueConstraint(
            "upstream_id",
            "downstream_id",
            name="uq_lineage_edge",
        ),
    )
