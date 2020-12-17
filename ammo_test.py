# NOTE: Research pytest "https://docs.pytest.org/en/latest/"

from ammo_scrape import parse_ammos
from ammo_scrape import fetch_html


def test_parse_ammos_true():
    html = fetch_html(True)
    ammos = parse_ammos(html)
    assert ammos == parse_ammos(fetch_html(False))
