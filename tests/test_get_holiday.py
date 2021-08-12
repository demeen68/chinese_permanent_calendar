# -*- coding: utf-8 -*-

import datetime
import unittest


class AddCodeTest(unittest.TestCase):

    def test_info(self):
        from chinese_permanent_calendar import get_lunar_by_gregorian, get_gregorian_by_lunar
        april_last = datetime.date(2018, 4, 30)
        self.assertIsNotNone(get_lunar_by_gregorian(april_last))
        self.assertIsNone(get_gregorian_by_lunar(april_last))

    def test_error_info(self):
        from chinese_permanent_calendar import get_gregorian_by_lunar
        self.assertIsNotNone(get_gregorian_by_lunar(datetime.date(1969, 11, 25)))

    def test_holiday(self):
        from chinese_permanent_calendar import is_weekday, is_weekend
        april_last = datetime.date(2018, 4, 29)
        self.assertTrue(is_weekend(april_last))
        self.assertTrue(not is_weekday(april_last))

    def test_festival(self):
        from chinese_permanent_calendar import get_festival_by_days, get_days_by_festival
        self.assertEqual(get_festival_by_days(start='2020-01-01', end='2020-01-05'), {'腊八节'})
        self.assertIsNotNone(get_days_by_festival(['腊八节'], start='1970-01-01', end='1980-01-01'))
