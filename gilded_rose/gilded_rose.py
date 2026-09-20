"""Módulo principal do sistema Gilded Rose refatorado."""

from typing import List
from gilded_rose.item import Item
from gilded_rose.updaters.normal_updater import AtualizadorNormal
from gilded_rose.updaters.aged_brie_updater import AtualizadorAgedBrie
from gilded_rose.updaters.sulfuras_updater import AtualizadorSulfuras
from gilded_rose.updaters.backstage_updater import AtualizadorBackstage
from gilded_rose.updaters.conjured_updater import AtualizadorConjurado


class GildedRose:
    """Gerencia o inventário da loja Gilded Rose e atualiza os itens a cada dia.
    
    Aplica o padrão Strategy para delegar a regra de negócio específica de cada item
    para seu respectivo atualizador, respeitando os princípios SRP e OCP.
    """

    _ATUALIZADORES = {
        "Aged Brie": AtualizadorAgedBrie,
        "Sulfuras, Hand of Ragnaros": AtualizadorSulfuras,
        "Backstage passes to a TAFKAL80ETC concert": AtualizadorBackstage,
        "Conjured Mana Cake": AtualizadorConjurado,
    }

    def __init__(self, items: List[Item]):
        self.items = items

    def _obter_atualizador(self, item: Item):
        """Identifica e retorna a instância da estratégia adequada para o item."""
        # Se contiver 'Conjured' no nome ou for o item exato, usa o atualizador Conjurado
        if "Conjured" in item.name:
            return AtualizadorConjurado()
            
        classe_atualizador = self._ATUALIZADORES.get(item.name, AtualizadorNormal)
        return classe_atualizador()

    def update_quality(self) -> None:
        """Processa a passagem de um dia para todos os itens do inventário."""
        for item in self.items:
            atualizador = self._obter_atualizador(item)
            atualizador.atualizar(item)