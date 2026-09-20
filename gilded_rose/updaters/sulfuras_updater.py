from gilded_rose.item_updater import AtualizadorDeItem


class AtualizadorSulfuras(AtualizadorDeItem):
    """Sulfuras é um item lendário: nunca tem de ser vendido nem perde qualidade."""

    def atualizar(self, item):
        pass