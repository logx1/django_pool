import sys
import time
from bs4 import BeautifulSoup
import requests

def get_first_link(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    try:
        response = requests.get(url, headers=headers, allow_redirects=True)
        if response.status_code != 200:
            print(f"Error fetching {url}: {response.status_code} {response.reason}")
            return None, None

        soup = BeautifulSoup(response.text, 'html.parser')
        title_tag = soup.find(id="firstHeading")
        title = title_tag.text.strip() if title_tag else "Unknown"

        content_div = soup.find(id="mw-content-text")
        if not content_div:
            return title, None

        content_div = content_div.find(class_="mw-parser-output")
        if not content_div:
            return title, None


        for paragraph in content_div.find_all('p'):
            text = paragraph.get_text()
            for link in paragraph.find_all('a', recursive=False):
                href = link.get('href')
                if href and href.startswith('/wiki/') and not href.startswith('/wiki/Special:') and not href.startswith('/wiki/Help:'):
                    link_text = link.get_text()
                    start_index = text.find(link_text)
                    if start_index != -1:
                        open_parentheses = text[:start_index].count('(') - text[:start_index].count(')')
                        if open_parentheses > 0:
                            continue

                    if link.find_parent('i') or link.find_parent('em'):
                        continue

                    return title, "https://en.wikipedia.org" + href

        return title, None

    except requests.RequestException as e:
        print(f"Request error: {e}")
        return None, None


def run():
    if len(sys.argv) != 2:
        print("Usage: python3 roads_to_philosophy.py <search_term>")
        sys.exit(1)

    search_term = sys.argv[1]
    search_url = f"https://en.wikipedia.org/wiki/{search_term.replace(' ', '_')}"
    visited = []
    steps = 0
    current_url = search_url

    while True:
        title, first_link = get_first_link(current_url)

        if not title:
            print("Error fetching page.")
            break

        if title.lower() in (t.lower() for t in visited):
            print("It leads to an infinite loop!")
            break

        visited.append(title)
        print(title)

        if title.lower() == "philosophy":
            print(f"{len(visited) - 1} roads from {search_term} to philosophy!")
            break

        if not first_link:
            print("It's a dead end!")
            break

        current_url = first_link
        steps += 1
        # time.sleep(0.5)

if __name__ == "__main__":
    run()
