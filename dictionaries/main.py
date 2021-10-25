from helpers import get_countries

__winc_id__ = "25a8041d2d5e4e3ab61ab1be43bfb863"
__human_name__ = "dictionaries"


def create_passport(name, date_birth, place_birth, height, nationality):
    passport = {
        "name": name,
        "date_of_birth": date_birth,
        "place_of_birth": place_birth,
        "height": height,
        "nationality": nationality,
    }
    return passport


def add_stamp(passport, country):
    if "stamps" not in passport:
        passport["stamps"] = []

    if country not in passport["stamps"] and country != passport["nationality"]:
        passport["stamps"].append(country)
    return passport


def check_passport(passport, country, countries_allowed, countries_not_allowed):
    if country in countries_allowed[passport["nationality"]]:
        if country in countries_not_allowed:
            if passport["nationality"] in countries_not_allowed[country]:
                return False
            if "stamps" in passport:
                for stamp in passport["stamps"]:
                    if stamp in countries_not_allowed[country]:
                        return False
        return add_stamp(passport, country)
    return False
