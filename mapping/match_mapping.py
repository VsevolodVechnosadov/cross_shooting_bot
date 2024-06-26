from model.match import Match
from utils.datetime_util import datetime_to_int, int_to_datetime


def match_from_row(row: tuple) -> Match:
    match = Match()
    match.id = row[0]
    match.start_time = datetime_to_int(row[1])
    match.duration = datetime_to_int(row[2])
    match.place_id = row[3]
    match.group_id = row[4]
    match.genre_id = row[5]
    match.is_loneliness_friendly = row[6]
    return match

def row_from_match(match: Match) -> tuple:
    int_start_time = int_to_datetime(match.start_time)
    int_duration = int_to_datetime(match.duration)
    row = (
        int_start_time,
        int_duration,
        match.place_id,
        match.group_id,
        match.genre_id,
        match.is_loneliness_friendly
    )
    return row
