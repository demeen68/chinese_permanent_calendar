# -*- coding: utf-8 -*-

# import chinese_permanent_calendar as chinese_pc
from chinese_permanent_calendar import get_all_data, get_lunar_info
import datetime
import unittest

# Check if 2018-04-30 is holiday in China
print('a')
april_last = datetime.date(2018, 4, 30)
data = get_all_data()
# get_lunar_date(april_last)  # 2018-3-15
# or check and get the holiday name
info = get_lunar_info(april_last)
import chinese_calendar as calendar  # with different import style

on_holiday, holiday_name = calendar.get_holiday_detail(april_last)
self.assertTrue(on_holiday)
self.assertEqual(calendar.Holiday.labour_day.value, holiday_name)

# even check if a holiday is in lieu
import chinese_calendar

self.assertFalse(chinese_calendar.is_in_lieu(datetime.date(2006, 2, 1)))
self.assertTrue(chinese_calendar.is_in_lieu(datetime.date(2006, 2, 2)))
