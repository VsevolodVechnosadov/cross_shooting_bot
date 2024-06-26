import datetime


def datetime_to_int(current_datetime: datetime) -> int:
    format_str = '%Y%m%d%H%M%S'
    date_str = current_datetime.strftime(format_str)
    date_int = int(date_str)
    return date_int

def int_to_datetime(current_datetime: int) -> datetime:
    date_str = str(current_datetime)
    format_str = '%Y%m%d%H%M%S'
    date_obj = datetime.datetime.strptime(date_str, format_str)
    return date_obj

def int_to_str(int_datetime: int) -> str:
    primary_str = str(int_datetime)
    secondary_str = primary_str[:4] + '-' + primary_str[4:6] + '-' + primary_str[6:8] + ' ' + primary_str[8:10] + ':' + primary_str[10:12] + ':' + primary_str[12:len(primary_str)]
    return secondary_str
