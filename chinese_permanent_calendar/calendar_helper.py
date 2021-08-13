# -*- coding: utf-8 -*-
from .perpetual_calendar import PerpetualCalendar
import datetime
import pandas as pd

_calendar = PerpetualCalendar()


def merge_column(dataframe, column, seq=' ') -> set:
    """合并多个列的信息"""
    merge_sentence = set()
    all_sentences = dataframe[column].values.tolist()
    for s in all_sentences:
        if not pd.isna(s):
            for i in s.split(seq):
                merge_sentence.add(i)
    return merge_sentence


def check_info(info, target):
    """提取一列中的信息"""
    if not pd.isna(info):
        for i in info.split(' '):
            if i in target:
                return True
    return False


# 0. 全部信息 finish
def get_info_by_date(date: datetime.date) -> pd.Series:
    """通过阳历日期返回这一天的全部信息"""
    return _calendar.calendar.loc[str(date)]


def get_all_data(start=datetime.date(1970, 1, 1), end=datetime.date(2099, 12, 31)) -> pd.DataFrame:
    """得到一段日期内的全部信息"""
    return _calendar.get_all_data(str(start), str(end))


# 1.节日
def get_lunar_festival(date: datetime.date) -> str:
    return _calendar.calendar.loc[str(date), 'LJie']


def get_festival_by_days(start: str = '1970-01-01', end: str = '2099-12-31', gregorian=True, lunar=True) -> set:
    """得到一个时间段内的全部节日"""
    data = get_all_data(start, end)
    festival = set()
    if lunar:
        festival = festival | merge_column(data, 'LJie')
    if gregorian:
        festival = festival | merge_column(data, 'GJie')
    return festival


def get_days_by_festival(festival: list, start: str = '1970-01-01', end: str = '2099-12-31', gregorian=True,
                         lunar=True):
    """查询一个时间段内包含这个节日的日子"""
    data = get_all_data(start, end)
    check_df = pd.DataFrame(columns=data.columns)
    if gregorian:
        check_index = data['LJie'].apply(check_info, args=(festival))
        check_df = check_df.append(data[check_index])
    if lunar:
        check_index = data['GJie'].apply(check_info, args=(festival))
        check_df = check_df.append(data[check_index])
    return check_df


# 7:日期转换
def get_lunar_by_gregorian(date: datetime.date) -> pd.Series:
    """
    根据阳历，得到对应的阴历的：阴历时间、阴历节日、宜、忌、冲、煞、神位、胎神 信息
    :param date: 阳历日期
    :return: 阴历时间、阴历节日、宜、忌、冲、煞、神位、胎神
    """
    return get_info_by_date(date)


def get_gregorian_by_lunar(date: datetime.date):
    """
    根据阴历日期，得到
    :param date: 阴历日期
    :type date: datetime.date
    :return:
    """
    all_data = get_all_data()
    target_data = all_data[all_data['LunarDate'] == str(date)]
    if target_data.empty:
        return None
    else:
        return target_data.iloc[0, :]


# 8:节假日、工作日
def is_weekend(date: datetime.date) -> bool:
    """判断一天是否为节假日"""
    return _calendar.calendar.loc[str(date), 'is_weekend']


def is_weekday(date: datetime.date) -> bool:
    """判断一天是否为工作日"""
    return not is_weekend(date)
