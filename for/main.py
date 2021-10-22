from typing_extensions import Protocol
from helpers import get_countries
from operator import itemgetter


""" Leave this untouched. Wincpy uses it to match this assignment with the
tests it runs. """
__winc_id__ = "c545bc87620d4ced81cbddb8a90b4a51"
__human_name__ = "for"


""" Write your functions here. """


def shortest_names(list_names):
    short_name = 100
    new_list = []
    for name in list_names:
        if len(name) < short_name:
            short_name = len(name)
    for name in list_names:
        if len(name) == short_name:
            new_list.append(name)
    return new_list


def most_vowels(list_names):
    list = []
    sort_list = []
    vowels = ["a", "e", "i", "o", "u"]
    for name in list_names:
        count = 0
        for x in name.lower():
            if x in vowels:
                count += 1
        list.append([name, count])
    list = sorted(list, key=itemgetter(1), reverse=True)
    for item in list:
        sort_list.append(item[0])
    return sort_list[0:3]


# def alphabet_set(list):
#     set_letters = []
#     list_counties = []
#     for country in list:
#         # print(countries)
#         for char in country.lower():
#             # print(char)
#             if char not in set_letters:
#                 set_letters.append(char)
#                 if country not in list_counties:
#                     list_counties.append(country)
#     set_letters.sort()
#     return list_counties


def alphabet_set(list):
    set_letters = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
    ]
    list_countries = []
    sort_list_countries = []
    for country in list:
        count = 0
        for char in country.lower():
            if char in set_letters:
                count += 1
        sort_list_countries.append([country, count])
    sort_list_countries = sorted(sort_list_countries, key=itemgetter(1), reverse=True)
    for country in sort_list_countries:
        for char in country[0].lower():
            if char in set_letters:
                set_letters.remove(char)
                if country[0] not in list_countries:
                    list_countries.append(country[0])
            elif len(set_letters) == 0:
                break
    set_letters.sort()
    return list_countries


# This block is only run if this file is the entrypoint; python main.py
# It is not run if it is imported as a module: `from main import *`
if __name__ == "__main__":
    countries = get_countries()

    """ Write the calls to your functions here. """
    shortest_names(countries)
    most_vowels(countries)
    print(alphabet_set(countries))
    print(len(alphabet_set(countries)))
