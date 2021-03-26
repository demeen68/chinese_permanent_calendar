import pandas as pd
import datetime


def get_week(year: int, month: int, day: int) -> str:
    check_week = datetime.datetime(year, month, day).strftime("%w")
    if check_week == '0':  # 由于周日会被认为是0，这里返回7
        return '7'
    else:
        return check_week


def change_seg(series):
    # 'GregorianDateTime' 'LunarDateTime' 'IsJieJia' 'LJie' 'GJie' 'Yi' 'Ji'
    #  'ShenWei' 'Taishen' 'Chong' 'SuiSha' 'WuxingJiazi' 'WuxingNaYear'
    #  'WuxingNaMonth' 'WuxingNaDay' 'MoonName' 'XingEast' 'XingWest' 'PengZu'
    #  'JianShen' 'TianGanDiZhiYear' 'TianGanDiZhiMonth' 'TianGanDiZhiDay'
    #  'LMonthName' 'LYear' 'LMonth' 'LDay' 'SolarTermName'
    date_list = series['GregorianDateTime'].split(' ')[0].split('-')
    series['GregorianDateTime'] = series['GregorianDateTime'].split(' ')[0]
    series['GYear'] = int(date_list[0])
    series['GMonth'] = int(date_list[1])
    series['GDay'] = int(date_list[2])
    week = get_week(series['GYear'], series['GMonth'], series['GDay'])
    if week == '6' or week == '7':
        series['is_weekend'] = 1
        series['is_weekday'] = 0
    else:
        series['is_weekend'] = 0
        series['is_weekday'] = 1
    series['Yi'] = series['Yi'].replace('.', ' ')
    series['Ji'] = series['Ji'].replace('.', ' ')
    series['Taishen'] = series['Taishen'].replace(',', '，')
    series.drop('IsJieJia', inplace=True)
    print(series['GregorianDateTime'])
    return series


if __name__ == '__main__':
    df = pd.read_csv('cp_calendar.csv', sep=';')
    df.drop('LunarShow', axis=1, inplace=True)
    df = df.apply(change_seg, axis=1)
    df.to_csv('cp_calendar.csv', index=False)
    df.to_pickle('cp_calendar.pkl')
