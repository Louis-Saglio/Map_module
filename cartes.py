class Case:

    def __init__(self, value, owning_map, coordinates):
        self.value = value
        self.owning_map = owning_map
        self.coordinates = coordinates
        self.border = self.set_position()

    def __str__(self):
        return str(self.value)

    def set_position(self):
        l, h = self.coordinates
        return {
            "is_top": True if h == 0 else False,
            "is_left": True if l == 0 else False,
            "is_bottom": True if h == self.owning_map.height - 1 else False,
            "is_right": True if l == self.owning_map.width - 1 else False
        }


class Map:

    def __init__(self, width, height, filling='M', border='B'):
        self.width = width
        self.height = height
        self.border_type = border
        self.filling_type = filling
        self.map = self.create_map()

    def __iter__(self):
        iterator = []
        for h in range(self.height):
            for l in range(self.width):
                iterator.append(self[l, h])
        return iter(iterator)

    def __getitem__(self, pos):
        l, h = pos
        return self.map[l][h]

    def __setitem__(self, key, value):
        index1, index2 = key
        self.map[index1][index2] = Case(value, self, key)

    def __str__(self):
        rep = ''
        for case in self:
            rep += str(case.value) + ' ' + ('\n' if case.border["is_right"] else '')
        return rep

    def create_map(self):
        return [[Case(self.filling_type, self, (l, h)) for h in range(self.height)] for l in range(self.width)]

    def is_border_position(self, pos):
        l, h = pos
        return h == (self.height - 1) or (h == 0) or (l == self.width - 1) or (l == 0)

    def create_border(self):
        for case in self:
            if self.is_border_position(case.coordinates):
                self[case.coordinates] = Case(self.border_type, self, case.coordinates)

    @staticmethod
    def clear():
        # todo executer "cls" ou "clear" en fonction de l'os
        from os import system
        system("cls")


if __name__ == '__main__':
    # todo tester le module avec des nombres aléatoires
    # from random import randint
    # todo mesurer le temps d'execution
    test = Map(15, 7)
    test[2, 3] = "P"
    test.create_border()
    print(test)
    print(test[2, 3])
