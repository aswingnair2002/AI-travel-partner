import urllib.parse


def get_google_maps_link(place, city):

    query = f"{place}, {city}"

    return (
        "https://www.google.com/maps/search/"
        + urllib.parse.quote(query)
    )