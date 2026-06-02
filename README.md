# Enterprise Databricks Lakehouse Platform

## Overview

This project demonstrates the implementation of a modern enterprise lakehouse architecture using Databricks, Delta Lake, PySpark, and Unity Catalog.

The platform follows a Medallion Architecture approach (Bronze → Silver → Gold) and simulates a real-world retail analytics environment with scalable ingestion pipelines, incremental processing, orchestration workflows, and analytical fact/dimension modeling.

The project was designed to emulate production-grade data engineering patterns commonly used in modern cloud analytics platforms.

---

# Architecture

## Medallion Architecture

```text
Raw CSV Files
    ↓
Bronze Layer
    ↓
Silver Layer
    ↓
Gold Layer
```

### Bronze Layer

* Raw ingestion layer
* Metadata enrichment
* Incremental ingestion
* Source traceability

### Silver Layer

* Cleansing and standardization
* Deduplication
* Business validation rules
* Data quality improvements

### Gold Layer

* Dimensional modeling
* Fact and dimension tables
* KPI-ready analytical datasets
* BI and reporting optimized structures

---

# Technologies Used

* Databricks
* PySpark
* Delta Lake
* Unity Catalog
* SQL
* Python
* Delta MERGE
* Databricks Workflows
* Delta Optimization (OPTIMIZE / ZORDER)
* Medallion Architecture

---

# Data Model

## Dimensions

* `gold.dim_customers`

## Fact Tables

* `gold.fact_sales`

---

# Pipeline Components

## Customer Pipeline

```text
bronze_customers_ingestion
    ↓
silver_customers_transformation
    ↓
gold_customers_dimension
```

## Orders Pipeline

```text
bronze_orders_ingestion
    ↓
silver_orders_transformation
    ↓
gold_fact_sales
```

---

# Incremental Processing

The project includes incremental loading patterns using Delta Lake `MERGE INTO` operations to simulate enterprise-grade upsert pipelines.

Capabilities demonstrated:

* Incremental ingestion
* Upserts
* Transactional processing
* Delta Lake ACID operations

---

# Workflow Orchestration

Databricks Workflows were implemented to orchestrate notebook dependencies and automate pipeline execution across Bronze, Silver, and Gold layers.

---

# Performance Optimization

Delta optimization techniques implemented:

* OPTIMIZE
* ZORDER
* Delta transaction history
* File compaction strategies

---

# Data Quality Framework

The platform includes a Data Quality validation framework designed to simulate enterprise-grade governance and resiliency patterns.

## Validation Rules

The pipeline validates:

* Null business keys
* Invalid quantities
* Negative prices
* Invalid total amounts
* Missing order dates

## Quarantine Pattern

Invalid records are automatically redirected into quarantine tables for auditing and remediation instead of being discarded.

### Valid Records

```text
silver.orders_validated
```

### Invalid Records

```text
silver.quarantine_orders
```

This pattern improves:

* Data trust
* Recoverability
* Governance
* Auditability
* Pipeline resiliency


# Unity Catalog Organization

```text
enterprise_lakehouse
    ├── bronze
    ├── silver
    └── gold
```

---

# Screenshots

## Workflow DAG

![Workflow DAG](docs/architecture/screenshots/workflow_dag.png)

## Unity Catalog

![Unity Catalog](docs/architecture/screenshots/unity_catalog.png)

## Fact Sales Table

![Fact Sales](docs/architecture/screenshots/fact_sales.png)

---

# Future Enhancements

* CDC pipelines
* Slowly Changing Dimensions (SCD)
* dbt integration
* Data Quality framework
* Streaming ingestion
* CI/CD automation
* Terraform infrastructure deployment
* Monitoring and alerting

---

# Project Goals

This project was built to demonstrate practical experience with:

* Modern Data Engineering
* Databricks Lakehouse Architecture
* Enterprise ETL Design
* Delta Lake Transactional Processing
* Scalable Analytics Engineering
* Production-style Workflow Orchestration
