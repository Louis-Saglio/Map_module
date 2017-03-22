class Case:

    def __init__(self, value, owning_map, coordinates):
        self.value = value
        self.owning_map = owning_map
        self.coordinates = coordinates
        self.border = self.get_border_type()

    def __str__(self):
        return str(self.value)

    def get_border_type(self):
        l, h = self.coordinates
        return {
            "is_top": True if h == 0 else False,
            "is_left": True if l == 0 else False,
            "is_bottom": True if h == self.owning_map.height - 1 else False,
            "is_right": True if l == self.owning_map.width - 1 else False
        }

    def is_border_position(self, pos):
        l, h = pos
        return len([True for value in self.border.values() if value]) != 0


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

    def create_border(self):
        for case in self:
            if case.is_border_position(case.coordinates):
                self[case.coordinates] = Case(self.border_type, self, case.coordinates)


class Pawn:

    def __init__(self, owning_map, position, look):
        """
        :type owning_map Map
        :type position tuple
        :type look str
        """
        self._position = position
        self.look = look
        self.owning_map = owning_map
        self._case = self.owning_map[self.position]
        self.set_position(self.position)

    def __str__(self):
        return str(self.look)

    @property
    def case(self):
        return self._case

    @property
    def position(self):
        return self._position

    def set_position(self, new_position):
        self._position = new_position
        self._case = self.owning_map[self.position]
        self.owning_map[self.position] = self

    def move_up(self):
        self.owning_map[self.position] = self.case
        self.set_position((self.position[0], self.position[1]-1))

    def move_down(self):
        self.owning_map[self.position] = self.case
        self.set_position((self.position[0], self.position[1]+1))

    def move_right(self):
        self.owning_map[self.position] = self.case
        self.set_position((self.position[0]+1, self.position[1]))

    def move_left(self):
        self.owning_map[self.position] = self.case
        self.set_position((self.position[0]-1, self.position[1]))


if __name__ == '__main__':
    # todo mesurer le temps d'execution
    x, y, a, b = 10, 6, 2, 3
    test = Map(x, y)
    test.create_border()
    test[a, b] = "P"
    print(test[a, b])
    pawn = Pawn(test, (5, 4), "O")
    pawn.move_up()
    pawn.move_left()
    pawn.move_down()
    pawn.move_right()
    print(test)
