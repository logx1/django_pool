import sys

def clean_list(unclean_list):
    cleaned = []
    for item in unclean_list:
        stripped = item.strip()
        if stripped != "":
            cleaned.append(stripped)
    return cleaned


def all_in(words):
    if ",," in words:
        return
    listt = words.split(",")
    listt = clean_list(listt)
    if not listt:
        return

    states = {
        "Oregon": "OR",
        "Alabama": "AL",
        "New Jersey": "NJ",
        "Colorado": "CO"
    }

    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
    }

    new_dic = {}
    for key, val in states.items():
        new_dic[key.lower()] = capital_cities[val].lower()

    reverse_dic = {v: k for k, v in new_dic.items()}

    for word in listt:
        w = word.strip().lower()

        if w in new_dic:
            print(f"{word.strip()} is a state of which the capital is {new_dic[w].title()}")
        elif w in reverse_dic:
            print(f"{word.strip()} is the capital of {reverse_dic[w]}")
        else:

            print(f"{word.strip()} is neither a capital city nor a state")


if __name__ == "__main__":
    if len(sys.argv) == 2:
        all_in(sys.argv[1])
