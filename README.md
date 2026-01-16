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

## Architecture Decisions

The architecture of this project was designed with simplicity, clarity, and real-world backend practices in mind.

### Backend Framework
FastAPI was chosen for its high performance, built-in request validation using Pydantic, and automatic API documentation via Swagger UI. This made it suitable for rapid development while maintaining production-quality standards.

### Data Modeling
Datasets are uniquely identified using a Fully Qualified Name (FQN), which encodes the connection, database, schema, and table information. This approach avoids unnecessary table duplication and keeps the data model simple and normalized.

Column metadata is stored in a separate table with a one-to-many relationship to datasets, enabling flexible schema definitions per dataset.

### Database & ORM
MySQL was selected as a reliable relational database, and SQLAlchemy was used as the ORM to abstract database interactions. This combination provides strong data integrity, portability, and maintainability.

Database schema changes are managed using Alembic migrations to ensure version-controlled and repeatable schema evolution.

### Search Design
The search functionality was implemented using application-level logic rather than complex database queries. Each dataset is evaluated against the search keyword and assigned a priority based on where the match occurs (table, column, schema, or database). Results are then sorted by priority to ensure relevance while keeping the implementation easy to understand and maintain.

### Lineage & Cycle Detection
Dataset lineage is modeled as a directed graph. Before creating a new lineage relationship, a depth-first search (DFS) is performed to detect whether adding the relationship would introduce a cycle. This prevents invalid upstream/downstream dependencies and ensures graph consistency without over-engineering.

### Configuration & Environment Management
Configuration values such as database credentials are managed using environment variables. Poetry is used for dependency and environment management to ensure reproducible builds and clean dependency resolution.

Overall, the architecture focuses on correctness, readability, and engineering maturity rather than over-optimization or unnecessary complexity.


