import requests
from bs4 import BeautifulSoup

url = "https://www.ammunitiondepot.com/603-bulk-9mm-ammo"

response = requests.get(url)

soup = BeautifulSoup(response.content, "lxml")

banner = soup.find('span', class_='base').text
items = soup.find_all('div', class_='product-item-details')
max_investment = 460

print(banner)
print("___________________________________________")
nine_mm = 59.95

for each in items:
    title = each.a.text
    rounds = each.find('span', class_='rounds-qty').text
    num_rounds = int(rounds[:-6])
    num_boxes = round(num_rounds/50)
    price = each.find('span', class_='price').text
    price_num = price[1:]
    flt = float(price_num)

    buy_after_tax = (flt * .0825) + flt
    box_cost = buy_after_tax/num_boxes

    if buy_after_tax < max_investment:
        print(f'*{title.lstrip()}*')
        print(rounds)
        print(price)
        print('')
        print(f'This order has {num_rounds} rounds. \n'
              f'That is a total of {num_boxes} boxes of 50 cartriges.\n'
              f'Your total investment on this item after is ${buy_after_tax:.2f}\n'
              f'If we divide your investment({buy_after_tax:.2f}) by the number of boxes({num_boxes})\n'
              f'...\n'
              f'We get ${box_cost:.2f}/Box of Ammo\n'
              f'That is a SGP of ${59.95-box_cost:.2f} per 50 Round box.\n'
              f'${(59.95-box_cost)/50:.2f} SGP per Round.\n'
              f'Our Total SGP for this item would be ${(nine_mm * num_boxes)-buy_after_tax:.2f}')
        print("___________________________________________")
