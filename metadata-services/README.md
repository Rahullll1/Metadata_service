# Metadata Service

# Overview
This project is a Metadata Management Service built using FastAPI.  
It allows users to register datasets, search datasets using priority-based logic, and define lineage relationships between datasets with cycle detection.

The project demonstrates real-world backend development practices including database design, API validation, and graph-based problem solving.


# Tech Stack
- FastAPI
- SQLAlchemy
- MySQL
- Alembic
- Poetry
- Swagger UI


# Features

# 1. Dataset Management
- Create datasets with column metadata
- Enforces uniqueness using Fully Qualified Name (FQN)
- Stores dataset and column information in a relational database

# 2. Priority-Based Search
Search datasets using a keyword with the following priority order:
1. Table name
2. Column name
3. Schema name
4. Database name

Results are sorted so the most relevant datasets appear first.

# 3. Lineage Management
- Create upstream → downstream dataset relationships
- Prevents cyclic dependencies using graph traversal
- Validates dataset existence before creating lineage



# Database Schema
- datasets
- columns
- lineage

Alembic is used for schema migrations.

---

# Running the Project

poetry install
poetry run alembic upgrade head
poetry run uvicorn app.main:app --reload

# Access Swagger UI at
# http://127.0.0.1:8000/docs
