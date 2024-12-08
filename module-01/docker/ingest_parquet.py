import argparse
import os
import pyarrow.parquet as pq

from time import time
from sqlalchemy import create_engine

BATCH_SIZE = 100000


def get_url(url: str) -> str:
    file = url.split("/")[-1]
    print(f"Downloading '{file}' from '{url}'")
    os.system(f"curl {url} -o {file}")
    print("Downloaded successfully.")
    return file


def main(
    user: str,
    password: str,
    host: str,
    port: str,
    db: str,
    tb: str,
    url: str,
):
    file = get_url(url)

    # Create SQL connection
    engine = create_engine(f"postgresql://{user}:{password}@{host}:{port}/{db}")

    parquet = pq.ParquetFile(file)
    # Read parquet into dataframe in chunks
    df = next(parquet.iter_batches()).to_pandas()

    # Create the table in db
    df.head(0).to_sql(name=tb, con=engine, if_exists="replace")

    # Insert the parquet
    start = time()
    chunk_count = 0

    for chunk in parquet.iter_batches(batch_size=BATCH_SIZE):
        chunk_count += 1
        df = chunk.to_pandas()

        chunk_start = time()
        df.to_sql(name=tb, con=engine, if_exists="append")
        chunk_end = time()

        print(
            f"Inserted chunk {chunk_count} in {chunk_end - chunk_start:10.3f} seconds\n"
        )

    print(f"Inserted {chunk_count} chunks in {time() - start:10.3f}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Loading data from .parquet file link to a Postgres datebase."
    )

    parser.add_argument("--user", help="Username for Postgres.")
    parser.add_argument("--password", help="Password to the username for Postgres.")
    parser.add_argument("--host", help="Hostname for Postgres.")
    parser.add_argument("--port", help="Port for Postgres.")
    parser.add_argument("--db", help="Database name for Postgres")
    parser.add_argument("--tb", help="Destination table name for Postgres.")
    parser.add_argument("--url", help="URL for .parquet file.")

    args = parser.parse_args()
    main(args.user, args.password, args.host, args.port, args.db, args.tb, args.url)
