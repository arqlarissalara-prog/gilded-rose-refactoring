from abc import ABC, abstractmethod


class AtualizadorDeItem(ABC):
    """Classe base: toda regra de atualização de item implementa atualizar()."""

    @abstractmethod
    def atualizar(self, item):
        """Atualiza sell_in e quality de um item, seguindo suas regras próprias."""
        pass