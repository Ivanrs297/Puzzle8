class Printer:

    def print(self, node_path_list):
        for node in node_path_list:
            print()
            print(self.get_movement(node.movement))
            for i, char in enumerate(node.value):
                print(char, end=" ")
                if (i + 1) % 3 == 0:
                    print()
            print()

    def get_movement(self, movement):
        if movement == 0:
            return "UP"
        elif movement == 1:
            return "RIGHT"
        elif movement == 2:
            return "LEFT"
        elif movement == 3:
            return "DOWN"
        else:
            return "ROOT"

