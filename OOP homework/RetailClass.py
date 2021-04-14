class Retail:
    def __init__(self, i, u, p):
        self.__item_desc = i
        self.__unit_inv = u
        self.__price = p

    def __str__(self):
        return (
            "\t\t"
            + str(self.__item_desc)
            + "\t\t\t\t"
            + str(self.__unit_inv)
            + "\t\t\t"
            + str(self.__price)
        )
