from enum import Enum


class error(Enum):
    OUT_OF_RANGE = -1
    MISSING_PARAM = -2
    WRONG_FORMAT = -3


ERROR_SET = (0, 0, 0)


ERROR_MAP = {error.OUT_OF_RANGE: {"Error": "No data within this date range"},
             error.MISSING_PARAM: {"Error": "Missing startDate or endDate"},
             error.WRONG_FORMAT: {"Error": "Wrong date format(YYYY-MM-DD) or Invalid Date"}}  # noqa: E501
