import json
from flask import Flask, request
from initialise_db import init_database_from_excel
from list_of_var import EXCEL_PATH
from json_return import json_return

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True


if __name__ == '__main__':
    # Initialize db everytime flask app is started
    init_database_from_excel(EXCEL_PATH)
    app.run(debug = True)
