from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.dataset import Dataset
from app.models.column import ColumnMeta
from app.schemas.dataset import DatasetCreate, DatasetResponse

router = APIRouter(prefix="/datasets", tags=["Datasets"])


@router.post(
    "",
    response_model=DatasetResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_dataset(
    payload: DatasetCreate,
    db: Session = Depends(get_db),
):
    # 1. Check for duplicate FQN
    existing = db.query(Dataset).filter(Dataset.fqn == payload.fqn).first()
    if existing:
        raise HTTPException(
            status_code=400,
            detail="Dataset with this FQN already exists",
        )

    # 2. Create dataset
    dataset = Dataset(
        fqn=payload.fqn,
        source_type=payload.source_type,
    )
    db.add(dataset)
    db.flush()  # get dataset.id

    # 3. Create columns
    columns = [
        ColumnMeta(
            name=col.name,
            data_type=col.data_type,
            dataset_id=dataset.id,
        )
        for col in payload.columns
    ]
    db.add_all(columns)

    db.commit()
    db.refresh(dataset)

    return dataset
