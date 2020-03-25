from log_data_parse import convert_to_datetime, time_between_shutdowns, SHUTDOWN_EVENT
from datetime import datetime

def test_convert_to_datetime():
    line = "INFO 2014-07-03T23:27:51 supybot Shutdown complete."
    assert convert_to_datetime(line=line) == datetime(2014, 7, 3, 23, 27, 51)

def test_time_between_shutdowns():
    log_lines = "INFO 2014-07-03T23:27:51 supybot Shutdown initiated," \
                "INFO 2014-07-03T23:57:51 supybot Shutdown initiated."
    assert time_between_shutdowns(loglines=log_lines) == datetime(2014, 7, 3, 23, 57, 51) - datetime(2014, 7, 3, 23, 27, 51)