from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.dataset import Dataset
from app.models.lineage import Lineage
from app.schemas.lineage import LineageCreate
from app.utils.graph import has_path

router = APIRouter(prefix="/lineage", tags=["Lineage"])


@router.post("", status_code=status.HTTP_201_CREATED)
def create_lineage(
    payload: LineageCreate,
    db: Session = Depends(get_db),
):
    # Fetch datasets
    upstream = db.query(Dataset).filter(Dataset.fqn == payload.upstream_fqn).first()
    downstream = db.query(Dataset).filter(Dataset.fqn == payload.downstream_fqn).first()

    if not upstream or not downstream:
        raise HTTPException(
            status_code=404,
            detail="Upstream or downstream dataset not found",
        )

    if upstream.id == downstream.id:
        raise HTTPException(
            status_code=400,
            detail="Upstream and downstream cannot be the same dataset",
        )

    # Build graph from existing lineage
    lineage_rows = db.query(Lineage).all()
    graph = {}
    for row in lineage_rows:
        graph.setdefault(row.upstream_id, []).append(row.downstream_id)

    # Cycle check: does downstream reach upstream already?
    if has_path(graph, downstream.id, upstream.id):
        raise HTTPException(
            status_code=400,
            detail="Invalid lineage: cycle detected",
        )

    # Prevent duplicates
    existing = (
        db.query(Lineage)
        .filter(
            Lineage.upstream_id == upstream.id,
            Lineage.downstream_id == downstream.id,
        )
        .first()
    )
    if existing:
        raise HTTPException(
            status_code=400,
            detail="Lineage already exists",
        )

    # Create lineage
    edge = Lineage(
        upstream_id=upstream.id,
        downstream_id=downstream.id,
    )
    db.add(edge)
    db.commit()

    return {"message": "Lineage created successfully"}
