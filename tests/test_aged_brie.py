from gilded_rose.item import Item
from gilded_rose.updaters.aged_brie_updater import AtualizadorAgedBrie


def test_aged_brie_increases_quality_by_one():
    item = Item(name="Aged Brie", sell_in=10, quality=20)
    atualizador = AtualizadorAgedBrie()
    atualizador.atualizar(item)
    assert item.sell_in == 9
    assert item.quality == 21


def test_aged_brie_increases_quality_twice_as_fast_after_sell_in():
    item = Item(name="Aged Brie", sell_in=0, quality=20)
    atualizador = AtualizadorAgedBrie()
    atualizador.atualizar(item)
    assert item.sell_in == -1
    assert item.quality == 22


def test_aged_brie_quality_never_exceeds_fifty():
    item = Item(name="Aged Brie", sell_in=5, quality=50)
    atualizador = AtualizadorAgedBrie()
    atualizador.atualizar(item)
    assert item.sell_in == 4
    assert item.quality == 50