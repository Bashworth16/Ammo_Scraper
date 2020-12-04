from collections import namedtuple

import requests
from bs4 import BeautifulSoup


MAX_INVESTMENT = 1000
# TODO: Change to decimal
SALE_PRICE_9MM = 59.95


def get_9mm_content():
    url = "https://www.ammunitiondepot.com/603-bulk-9mm-ammo"
    response = requests.get(url)
    return response.content


Ammos = namedtuple('Ammos', 'banner title rounds price ')

# Return a list of


def parse_banner(x):
    Ammos.banner = x.find('span', class_='base').text
    print(Ammos.banner)


def parse_ammos(e):
    Ammos.title = e.a.text
    return Ammos.title.lstrip()


def print_rounds(e):
    Ammos.rounds = e.find('span', class_='rounds-qty').text
    print(Ammos.rounds)


def print_price(e):
    price = e.find('span', class_='price').text
    print(price)


def mute_price(e):
    price = e.find('span', class_='price').text
    price_num = price[1:]
    flt = float(price_num)
    buy_after_tax = (flt * .0825) + flt
    return buy_after_tax


def mute_rounds(r):
    Ammos.rounds = r.find('span', class_='rounds-qty').text
    return int(Ammos.rounds[:-6])


def main():
    number = 1
    html = get_9mm_content()
    soup = BeautifulSoup(html, "html.parser")
    parse_banner(soup)
    items = soup.find_all('div', class_='product-item-details')
    print("___________________________________________")
    for each in items:
        num_rounds = mute_rounds(each)
        num_boxes = round(num_rounds/50)
        bat = mute_price(each)
        box_cost = bat / num_boxes
        if bat < MAX_INVESTMENT:
            print(f'{number}. {parse_ammos(each)}')
            print_rounds(each)
            print_price(each)
            print('')
            print(f'This order has {num_rounds} rounds. \n'
                  f'That is a total of {num_boxes} boxes of 50 cartridges.\n'
                  f'Your total investment on this item after is ${bat:.2f}\n'
                  f'If we divide your investment({bat:.2f}) by the number of boxes({num_boxes})\n'
                  f'...\n'
                  f'We get ${box_cost:.2f}/Box of Ammo\n'
                  f'That is a SGP of ${59.95-box_cost:.2f} per 50 Round box.\n'
                  f'${(59.95-box_cost)/50:.2f} SGP per Round.\n'
                  f'Our Total SGP for this item would be ${(SALE_PRICE_9MM * num_boxes) - bat:.2f}')
            print("___________________________________________")
            number = number + 1


if __name__ == "__main__":
    main()
