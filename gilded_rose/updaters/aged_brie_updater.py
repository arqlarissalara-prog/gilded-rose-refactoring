from gilded_rose.item_updater import AtualizadorDeItem
from gilded_rose.constants import QUALIDADE_MAXIMA


class AtualizadorAgedBrie(AtualizadorDeItem):
    """Aged Brie aumenta de qualidade à medida que envelhece.
    
    Aumenta 1 por dia antes de vencer.
    Aumenta 2 por dia após a data de validade.
    A qualidade nunca passa de 50.
    """

    def atualizar(self, item):
        item.sell_in -= 1
        ganho = 2 if item.sell_in < 0 else 1
        item.quality = min(item.quality + ganho, QUALIDADE_MAXIMA)