from gilded_rose.item import Item
from gilded_rose.updaters.conjured_updater import AtualizadorConjurado


def test_conjurado_perde_dois_de_qualidade_por_dia():
    item = Item(name="Conjured Mana Cake", sell_in=5, quality=10)
    AtualizadorConjurado().atualizar(item)
    assert item.sell_in == 4
    assert item.quality == 8


def test_conjurado_perde_quatro_de_qualidade_apos_vencer():
    item = Item(name="Conjured Mana Cake", sell_in=0, quality=10)
    AtualizadorConjurado().atualizar(item)
    assert item.sell_in == -1
    assert item.quality == 6


def test_conjurado_qualidade_nunca_fica_negativa():
    item = Item(name="Conjured Mana Cake", sell_in=5, quality=1)
    AtualizadorConjurado().atualizar(item)
    assert item.quality == 0


def test_conjurado_qualidade_nunca_fica_negativa_apos_vencer():
    item = Item(name="Conjured Mana Cake", sell_in=0, quality=2)
    AtualizadorConjurado().atualizar(item)
    assert item.quality == 0