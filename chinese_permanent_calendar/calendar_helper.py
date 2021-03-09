# -*- coding: utf-8 -*-
from perpetual_calendar import PerpetualCalendar
import datetime
import pandas as pd

_calendar = PerpetualCalendar()


def get_all_data():
    return _calendar.get_all_data()


def _get_info_series(date: datetime.date) -> pd.Series:
    return _calendar.calendar.loc[str(date)]


def get_lunar_info(date: datetime.date) -> pd.Series:
    """
    得到阳历对应的阴历的  阴历时间、阴历节日、宜、忌、冲、煞、神位、胎神
    :param date: 阳历日期
    :return: 阴历时间、阴历节日、宜、忌、冲、煞、神位、胎神
    """
    lunar_series: pd.Series = _get_info_series(date)
    return pd.Series(
        lunar_series,
        index=['LunarDateTime', 'Ljie', 'Yi', 'Ji', 'ShenWei', 'Taishen', 'Chong', 'SuiSha', ])


def get_lunar_festival(date: datetime.date) -> str:
    return _calendar.calendar.loc[str(date), 'LJie']


def is_weekend(date: datetime.date) -> bool:
    return _calendar.calendar.loc[str(date), 'is_weekend']


def is_weekday(date: datetime.date) -> bool:
    return not is_weekend(date)