class Item:
    """Representa um item do inventário da loja.

       Esta classe é fornecida pelo enunciado do projeto e não deve ser
       modificada — os atributos name, sell_in e quality são usados pelos
       testes de caracterização e pelas regras de negócio originais.

       Atributos:
           name (str): nome do item, usado para determinar qual regra
               de atualização se aplica a ele.
           sell_in (int): número de dias restantes para vender o item.
           quality (int): o quão valioso o item é (geralmente entre 0 e 50,
               exceto o item lendário Sulfuras, que é fixo em 80).
       """
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)