import requests
from bs4 import BeautifulSoup

URL = "https://en.wikipedia.org/wiki/Python_(programming_language)"


def get_h2_headers(url):
    request_headers = {
        "User-Agent": (
            "PythonCourseHeadingScraper/1.0 "
            "(https://github.com/kimamovic21/udemy-python-course-hc)"
        )
    }

    try:
        response = requests.get(url, headers=request_headers, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Failed to fetch page: \n {e}")
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    h2_tags = soup.find_all("h2")
    print(h2_tags)
    headers = []
    for tag in h2_tags:
        header_text = tag.get_text(strip=True)
        if header_text and header_text.lower() != "contents":
            headers.append(header_text)
    print(headers)


get_h2_headers(URL)
