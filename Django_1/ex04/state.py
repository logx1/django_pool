import sys

def statex(city):
    states = {
        "Oregon" : "OR",
        "Alabama" : "AL",
        "New Jersey": "NJ",
        "Colorado" : "CO"
        }
    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
        }
    # print(capital_cities)
    # print(capital_cities.items())
    for key, val in capital_cities.items():
        if val == city:
            # print(key)
            for newkey,newval in states.items():
                if key == newval:
                    print(newkey)
    

if __name__ == "__main__":
    if len(sys.argv) == 2:
        statex(sys.argv[1])