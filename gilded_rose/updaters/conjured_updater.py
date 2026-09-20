from gilded_rose.item_updater import AtualizadorDeItem
from gilded_rose.constants import QUALIDADE_MINIMA


class AtualizadorConjurado(AtualizadorDeItem):
    """Itens conjurados degradam a qualidade duas vezes mais rápido
    que itens normais, antes e depois de vencer."""

    def atualizar(self, item):
        item.sell_in -= 1

        perda = 4 if item.sell_in < 0 else 2
        item.quality = max(item.quality - perda, QUALIDADE_MINIMA)