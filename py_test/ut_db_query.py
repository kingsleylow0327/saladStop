import sys
sys.path.append("../")
from unittest import TestCase
from unittest.mock import patch
import db_query
from errors import error, ERROR_MAP


class TestDBQuery(TestCase):

    @patch.object(db_query, "engine")
    def test_init_database_from_excel(self, engine_mock):
        db_query.init_database_from_excel("./data/dummy.xlsx")
        assert (engine_mock.execute.call_count == 3)

    def test_get_query_data_missing_param(self):
        test_obj1 = db_query.get_query_data(None, "2021-01-01")
        assert (test_obj1 == ERROR_MAP[error.MISSING_PARAM])

        test_obj2 = db_query.get_query_data("2021-01-01", None)
        assert (test_obj2 == ERROR_MAP[error.MISSING_PARAM])

        test_obj3 = db_query.get_query_data(None, None)
        assert (test_obj3 == ERROR_MAP[error.MISSING_PARAM])

    def test_get_query_data_wrong_format(self):
        test_obj1 = db_query.get_query_data("2021-01-01", "123")
        assert (test_obj1 == ERROR_MAP[error.WRONG_FORMAT])

        test_obj2 = db_query.get_query_data("aasd", "2021-01-01")
        assert (test_obj2 == ERROR_MAP[error.WRONG_FORMAT])

    @patch.object(db_query, "engine")
    def test_get_query_data_out_of_range(self, engine_mock):
        test_obj1 = db_query.get_query_data("2021-03-01", "2021-01-01")
        assert (engine_mock.execute.call_count == 2)
        assert (test_obj1 == ERROR_MAP[error.OUT_OF_RANGE])
