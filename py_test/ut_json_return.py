import sys
sys.path.append("../")
from unittest import TestCase
import json_return
from errors import error, ERROR_MAP


valid_return = {"totalCost": "1.00",
                "avgCostWoGst": "2.00",
                "topSupplierCountry": "SG"}


class TestJsonReturn(TestCase):

    def test_get_json_no_error(self):
        test_obj = json_return.JsonReturn(1, 2, "SG").get_json()
        assert (test_obj == valid_return)

    def test_get_json_out_of_range_error(self):
        test_obj = json_return.JsonReturn(1,
                                          2,
                                          "SG",
                                          error_code=error.OUT_OF_RANGE)
        assert (test_obj.get_json() == ERROR_MAP[error.OUT_OF_RANGE])

    def test_get_json_missing_param_error(self):
        test_obj = json_return.JsonReturn(1,
                                          2,
                                          "SG",
                                          error_code=error.MISSING_PARAM)
        assert (test_obj.get_json() == ERROR_MAP[error.MISSING_PARAM])

    def test_get_wrong_format_error(self):
        test_obj = json_return.JsonReturn(1,
                                          2,
                                          "SG",
                                          error_code=error.WRONG_FORMAT)
        assert (test_obj.get_json() == ERROR_MAP[error.WRONG_FORMAT])
