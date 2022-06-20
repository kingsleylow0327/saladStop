import pandas as pd
from sqlalchemy import create_engine
from list_of_var import SQL_URL, DB_NAME, TABLE_NAME, EXCEL_PATH, INIT_QUERY

# Create SQLAlchemy engine to connect to MySQL Database
engine = create_engine(SQL_URL)


def init_database_from_excel(path):
    # Initialize Database
    for query in INIT_QUERY:
        engine.execute(query.format(DB_NAME))
    df = pd.read_excel(path, header=2)
    df.to_sql(TABLE_NAME, engine, index=False)
    return df


# Testing Code
if "__main__" == __name__:
    df = init_database_from_excel(EXCEL_PATH)
    print(df)
