from model.place import Place


def place_from_row(row: tuple) -> Place:
    place = Place()
    place.id = row[0]
    place.name = row[1]
    return place

def row_from_place(place: Place) -> tuple:
    row = (place.id, place.name)
    return row
