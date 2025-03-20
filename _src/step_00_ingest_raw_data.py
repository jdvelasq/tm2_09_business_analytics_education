# pylint: disable=import-error
from techminer2.ingest import ingest_raw_data  # type: ignore

if __name__ == "__main__":
    ingest_raw_data(
        #
        # DATABASE PARAMS:
        root_dir="./",
    )
