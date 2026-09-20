"""Testes de integracao para a classe principal GildedRose."""

import pytest
from gilded_rose.gilded_rose import GildedRose
from gilded_rose.item import Item


def test_gilded_rose_atualiza_lista_diversa_de_itens():
    """Garante que a classe GildedRose orquestra a atualizacao de diferentes tipos de itens."""
    itens = [
        Item(name="Item Normal", sell_in=10, quality=20),
        Item(name="Aged Brie", sell_in=5, quality=10),
        Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=8, quality=25),
        Item(name="Conjured Mana Cake", sell_in=3, quality=6),
    ]

    loja = GildedRose(itens)
    loja.update_quality()

    # Normal (-1 / -1)
    assert itens[0].sell_in == 9
    assert itens[0].quality == 19

    # Aged Brie (-1 / +1)
    assert itens[1].sell_in == 4
    assert itens[1].quality == 11

    # Sulfuras (imutável)
    assert itens[2].sell_in == 0
    assert itens[2].quality == 80

    # Backstage (entre 6 e 10 dias -> +2)
    assert itens[3].sell_in == 7
    assert itens[3].quality == 27

    # Conjured (-1 / -2)
    assert itens[4].sell_in == 2
    assert itens[4].quality == 4


def test_gilded_rose_identifica_item_conjurado_pelo_prefixo():
    """Verifica se qualquer item contendo 'Conjured' no nome utiliza a regra de Conjurado."""
    itens = [Item(name="Conjured Dark Blade", sell_in=2, quality=10)]
    loja = GildedRose(itens)
    loja.update_quality()

    assert itens[0].sell_in == 1
    assert itens[0].quality == 8