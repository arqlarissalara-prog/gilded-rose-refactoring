from gilded_rose import GildedRose, Item


def test_sulfuras_never_changes_sell_in_or_quality():
    item = Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80)
    gilded_rose = GildedRose([item])
    gilded_rose.att()
    assert item.sell_in == 0
    assert item.quality == 80


def test_sulfuras_maintains_quality_with_negative_sell_in():
    item = Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80)
    gilded_rose = GildedRose([item])
    gilded_rose.att()
    assert item.sell_in == -1
    assert item.quality == 80