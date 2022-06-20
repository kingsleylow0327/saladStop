import pandas as pd
from json_return import json_return
from sqlalchemy import create_engine
from list_of_var import SQL_URL, DB_NAME, TABLE_NAME, INIT_QUERY, USE_DB, SQL_QUERY

# Create SQLAlchemy engine to connect to MySQL Database
engine = create_engine(SQL_URL)


def init_database_from_excel(path):
    # Initialize Database
    for query in INIT_QUERY:
        engine.execute(query.format(DB_NAME))
    df = pd.read_excel(path, header=2)
    df.to_sql(TABLE_NAME, engine, index=False)
    return df


def get_data(start_date, end_date):
    engine.execute(USE_DB)
    sql_ret = engine.execute(SQL_QUERY.format(start_date, end_date)).fetchmany()

    # Out of date range
    if len(sql_ret) != 1:
        return json_return(*(0,0,0), error_code=-1).get_json()

    return json_return(*sql_ret[0]).get_json()

# Testing Code
if "__main__" == __name__:
    print(get_data('2021-01-01','2021-01-02'))
