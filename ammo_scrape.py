from decimal import Decimal
from typing import List, NamedTuple

import textwrap
import requests
from bs4 import BeautifulSoup

MAX_INVESTMENT = 1000
SALE_PRICE_9MM = Decimal('59.95')
USE_FIXTURE = True


def main():
    html = fetch_html(USE_FIXTURE)
    ammos = parse_ammos(html)
    rendered = render_ammos(ammos)
    print(rendered)


def fetch_html(use_fixture) -> bytes:
    if use_fixture:
        with open("fixtures/9mm.html", "br") as f:
            return f.read()
    else:
        url = "https://www.ammunitiondepot.com/603-bulk-9mm-ammo"
        response = requests.get(url)
        return response.content


# Ammo = namedtuple('Ammo', 'title rounds price')

class Ammo(NamedTuple):
    title: str
    rounds: int
    price: Decimal


def parse_ammos(h: bytes) -> List[Ammo]:
    soup = BeautifulSoup(h, "html.parser")
    ammos = []
    # banner = soup.find('span', class_='base').text

    items = soup.find_all('div', class_='product-item-details')
    for item in items:
        title = item.find("a", class_="product-item-link").text
        r = item.find('span', class_='rounds-qty').text
        price = item.find('span', class_='price').text
        unit = Ammo(title=title.strip(), rounds=parse_rounds(r), price=parse_price(price))
        ammos.append(unit)
    return ammos


def parse_rounds(rounds: str) -> int:
    return int(rounds[:-6])


def parse_price(price: str) -> Decimal:
    return round(Decimal(price[1:]), 2)


def get_boxes(ammo: Ammo) -> int:
    return round(ammo.rounds / 50)


def price_per_box(ammo: Ammo) -> Decimal:
    return round(Decimal(after_tax(ammo) / get_boxes(ammo)), 2)


def after_tax(ammo: Ammo) -> Decimal:
    return round(Decimal(ammo.price * Decimal("1.0825")), 2)


def sales_gross_profit_per_box(ammo: Ammo) -> Decimal:
    return round((SALE_PRICE_9MM - price_per_box(ammo)), 2)


def get_sgp_round(ammo: Ammo) -> Decimal:
    return round(Decimal((SALE_PRICE_9MM - price_per_box(ammo)) / 50), 2)


def render_ammo(ammo: Ammo) -> str:
    return textwrap.dedent(f"""
        {ammo.title}
        {ammo.rounds}
        ${ammo.price}
        This order has {ammo.rounds} rounds.
        That is a total of {get_boxes(ammo)} boxes of 50 cartridges.
        Your total investment on this item after is ${after_tax(ammo)}
        If we divide your investment({after_tax(ammo)}) by the number of boxes({get_boxes(ammo)})
        ...
        We get ${price_per_box(ammo)}/Box of Ammo
        That is a SGP of ${sales_gross_profit_per_box(ammo)} per 50 Round box.
        ${get_sgp_round(ammo)} SGP per Round.
        Our Total SGP for this item would be ${(SALE_PRICE_9MM * get_boxes(ammo)) - after_tax(ammo)}
        ___________________________________________
    """).strip()


def render_ammos(ammos: List[Ammo]) -> str:
    rendered = []
    for i, ammo in enumerate(ammos, 1):
        render = f'{i}, {render_ammo(ammo)}'
        rendered.append(render)
    return "\n".join(rendered)


if __name__ == "__main__":
    main()
