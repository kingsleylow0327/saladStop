Pre-Requisite:
Docker (If you do not wish to install docker, Try B)

Steps to build (A):

1. Build a docker version of SQL so that the SQL that we are using is completely Isolated with other project
docker run --name salad_stop_sql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=123456 -d mysql

2. Build flask app docker
docker build -t salad_stop:0.1 -f ./Dockerfile.salad-stop .

3. Run flask app docker
docker run --name salad_stop_app -p 5000:5000 -e MYSQL_HOST=host.docker.internal -e MYSQL_USER=root -e MYSQL_PASS=123456 salad_stop:0.1


(Not preferable, will clear all sql schemas in database)
Steps to build (B):

1. Open .env, change to desire DB credential (This app will create new db schema and table)

2. Install python depenency
pip3 install -r ./requirement.txt

3. Run flask app (Reminder, this step will clear all sql schemas in your database)
python ./app.py


How to load Excel data into database?
When the flask app is starting, the excel data will automatically loads into SQL Database.
Everytime flask app is running, it will clear the databases and reload the excel data into it (initialization)

If you want to run the loading of excel manually, you can run the following command:
python ./db_query.py


EndPoint Format: http://127.0.0.1:5000/data?startDate=2021-12-11&endDate=2021-12-31
You may replace startDate and endDate value
The date format must be YYYY-MM-DD, otherwise will return error message in json format


py_test folder contained py_test, following shows the run command
python -m pytest .\ut_db_query.py
python -m pytest .\ut_json_return.py
