import math
import control
import numpy as np

def check_valid_move(i1,j1,i2,j2, map):
    if (i1 < 0 or i2 < 0 or i1 >= map.shape[0] or i2 >= map.shape[0]) or (j1 < 0 or j2 < 0 or j1 >= map.shape[1] or j2 >= map.shape[1]):
        return False
    return True

class blind_search:
    def __init__(self,i1,j1,i2,j2, map):
        self.i1 = i1
        self.j1 = j1
        self.i2 = i2
        self.j2 = j2
        self.map = map
    def dfs(self):
        visited = []
        stack = []
        check = check_valid_move(self.i1,self.j1,self.i2,self.j2,self.map)
        #Di chuyển lên đến khi không còn đi được
        while (check):
            stack.append(np.array(self.i1,self.j1,self.i2,self.j2))
            self.i1,self.j1,self.i2,self.j2 = control.UP(self.i1,self.j1,self.i2,self.j2)
            check = check_valid_move(self.i1,self.j1,self.i2,self.j2,self.map)




if __name__ == "__main__":
    map = np.matrix([
        [2,2,2,0,0,0,0,0,0,0],
        [2,2,2,2,2,2,0,0,0,0],
        [2,2,2,2,2,2,2,2,2,0],
        [0,2,2,2,2,2,2,2,2,2],
        [0,0,0,0,0,2,2,0,2,2],
        [0,0,0,0,0,0,2,2,2,0]
    ])
    initBlock = [1,1,1,1]
    i1 = initBlock[0]
    j1 = initBlock[1]
    i2 = initBlock[2]
    j2 = initBlock[3]

    map[i1,j1] = map[i1,j1] - 1
    map[i2,j2] = map[i2,j2] - 1

    i1,j1,i2,j2 = control.UP(i1,j1,i2,j2)
    print(map)