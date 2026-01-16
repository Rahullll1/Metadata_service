# Metadata_service

# Metadata Service

## Overview
This project is a **Metadata Management Service** built using **FastAPI**.  
It allows users to register datasets, search datasets using priority-based logic, and define lineage relationships between datasets while preventing cyclic dependencies.

The service models how modern data governance platforms manage dataset metadata rather than actual data.

---

## Problem Statement
The goal of this project is to design and implement a backend service that:
- Stores dataset metadata using a fully qualified name (FQN)
- Supports intelligent search across dataset attributes
- Tracks dataset lineage with validation to prevent invalid relationships

---

## Tech Stack
- **FastAPI** – REST API framework  
- **SQLAlchemy** – ORM for database interactions  
- **MySQL** – Relational database  
- **Alembic** – Database migrations  
- **Poetry** – Dependency and environment management  
- **Swagger UI** – API testing and documentation  

---

## Core Features

### 1. Dataset Management
- Create datasets with column-level metadata
- Each dataset is uniquely identified by a Fully Qualified Name (FQN)
- Enforces uniqueness and validates inputs at the API level

### 2. Priority-Based Search
Search datasets using a keyword with the following priority order:
1. Table name  
2. Column name  
3. Schema name  
4. Database name  

Search results are sorted by priority to return the most relevant datasets first.

### 3. Lineage Management
- Create upstream → downstream relationships between datasets
- Validates that both datasets exist before creating lineage
- Prevents cyclic dependencies using graph traversal logic

