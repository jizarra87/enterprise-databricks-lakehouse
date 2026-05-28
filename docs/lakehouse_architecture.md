# Lakehouse Architecture

## Business Domain

This project simulates an enterprise retail and ecommerce data platform.

The platform integrates operational data from multiple business domains including customers, products, orders, inventory, suppliers, shipments, and payments.

The goal is to build a scalable lakehouse architecture that supports analytics, reporting, governance, and future AI use cases.

## Source Systems

### ERP System
- Products
- Inventory
- Suppliers

### CRM System
- Customers
- Customer interactions

### Ecommerce Platform
- Orders
- Payments
- Shipments

### External APIs
- Currency exchange rates
- Weather data
- Logistics tracking events

## Medallion Architecture

### Bronze Layer
Raw ingestion layer that preserves source fidelity.

Main responsibilities:
- Incremental ingestion
- Raw historical retention
- Schema evolution handling
- Audit metadata capture

Example tables:
- bronze_customers
- bronze_orders
- bronze_products
- bronze_inventory
- bronze_shipments

---

### Silver Layer
Cleaned and standardized enterprise data layer.

Main responsibilities:
- Deduplication
- Data quality validation
- Standardization
- Null handling
- Conformed business entities

Example tables:
- silver_customers
- silver_orders
- silver_products
- silver_inventory
- silver_shipments

---

### Gold Layer
Business-ready analytical and reporting layer.

Main responsibilities:
- Dimensional modeling
- KPI generation
- Aggregated analytics
- AI-ready curated datasets

Fact tables:
- fact_sales
- fact_inventory
- fact_shipments

Dimension tables:
- dim_customer
- dim_product
- dim_supplier
- dim_date

## Delta Lake Strategy

The platform uses Delta Lake as the primary storage format.

Key capabilities:
- ACID transactions
- Time travel
- Schema evolution
- Incremental processing
- Scalable analytics workloads

Partitioning strategy will be applied to large transactional tables to optimize query performance and storage efficiency.