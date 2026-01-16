from fastapi import FastAPI

from app.routes import datasets, search, lineage

app = FastAPI(title="Metadata Service")

app.include_router(datasets.router)
app.include_router(search.router)
app.include_router(lineage.router)

@app.get("/")
def health():
    return {"status": "ok"}
