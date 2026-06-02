# Databricks notebook source
# MAGIC %sql
# MAGIC
# MAGIC OPTIMIZE enterprise_lakehouse.gold.fact_sales
# MAGIC ZORDER BY (customer_id, order_date);
# MAGIC