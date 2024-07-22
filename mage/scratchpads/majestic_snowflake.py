"""
NOTE: Scratchpad blocks are used only for experimentation and testing out code.
The code written here will not be executed as part of the pipeline.
"""
import os
import psycopg


create_table_statement = """
drop table if exists dummy_metrics;
create table dummy_metrics(
	timestamp timestamp,
	value1 integer,
	value2 varchar,
	value3 float
)
"""

def prep_db():
	with psycopg.connect("host=postgres port=5432 user=postgres password=postgres", autocommit=True) as conn:
		res = conn.execute("SELECT 1 FROM pg_database WHERE datname='mage'")
		if len(res.fetchall()) == 0:
			conn.execute("create database mage;")
		with psycopg.connect("host=postgres port=5432 dbname=mage user=postgres password=postgres") as conn:
			conn.execute(create_table_statement)

prep_db()