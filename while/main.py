from helpers import random_koala_fact

__winc_id__ = 'c0dc6e00dfac46aab88296601c32669f'
__human_name__ = 'while'

# This block is only executed if this script is run directly (python main.py)
# It is not run if you import this file as a module.
if __name__ == '__main__':
    (random_koala_fact())

def unique_koala_facts(int):
    # make een lijst van alle random fact die al eens geweest zijn
    # als fact nog niet is geweest print deze dan uit
    # alleen i plus als de fact nog niet is geweest
    past_list = []
    i = 0
    count = 0
    while i < int and count < 1000:
        fact = random_koala_fact()
        if  fact not in past_list:
            past_list.append(fact)
            i += 1
        else:
            count += 1
    return past_list

# unique_koala_facts(100)

def num_joey_facts():
    # tel het aantal unique fact met het woord joeys erin
    # laat de loop lopen totdat de eerste fact 10 keer is herhaald
    
    count_fact = 0
    fact_joeys = []
    while count_fact < 10:
        fact = random_koala_fact()
        if "joey" not in fact.lower():
            continue
        elif fact not in fact_joeys:
            fact_joeys.append(fact)
        elif fact_joeys[0] in fact_joeys:
            count_fact += 1
    else:
        print(count_fact)
        return len(fact_joeys)
        

def koala_weight():
    kg = 0
    while kg == 0:
        fact = random_koala_fact()
        if "kg" not in fact.lower():
            continue
        else:
            number= fact.find("kg")
            number_of_kg = int(fact[number-2:number])
            return number_of_kg


print(koala_weight())