from gilded_rose.item import Item
from gilded_rose.updaters.sulfuras_updater import AtualizadorSulfuras


def test_sulfuras_never_changes_sell_in_or_quality():
    item = Item(name="Sulfuras, Hand of Ragnaros", sell_in=10, quality=80)
    atualizador = AtualizadorSulfuras()
    atualizador.atualizar(item)
    assert item.sell_in == 10
    assert item.quality == 80


def test_sulfuras_negative_sell_in():
    item = Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80)
    atualizador = AtualizadorSulfuras()
    atualizador.atualizar(item)
    assert item.sell_in == -1
    assert item.quality == 80