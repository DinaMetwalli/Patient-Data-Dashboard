import psycopg2


def test_underlying_pg_connection():
    psycopg2.connect(
        "dbname=postgres user=postgres password=postgres host=localhost port=5432")