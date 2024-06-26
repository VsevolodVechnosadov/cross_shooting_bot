from model.genre import Genre


def genre_from_row(row: tuple) -> Genre:
    genre = Genre()
    genre.id = row[0]
    genre.name = row[1]
    return genre

def row_from_genre(genre: Genre) -> tuple:
    row = (genre.id, genre.name)
    return row
