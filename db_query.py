import datetime
import pandas as pd
from errors import error, ERROR_SET
from json_return import JsonReturn
from list_of_var import SQL_URL, DB_NAME, TABLE_NAME, INIT_QUERY, USE_DB, SQL_QUERY, EXCEL_PATH  # noqa: E501
from sqlalchemy import create_engine

# Create SQLAlchemy engine to connect to MySQL Database
engine = create_engine(SQL_URL)


def init_database_from_excel(path):
    # Initialize Database
    for query in INIT_QUERY:
        engine.execute(query.format(DB_NAME))
    df = pd.read_excel(path, header=2)
    df.to_sql(TABLE_NAME, engine, index=False)


def get_query_data(start_date, end_date):
    # Missing Date
    if not start_date or not end_date:
        return JsonReturn(*ERROR_SET, error_code=error.MISSING_PARAM).get_json()  # noqa: E501

    # Format Check
    try:
        datetime.datetime.strptime(start_date, '%Y-%m-%d')
        datetime.datetime.strptime(end_date, '%Y-%m-%d')
    except:  # noqa: E722
        return JsonReturn(*ERROR_SET, error_code=error.WRONG_FORMAT).get_json()  # noqa: E501

    engine.execute(USE_DB)
    sql_ret = engine.execute(SQL_QUERY.format(start_date, end_date)).fetchmany()  # noqa: E501
    print(sql_ret)
    # Out of date range
    if len(sql_ret) != 1:
        return JsonReturn(*ERROR_SET, error_code=error.OUT_OF_RANGE).get_json()  # noqa: E501

    return JsonReturn(*sql_ret[0]).get_json()


if "__main__" == __name__:
    init_database_from_excel(EXCEL_PATH)
