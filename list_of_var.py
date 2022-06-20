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
USE_DB = "USE " + DB_NAME

# Database Initialisation Query
INIT_QUERY = ["DROP DATABASE IF EXISTS {}",
              "CREATE DATABASE {}",
              USE_DB]

# Query
SQL_QUERY = """
SELECT 
SUM(`Total incl GST`) AS `totalCost`,
AVG(`Unitprice - SGD`) AS `avgCostWoGst`,
`Country of origin` AS `topSupplierCountry`
FROM `transaction_details`
WHERE
`Transaction date` >= '{}'
AND
`Transaction date` < '{}'
GROUP BY`Country of origin`
ORDER BY Count(`Country of origin`) DESC
LIMIT 1;
"""

# Excel Path
EXCEL_PATH = "./excel_input/SaladStopdummydata.xlsx"
