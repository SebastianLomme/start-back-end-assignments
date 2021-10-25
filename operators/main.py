# Do not modify these lines
__winc_id__ = "d0d3cdcefbb54bc980f443c04ab3a9eb"
__human_name__ = "operators"

# Add your code after this line

spain_most_spoken_language = "Spanish"
switzerland_most_spoken_language = "German"

print(spain_most_spoken_language == switzerland_most_spoken_language)

spain_most_prevalent_religion = "Roman Catholic"
switzerland_most_prevalent_religion = "Roman Catholic"

print(spain_most_prevalent_religion == switzerland_most_prevalent_religion)

name_length_capital_spain = len("Madrid")
name_length_capital_switzerland = len("Bern")

print(name_length_capital_spain != name_length_capital_switzerland)

spain_gdp = 1778
switzerland_gdp = 580
print(switzerland_gdp > spain_gdp)

population_growth_spain = 0.67
population_growth_switzerland = 0.66
print(population_growth_spain < 1 and population_growth_switzerland < 1)

population_count_spain = 50
population_count_switzerland = 8.4

print(population_count_spain > 10 or population_count_switzerland > 10)
print((population_count_spain > 10) ^ (population_count_switzerland > 10))
