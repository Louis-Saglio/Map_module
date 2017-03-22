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
                iterator.append({
                    "case": self.map[l][h],
                    "position": (l, h),
                    "is_top_border": True if h == 0 else False,
                    "is_left_border": True if l == 0 else False,
                    "is_bottom_border": True if h == self.height-1 else False,
                    "is_right_border": True if l == self.width-1 else False
                })
        return iter(iterator)

    def __getitem__(self, pos):
        index1, index2 = pos
        return self.map[index1][index2]

    def __setitem__(self, key, value):
        index1, index2 = key
        self.map[index1][index2] = value

    def __str__(self):
        rep = ''
        for case in self:
            rep += case["case"] + ''
        return rep

    def create_map(self):
        return [[self.filling_type for h in range(self.height)] for l in range(self.width)]

    def print_map(self):
        print('')
        for case in self:
            print(case["case"] + ' ', end='\n' if case["is_right_border"] else '', sep='')

    def is_border_position(self, pos):
        h, l = pos
        return h == self.height - 1 or h == 0 or l == self.width - 1 or l == 0

    def create_border(self):
        for case in self:
            if len([case[clef] for clef in case if case[clef] and clef not in ["case", "position"]]) != 0:
                self[case["position"]] = self.border_type

    @staticmethod
    def clear():
        # todo executer "cls" ou "clear" en fonction de l'os
        from os import system
        system("cls")


class Pawn:

    def __init__(self, a_map, position=(1, 1)):
        self.x, self.y = position

    def get_in_map(self):
        pass

if __name__ == '__main__':
    # todo tester le module avec des nombres aléatoires
    # from random import randint
    # todo mesurer le temps d'execution
    test = Map(15, 7)
    test[2, 3] = "P"
    test.create_border()
    test.print_map()
    print(test[2, 3])
    print(test)
