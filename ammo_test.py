from decimal import Decimal

from ammo_scrape import fetch_html, parse_ammos, Ammo


def test_parse_ammos():
    html = fetch_html(use_fixture=True)
    ammos = parse_ammos(html)
    assert ammos == EXPECTED_FIXTURE


EXPECTED_FIXTURE = [
    Ammo(title='USC Ammo Remanufactured 9mm 124 Grain FMJ (1000 Round)', rounds=1000, price=Decimal('649.99')),
    Ammo(title='US Cartridge 9mm 124 Grain Bonded UHP', rounds=200, price=Decimal('224.99')),
    Ammo(title='Federal Premium HST 9mm 124 Grain +P JHP RTAC Tactical Sling Combo', rounds=250, price=Decimal('401.39')),
    Ammo(title='Federal Premium HST 9mm 124 Grain +P JHP RTAC Small Range Bag Combo', rounds=400, price=Decimal('635.14')),
    Ammo(title='Federal Premium HST 9mm 124 Grain +P JHP RTAC Assault Pack Combo', rounds=400, price=Decimal('635.89')),
    Ammo(title='Blazer Brass 9mm 115 Grain FMJ RTAC Tactical Sling Combo', rounds=350, price=Decimal('299.96')),
    Ammo(title='Blazer Brass 9mm 115 Grain FMJ RTAC Assault Pack Combo', rounds=500, price=Decimal('401.04')),
    Ammo(title='Blazer Brass 9mm 115 Grain FMJ RTAC Small Range Bag Combo', rounds=500, price=Decimal('428.25')),
    Ammo(title='US Cartridge 9mm 124 Grain Bonded UHP RTAC Tactical Sling Combo', rounds=200, price=Decimal('259.61')),
]
