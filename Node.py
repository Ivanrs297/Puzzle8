# This is a class to represent the Node of a Search Tree

def cmp(a, b):
    return (a > b) - (a < b)

class Node:
    value = ""  # The value of the node
    x = None  # The index of the X
    father = None  # The father of the node
    weight = 0  # The value of the g(n)
    heuristic = None  # The value of the heuristic of the node h(u)
    movement = None  # The movement to get to this state
    cost = 0

    # Constructor
    def __init__(self, value, father, T, movement):
        self.value = value
        self.x = value.find('0')
        self.heuristic = self.get_heuristic(value, T)
        self.father = father
        self.movement = movement
        if father is None:
            self.weight = 0
        else:
            self.weight = father.weight + 1
        self.cost = self.get_cost()  # g(n) + h(n)

    def __eq__(self, obj):
        return isinstance(obj, Node) and obj.value == self.value

    def __lt__(self, other):
        return self.cost < other.cost

    # Function to get the list of succesors of the node
    def expand(self, T, A):
        node_list = []
        for movement in A:
            validMove = False
            if movement == -3 and self.x >= 3 and self.x <= 8:
                validMove = True
            elif movement == 1 and self.x != 2 and self.x != 5 and self.x != 8:
                validMove = True
            elif movement == -1 and self.x != 0 and self.x != 3 and self.x != 6:
                validMove = True
            elif movement == 3 and self.x <= 5:
                validMove = True

            # If the movement is valid then:
            if validMove:
                newValue = list(self.value)  # Change to array to swap positions
                newValue[self.x], newValue[self.x + movement] = newValue[self.x + movement], newValue[
                    self.x]  # Get the new value of the state
                node_list.append(Node(''.join(newValue), self, T, A.index(movement)))

        return node_list

    # Function to return the cost of the state
    def get_cost(self):
        return self.weight + self.heuristic

    # Function to calculate the Heuristic
    def get_heuristic(self, value, T):
        heuristic_value = 0
        for x in range(len(value)):
            if value[x] != T[x]:
                heuristic_value += 1
        return heuristic_value
