import db_query
from db_query import get_query_data
from flask import Flask, request
from list_of_var import EXCEL_PATH

app = Flask(__name__)
app.config["JSONIFY_PRETTYPRINT_REGULAR"] = True


@app.route("/data", methods=["GET"])
def get_data():
    start_date = request.args.get("startDate")
    end_date = request.args.get("endDate")
    return get_query_data(start_date, end_date)


if __name__ == "__main__":
    # Initialize db everytime flask app is started
    db_query.init_database_from_excel(EXCEL_PATH)
    app.run(host='0.0.0.0', port=5000, debug=True)
