from gilded_rose import GildedRose, Item


def test_aged_brie_increases_quality_by_one_before_sell_in():
    item = Item(name="Aged Brie", sell_in=2, quality=0)
    gilded_rose = GildedRose([item])
    gilded_rose.att()
    assert item.sell_in == 1
    assert item.quality == 1


def test_aged_brie_increases_quality_twice_as_fast_after_sell_in():
    item = Item(name="Aged Brie", sell_in=0, quality=10)
    gilded_rose = GildedRose([item])
    gilded_rose.att()
    assert item.sell_in == -1
    assert item.quality == 12


def test_aged_brie_quality_never_exceeds_fifty():
    item = Item(name="Aged Brie", sell_in=5, quality=50)
    gilded_rose = GildedRose([item])
    gilded_rose.att()
    assert item.quality == 50


def test_aged_brie_quality_caps_at_fifty_after_sell_in():
    item = Item(name="Aged Brie", sell_in=-1, quality=49)
    gilded_rose = GildedRose([item])
    gilded_rose.att()
    assert item.quality == 50