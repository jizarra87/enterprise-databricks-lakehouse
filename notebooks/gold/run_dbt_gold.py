# Databricks notebook source
%pip install dbt-databricks
dbutils.library.restartPython()

import os
import subprocess

token = dbutils.secrets.get(scope="dbt", key="databricks_token")
os.environ["DATABRICKS_TOKEN"] = token

project_dir = "/Workspace/Users/juancarlosizarra@gmail.com/.bundle/enterprise-databricks-lakehouse/dev/files/enterprise_lakehouse_dbt"

commands = [
    ["dbt", "run", "--profiles-dir", "profiles", "--select", "dim_customers", "fact_sales"],
    ["dbt", "test", "--profiles-dir", "profiles", "--select", "dim_customers", "fact_sales"]
]

for command in commands:
    result = subprocess.run(
        command,
        cwd=project_dir,
        capture_output=True,
        text=True
    )

    print(result.stdout)

    if result.returncode != 0:
        print(result.stderr)
        raise Exception(f"Command failed: {' '.join(command)}")