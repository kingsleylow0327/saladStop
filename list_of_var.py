# Connection Credential
HOSTNAME = "localhost"
UNAME = "root"
PWD = "123456"

# Database Name
DB_NAME = "salad_stop"

# Table Name
TABLE_NAME = "transaction_details"

# SQL URL
SQL_URL = "mysql+pymysql://{user}:{pw}@{host}".format(host=HOSTNAME,
                                                      user=UNAME,
                                                      pw=PWD)
# Database Initialisation Query
INIT_QUERY = ["DROP DATABASE IF EXISTS {}",
              "CREATE DATABASE {}",
              "USE {}"]

# Excel Path
EXCEL_PATH = "./excel_input/SaladStopdummydata.xlsx"
