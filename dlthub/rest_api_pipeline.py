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

    # create a dlt source that will load tables "family" and "genome"
    source = sql_database().with_resources("family", "genome")

    # Create a dlt pipeline object
    pipeline = dlt.pipeline(
        pipeline_name="sql_to_duckdb_pipeline", # custom name for the pipeline
        destination="duckdb", # dlt destination to which the data will be loaded
        dataset_name="sql_to_duckdb_pipeline_data" # custom name for the dataset created in the destination
    )

    # Run the pipeline
    load_info = pipeline.run(source)

    # Pretty print load information
    print(load_info)

if __name__ == '__main__':
    load_tables_family_and_genome()

