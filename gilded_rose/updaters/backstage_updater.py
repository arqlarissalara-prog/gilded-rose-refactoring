from gilded_rose.item_updater import AtualizadorDeItem
from gilded_rose.constants import QUALIDADE_MAXIMA, QUALIDADE_MINIMA


class AtualizadorBackstage(AtualizadorDeItem):
    """Ingressos de backstage ganham qualidade conforme o show se aproxima,
    e não valem nada depois que o show acontece."""

    def atualizar(self, item):
        item.sell_in -= 1

        if item.sell_in < 0:
            item.quality = QUALIDADE_MINIMA
            return

        ganho = self._calcular_ganho_qualidade(item.sell_in)
        item.quality = min(item.quality + ganho, QUALIDADE_MAXIMA)

    def _calcular_ganho_qualidade(self, dias_restantes):
        if dias_restantes < 5:
            return 3
        if dias_restantes < 10:
            return 2
        return 1