# -*- coding: utf-8 -*-
import pandas as pd


class PerpetualCalendar(object):
    def __init__(self):
        import os.path
        file_path = os.path.abspath(os.path.dirname(__file__))
        # self.calendar: pd.DataFrame = pd.read_pickle(file_path + '/cp_calendar.pkl')  # This is a data file
        self.calendar: pd.DataFrame = pd.read_csv(file_path + '/cp_calendar.csv.gz', compression='gzip')

        self.calendar[['GYear', 'GMonth', 'GDay']] = self.calendar[['GYear', 'GMonth', 'GDay']].apply(
            pd.to_numeric)
        # self.calendar['GregorianDateTime'] = pd.to_datetime(self.calendar['GregorianDateTime'], format="%Y-%m-%d", )
        self.calendar['is_weekday'] = self.calendar['is_weekday'].astype('bool')  # 转为 bool 类型
        self.calendar['is_weekend'] = self.calendar['is_weekend'].astype('bool')
        self.calendar.set_index('GregorianDate', inplace=True)

    def get_all_data(self, start, end):
        data = self.calendar
        # if start
        if start:
            # todo 待优化
            data = data[(data.index > start)]
        if end:
            data = data[(data.index < end)]
        return data
