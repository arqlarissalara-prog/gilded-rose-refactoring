from gilded_rose.item_updater import AtualizadorDeItem
from gilded_rose.constants import QUALIDADE_MINIMA


class AtualizadorNormal(AtualizadorDeItem):
    """Atualiza itens normais.
    
    A qualidade diminui em 1 por dia.
    Após a data de validade (sell_in < 0), a qualidade degrada em 2 por dia.
    A qualidade nunca fica negativa.
    """

    def atualizar(self, item):
        item.sell_in -= 1
        perda = 2 if item.sell_in < 0 else 1
        item.quality = max(item.quality - perda, QUALIDADE_MINIMA)