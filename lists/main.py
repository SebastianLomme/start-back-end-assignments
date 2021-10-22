# Do not modify these lines
__winc_id__ = "6eb355e1a60f48a28a0bbbd0c88d9ab4"
__human_name__ = "lists"

# Add your code after this line


def alphabetical_order(list):
    list.sort()
    return list


def won_golden_globe(film):
    won_films = [
        "Jaws",
        "Star Wars: Episode IV – A New Hope",
        "E.T. the Extra-Terrestrial",
        "Memoirs of a Geisha",
    ]
    won_films = [x.lower() for x in won_films]
    return film.lower() in won_films


def remove_toto_albums(albums):
    albums_toto = [
        "Fahrenheit",
        "The Seventh One",
        "Toto XX",
        "Falling in Between",
        "35th Anniversary – Live in Poland",
        "Toto XIV",
        "Old Is New",
        "40 Tours Around the Sun",
        "With a Little Help from My Friends",
    ]
    filtered = []
    for album in albums:
        if album not in albums_toto:
            filtered.append(album)
    print(filtered)
    return filtered

