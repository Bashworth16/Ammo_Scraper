from decimal import Decimal

from ammo_scrape import fetch_html, \
    parse_ammos, \
    Ammo, parse_rounds, \
    parse_price, \
    get_boxes, \
    price_per_box, \
    after_tax, \
    sales_gross_profit_per_box, \
    get_sgp_round, \
    render_ammo, \
    render_ammos


def test_parse_ammos():
    html = fetch_html(use_fixture=True)
    ammos = parse_ammos(html)
    assert ammos == EXPECTED_FIXTURE


def test_parse_rounds():
    rounds = parse_rounds("500rounds")
    assert rounds == 500


def test_parse_price():
    price = parse_price("$500")
    assert price == 500


def test_get_boxes():
    boxes = get_boxes(EXPECTED_FIXTURE[0])
    assert boxes == 20


def test_price_per_box():
    res = price_per_box(EXPECTED_FIXTURE[0])
    assert res == Decimal("35.18")


def test_after_tax():
    res = after_tax(EXPECTED_FIXTURE[0])
    assert res == Decimal("703.61")


def test_sales_gross_profit():
    res = sales_gross_profit_per_box(EXPECTED_FIXTURE[0])
    assert res == Decimal('24.77')


def test_get_sgp_round():
    res = get_sgp_round(EXPECTED_FIXTURE[0])
    assert res == Decimal('0.50')


def test_render_ammo():
    res = render_ammo(EXPECTED_FIXTURE[0]).split("\n")
    assert res == [
        'USC Ammo Remanufactured 9mm 124 Grain FMJ (1000 Round)',
        '1000',
        '$649.99',
        'This order has 1000 rounds.',
        'That is a total of 20 boxes of 50 cartridges.',
        'Your total investment on this item after is $703.61',
        'If we divide your investment(703.61) by the number of boxes(20)',
        '...',
        'We get $35.18/Box of Ammo',
        'That is a SGP of $24.77 per 50 Round box.',
        '$0.50 SGP per Round.',
        'Our Total SGP for this item would be $495.39',
        '___________________________________________'
    ]

# .split() makes it easier to read.
def test_render_ammos():
    res = render_ammos(EXPECTED_FIXTURE[0:1]).split()
    assert res == ['1,','USC','Ammo','Remanufactured','9mm','124','Grain','FMJ','(1000','Round)','1000', '$649.99', 'This', 'order','has', '1000', 'rounds.', 'That', 'is', 'a', 'total', 'of', '20', 'boxes', 'of', '50', 'cartridges.', 'Your', 'total', 'investment', 'on', 'this', 'item', 'after', 'is', '$703.61', 'If', 'we', 'divide', 'your', 'investment(703.61)', 'by', 'the', 'number', 'of', 'boxes(20)', '...', 'We', 'get', '$35.18/Box', 'of', 'Ammo', 'That', 'is', 'a', 'SGP', 'of', '$24.77', 'per', '50', 'Round', 'box.', '$0.50', 'SGP', 'per', 'Round.', 'Our', 'Total', 'SGP', 'for', 'this', 'item', 'would', 'be', '$495.39', '___________________________________________']


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
