import chinese_permanent_calendar as calendar
import datetime

# 根据阳历日期得到阴历日期的详情
date = datetime.date(2020, 1, 1)
luner_date = calendar.get_lunar_by_gregorian(date)
print("阳历：", luner_date.name, "阴历：", luner_date['LunarDate'])

# 根据阴历得到阳历日期及当天的详情
gregorian_date = calendar.get_gregorian_by_lunar(luner_date['LunarDate'])

# 得到所有节日包含国庆节的日期
date = calendar.get_days_by_festival(['国庆节'])

# 得到所有的日期数据
all_data = calendar.get_all_data(start=datetime.date(2020, 1, 1), end=datetime.date(2020, 2, 1))
