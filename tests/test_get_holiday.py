# -*- coding: utf-8 -*-

# from chinese_permanent_calendar import get_all_data, get_lunar_info
import datetime
import unittest

# Check if 2018-04-30 is holiday in China
# april_last = datetime.date(2018, 4, 30)
# get_lunar_date(april_last)  # 2018-3-15
# or check and get the holiday name

# ['LunarDateTime', 'LJie', 'GJie', 'Yi', 'Ji', 'ShenWei', 'Taishen',
#        'Chong', 'SuiSha', 'WuxingJiazi', 'WuxingNaYear', 'WuxingNaMonth',
#        'WuxingNaDay', 'MoonName', 'XingEast', 'XingWest', 'PengZu', 'JianShen',
#        'TianGanDiZhiYear', 'TianGanDiZhiMonth', 'TianGanDiZhiDay',
#        'LMonthName', 'LYear', 'LMonth', 'LDay', 'SolarTermName', 'GYear',
#        'GMonth', 'GDay', 'is_weekend', 'is_weekday']
# from chinese_permanent_calendar import get_all_festival

# get_all_festival(festival='国庆节', start='2020-01-01', end='2020-03-01')


class AddCodeTest(unittest.TestCase):

    def test_info(self):
        from chinese_permanent_calendar import get_lunar_date
        april_last = datetime.date(2018, 4, 30)
        self.assertEqual(get_lunar_date(april_last).tolist(), ['狗', '三月', '十五'])
        # self.assertEqual(add_code.append(1, 2), 3)  # 使用 self.assert.... 来做判别

    def test_holiday(self):
        from chinese_permanent_calendar import is_weekday, is_weekend
        april_last = datetime.date(2018, 4, 29)
        self.assertTrue(is_weekend(april_last))
        self.assertTrue(not is_weekday(april_last))

    def test_festival(self):
        from chinese_permanent_calendar import get_all_festival
        self.assertIsNone(get_all_festival())
        self.assertEqual(get_all_festival(festival='国庆节', start='2020-01-01', end='2020-03-01'))
