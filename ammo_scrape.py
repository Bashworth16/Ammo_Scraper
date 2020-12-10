from collections import namedtuple
from typing import List
import requests
from bs4 import BeautifulSoup


MAX_INVESTMENT = 1000
# TODO: Change to decimal
SALE_PRICE_9MM = 59.95


def fetch_html() -> bytes:
    url = "https://www.ammunitiondepot.com/603-bulk-9mm-ammo"
    response = requests.get(url)
    return response.content


Ammo = namedtuple('Ammos', 'title rounds price')


def parse_ammos(h: bytes) -> List[Ammo]:
    soup = BeautifulSoup(h, "html.parser")
    ammos = []
    # banner = soup.find('span', class_='base').text
    title = soup.find("a", class_="product-item-link").text.lstrip()
    round = soup.find('span', class_='rounds-qty').text
    price = soup.find('span', class_='price').text
    items = soup.find_all('div', class_='product-item-details')
    for each in items:
        unit = Ammo(title=title, rounds=round, price=price)
        ammos.append(unit)
    return ammos

def render_ammos(ammos: List[Ammo]) -> str:
    item_number = 0
    for each in ammos:
        price_num = each.price[1:]
        flt = float(price_num)
        buy_after_tax = (flt * .0825) + flt
        print(item_number, buy_after_tax)
        item_number += 1

print(parse_ammos(fetch_html()))
print(render_ammos(parse_ammos(fetch_html())))

def mute_rounds(r):
    Ammos.rounds = r.find('span', class_='rounds-qty').text
    return int(Ammos.rounds[:-6])

def profit_cal(c, e):
    num_rounds = mute_rounds(e)
    num_boxes = round(num_rounds / 50)
    bat = mute_price(e)
    box_cost = bat / num_boxes
    if bat < MAX_INVESTMENT:
        print(f'{c}. {parse_ammos(e)}')
        print_rounds(e)
        print_price(e)
        print('')
        print(f'This order has {num_rounds} rounds. \n'
              f'That is a total of {num_boxes} boxes of 50 cartridges.\n'
              f'Your total investment on this item after is ${bat:.2f}\n'
              f'If we divide your investment({bat:.2f}) by the number of boxes({num_boxes})\n'
              f'...\n'
              f'We get ${box_cost:.2f}/Box of Ammo\n'
              f'That is a SGP of ${59.95 - box_cost:.2f} per 50 Round box.\n'
              f'${(59.95 - box_cost) / 50:.2f} SGP per Round.\n'
              f'Our Total SGP for this item would be ${(SALE_PRICE_9MM * num_boxes) - bat:.2f}')
        print("___________________________________________")


def main():
    number = 1
    html = get_9mm_content()

    parse_banner(soup)

    print("___________________________________________")
    for each in items:
        profit_cal(number, each)
        number += 1

# def main():
#     html = get_9mm_content()
#     ammos = parse_ammos(html)
#     rendered = render_ammos(ammos)
#    print(rendered)


if __name__ == "__main__":
    main()
