# flake8: noqa
import humanize
from typing import Any
import os

import dlt
from dlt.common import pendulum
from dlt.sources.credentials import ConnectionStringCredentials

from dlt.sources.sql_database import sql_database, sql_table, Table

from sqlalchemy.sql.sqltypes import TypeEngine
import sqlalchemy as sa


def load_tables_family_and_genome():

    source = sql_database().with_resources("family", "genome")

    pipeline = dlt.pipeline(
        pipeline_name="sql_to_duckdb_pipeline",
        destination="duckdb",
        dataset_name="sql_to_duckdb_pipeline_data"
    )

    load_info = pipeline.run(source, write_disposition="replace") # Set write_disposition to load the data with "replace"

    print(load_info)

if __name__ == '__main__':
    load_tables_family_and_genome()