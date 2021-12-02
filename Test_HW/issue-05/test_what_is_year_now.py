import pytest
import urllib.request
from unittest.mock import patch
from io import StringIO
from issue05.what_is_year_now import what_is_year_now


def test_format_yyyy_mm_dd():
    """
    Тестируем программу, когда формат даты: YYYY-MM-DD
    """
    date = StringIO('{"currentDateTime": "1999-04-05"}')
    exp_year = 1999
    with patch.object(urllib.request, 'urlopen', return_value=date):
        actual_year = what_is_year_now()
        assert exp_year == actual_year


def test_format_dd_mm_yyyy():
    """
    Тестируем программу, когда формат даты: DD-MM-YYYY
    """
    date = StringIO('{"currentDateTime": "05.04.1999"}')
    exp_year = 1999
    with patch.object(urllib.request, 'urlopen', return_value=date):
        actual_year = what_is_year_now()
        assert exp_year == actual_year


def test_invalid_data():
    """
    Тестируем программу, когда вместо даты мусор
    """
    date = StringIO('{"currentDateTime": "awdajv%@77gs!89-s"}')
    with pytest.raises(ValueError):
        with patch.object(urllib.request, 'urlopen', return_value=date):
            what_is_year_now()

