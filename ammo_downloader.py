import requests


def fetch_html() -> bytes:
    url = "https://www.ammunitiondepot.com/603-bulk-9mm-ammo"
    response = requests.get(url)
    return response.content


def main():
    html = fetch_html().decode('utf8')
    with open("fixtures/9mm.html", "w") as f:
        f.write(html)


if __name__ == "__main__":
    main()
