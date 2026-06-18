# Databricks notebook source
%pip install dbt-databricks
dbutils.library.restartPython()

import os
import subprocess

token = dbutils.secrets.get(scope="dbt", key="databricks_token")
os.environ["DATABRICKS_TOKEN"] = token
os.environ["DBT_CATALOG"] = dbutils.widgets.get("catalog")

import os

notebook_path = dbutils.notebook.entry_point.getDbutils().notebook().getContext().notebookPath().get()
bundle_root = "/Workspace" + "/".join(notebook_path.split("/")[:-3])
project_dir = f"{bundle_root}/enterprise_lakehouse_dbt"

print(f"Notebook path: {notebook_path}")
print(f"Bundle root: {bundle_root}")
print(f"Project dir: {project_dir}")

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