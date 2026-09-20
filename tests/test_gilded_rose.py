from gilded_rose.gilded_rose import GildedRose
from gilded_rose.item import Item


def test_gilded_rose_updates_normal_item():
    items = [Item(name="Normal Item", sell_in=5, quality=10)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].sell_in == 4
    assert items[0].quality == 9


def test_gilded_rose_updates_aged_brie():
    items = [Item(name="Aged Brie", sell_in=2, quality=0)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].sell_in == 1
    assert items[0].quality == 1


def test_gilded_rose_updates_sulfuras():
    items = [Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].sell_in == 0
    assert items[0].quality == 80


def test_gilded_rose_updates_backstage_passes():
    items = [Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].sell_in == 14
    assert items[0].quality == 21


def test_gilded_rose_updates_conjured_item():
    items = [Item(name="Conjured Mana Cake", sell_in=3, quality=6)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].sell_in == 2
    assert items[0].quality == 4


def test_gilded_rose_updates_item_with_conjured_in_name():
    items = [Item(name="Conjured Dark Blade", sell_in=3, quality=10)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].sell_in == 2
    assert items[0].quality == 8


def test_item_string_representation():
    item = Item(name="Test Item", sell_in=5, quality=10)
    assert str(item) == "Test Item, 5, 10"
