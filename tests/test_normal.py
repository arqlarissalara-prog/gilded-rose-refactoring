from gilded_rose.item import Item
from gilded_rose.updaters.normal_updater import AtualizadorNormal


def test_normal_item_decreases_sell_in_and_quality_by_one():
    item = Item(name="+5 Dexterity Vest", sell_in=10, quality=20)
    atualizador = AtualizadorNormal()
    atualizador.atualizar(item)
    assert item.sell_in == 9
    assert item.quality == 19


def test_normal_item_quality_degrades_twice_as_fast_after_sell_in():
    item = Item(name="+5 Dexterity Vest", sell_in=0, quality=20)
    atualizador = AtualizadorNormal()
    atualizador.atualizar(item)
    assert item.sell_in == -1
    assert item.quality == 18


def test_normal_item_quality_never_negative():
    item = Item(name="+5 Dexterity Vest", sell_in=5, quality=0)
    atualizador = AtualizadorNormal()
    atualizador.atualizar(item)
    assert item.sell_in == 4
    assert item.quality == 0