import requests
import json
import sys


class WikiApi:
    endpoint = "https://fr.wikipedia.org/w/api.php"
    headers = {
        'User-Agent': 'MyWikiBot/1.0 (https://mywebsite.com)'
    }
    search_params = {
        "format": "json",
        "action": "query",
        "list": "search",
        "srsearch": "cats",  
        "srlimit": "3",
        "prop": "extracts|info|extracts",
        "exintro": "1",
        "explaintext": "1"
    }

    def __init__(self, search=None):
        if search is None:
            print("You must add a keyword or topic for search.\n")
            return
        if isinstance(search, str) and search.strip():
            self.filename = "_".join(search.split()) + ".wiki"
            self.search_params['srsearch'] = search.lower()
        else:
            print("You must specify something to search.\n")
            return
        
    def search(self):
        res = requests.get(self.endpoint, params=self.search_params, headers=self.headers)
        if not res.ok:
            print("Error: Status code %s (%s)" % (res.status_code, res.reason))
            return None
        return res.json()

    def get_page_extract(self, pageid):
        params = {
            "format": "json",
            "action": "query",
            "prop": "extracts",
            "exintro": True,
            "explaintext": True,
            "pageids": pageid
        }
        res = requests.get(self.endpoint, params=params, headers=self.headers)
        if not res.ok:
            print("error in page fetvhing \n")
        data = res.json()
        return data["query"]["pages"][str(pageid)]["extract"]
        


if __name__ == "__main__":
    # if len(sys.argv) == 2:
    #     test = WikiApi(sys.argv[1]).search()

    #     if len(test["query"]["search"]) == 0:
    #         print("no rusolt fro wiki ")
    #     else:
    #         print(json.dumps(test["query"]["search"][0]["pageid"], indent=4))
    #     page = WikiApi("chocolatine").get_page_extract(test["query"]["search"][0]["pageid"])
    #     print(page)
    # else:
    #     print("ERRor the correct : python request_wikipedia.py keyword")
    test = WikiApi(sys.argv[1]).search()
    for el in test["query"]["search"]:
        print(json.dumps(el["pageid"],indent=4))
    print("=========================================================")  
    print(json.dumps(test, indent=4))

        
