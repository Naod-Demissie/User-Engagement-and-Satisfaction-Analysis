import psycopg2
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()


def fetch_data_from_db(query):
    """
    Fetch data from a PostgreSQL database and load it into a Pandas DataFrame.

    Parameters:
        query (str): SQL query to fetch data.

    Returns:
        pd.DataFrame: DataFrame containing the query result.
    """
    try:
        # Fetch database connection details from environment variables
        dbname = os.getenv("DB_NAME")
        user = os.getenv("DB_USER")
        password = os.getenv("DB_PASSWORD")
        host = os.getenv("DB_HOST")
        port = os.getenv("DB_PORT")

        # Connect to the PostgreSQL database
        conn = psycopg2.connect(
            dbname=dbname, user=user, password=password, host=host, port=port
        )

        # Load data into Pandas DataFrame
        df = pd.read_sql_query(query, conn)
        return df

    except Exception as e:
        print(f"Error: {e}")
        return None

    finally:
        if "conn" in locals() and conn is not None:
            conn.close()
