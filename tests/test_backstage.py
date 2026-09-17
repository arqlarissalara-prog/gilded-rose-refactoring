from gilded_rose.item import Item
from gilded_rose.updaters.backstage_updater import AtualizadorBackstage


def test_backstage_aumenta_um_quando_faltam_mais_de_dez_dias():
    item = Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20)
    AtualizadorBackstage().atualizar(item)
    assert item.sell_in == 14
    assert item.quality == 21


def test_backstage_aumenta_dois_quando_faltam_dez_dias_ou_menos():
    item = Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=20)
    AtualizadorBackstage().atualizar(item)
    assert item.sell_in == 9
    assert item.quality == 22


def test_backstage_aumenta_dois_com_seis_dias():
    item = Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=6, quality=20)
    AtualizadorBackstage().atualizar(item)
    assert item.quality == 22


def test_backstage_aumenta_tres_quando_faltam_cinco_dias_ou_menos():
    item = Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=20)
    AtualizadorBackstage().atualizar(item)
    assert item.sell_in == 4
    assert item.quality == 23


def test_backstage_aumenta_tres_com_um_dia():
    item = Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=1, quality=20)
    AtualizadorBackstage().atualizar(item)
    assert item.quality == 23


def test_backstage_zera_apos_o_show():
    item = Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=0, quality=20)
    AtualizadorBackstage().atualizar(item)
    assert item.sell_in == -1
    assert item.quality == 0


def test_backstage_qualidade_nunca_passa_de_cinquenta():
    item = Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49)
    AtualizadorBackstage().atualizar(item)
    assert item.quality == 50


def test_backstage_qualidade_limitada_a_cinquenta_perto_da_data():
    item = Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=3, quality=48)
    AtualizadorBackstage().atualizar(item)
    assert item.quality == 50