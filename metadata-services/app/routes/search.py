from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.dataset import Dataset
from app.models.column import ColumnMeta

router = APIRouter(prefix="/search", tags=["Search"])


@router.get("")
def search_datasets(
    query: str = Query(..., min_length=1),
    db: Session = Depends(get_db),
):
    results = []

    datasets = db.query(Dataset).all()

    for dataset in datasets:
        parts = dataset.fqn.split(".")
        if len(parts) != 4:
            continue

        connection, database, schema, table = parts
        priority = None

        # Priority 1: table name
        if query.lower() in table.lower():
            priority = 1

        # Priority 2: column name
        elif any(
            query.lower() in col.name.lower()
            for col in dataset.columns
        ):
            priority = 2

        # Priority 3: schema name
        elif query.lower() in schema.lower():
            priority = 3

        # Priority 4: database name
        elif query.lower() in database.lower():
            priority = 4

        if priority:
            results.append(
                {
                    "fqn": dataset.fqn,
                    "source_type": dataset.source_type,
                    "columns": [
                        {
                            "name": col.name,
                            "data_type": col.data_type,
                        }
                        for col in dataset.columns
                    ],
                    "priority": priority,
                }
            )

    # Sort by priority (1 → 4)
    results.sort(key=lambda x: x["priority"])

    return results
