import os
import requests
import time
from collections import deque
from urllib.parse import urljoin
from bs4 import BeautifulSoup

BASE_URL = "https://doc.rust-lang.org/std/"

OUTPUT_DIR = "./tmp/html"


def _main():
    start_url = urljoin(BASE_URL, "index.html")
    queue = deque([start_url])
    visited = {start_url}

    while queue:
        url = queue.popleft()
        print(url)
        response = requests.get(url)
        response.raise_for_status()

        path = os.path.join(OUTPUT_DIR, url[len(BASE_URL) :])
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "wb") as f:
            f.write(response.content)

        soup = BeautifulSoup(response.text, "html.parser")
        for link in soup.find_all("a"):
            href = link.get("href")
            if href is not None and href.endswith(".html"):
                href = urljoin(url, href)
                if href.startswith(BASE_URL) and href not in visited:
                    queue.append(href)
                    visited.add(href)

        time.sleep(0.1)


if __name__ == "__main__":
    _main()
