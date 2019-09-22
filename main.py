from BFS import BFS
from Scanner import Scanner
import time

A = [-3, 1, -1, 3]
Terminal = "123804765"
# nO = "123084765" # facil
# nO = "023184765"  # medio
# nO = Scanner().scan()
scanner = Scanner()
puzzle = scanner.scan()
if puzzle:
    obj = BFS(puzzle, A, Terminal)
    t_start = time.process_time()
    obj.search()
    t_end = time.process_time()

    print("Elapsed time during the whole program in seconds:",
    t_end - t_start)



# obj = BFS(nO, A, "123804765")
# # # obj = BFS("203184765", a, "123804765")
# # obj.search()