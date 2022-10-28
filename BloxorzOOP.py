class  Position:
    def __init__(self, i1,j1,i2,j2,parent = None):
        self.i1 = i1
        self.j1 = j1
        self.i2 = i2
        self.j2 = j2
        self.parent = parent
    def print(self):
        print("(", self.i1, self.j1, ")",  "(", self.i2, self.j2, ")")
    def get_state(self):
        if self.i1 == self.i2 and self.j1 == self.j2:
            return "STANDING"
        elif self.i1 == self.i2 and (self.j1 == self.j2-1 or self.j1 == self.j2+1):
            return "LYING_HORIZONTALLY"
        elif self.j1 == self.j2 and (self.i1 == self.i2-1 or self.i1 == self.i2+1):
            return "LYING_VERTICALLY"
    def move(self,instruction):
        state = self.get_state()
        if instruction == "UP":
            if state == "STANDING":
                return Position(self.i1-2, self.j1, self.i2-1, self.j2, self)
            if state == "LYING_HORIZONTALLY":
                return Position(self.i1-1, self.j1, self.i2-1, self.j2, self)
            if state == "LYING_VERTICALLY":
                return Position(min(self.i1, self.i2)-1, self.j1, min(self.i1, self.i2)-1, self.j2, self)
        if instruction == "DOWN":
            if state == "STANDING":
                return Position(self.i1+2, self.j1, self.i2+1, self.j2, self)
            if state == "LYING_HORIZONTALLY":
                return Position(self.i1+1, self.j1, self.i2+1, self.j2, self)
            if state == "LYING_VERTICALLY":
                return Position(max(self.i1, self.i2)+1, self.j1, max(self.i1, self.i2)+1, self.j2, self)
        if instruction == "LEFT":
            if state == "STANDING":
                return Position(self.i1, self.j1-2, self.i2, self.j2-1, self)
            if state == "LYING_HORIZONTALLY":
                return Position(self.i1, min(self.j1, self.j2)-1, self.i2, min(self.j1, self.j2)-1, self)
            if state == "LYING_VERTICALLY":
                return Position(self.i1, self.j1-1, self.i2, self.j2-1, self)
        if instruction == "RIGHT":
            if state == "STANDING":
                return Position(self.i1, self.j1+2, self.i2, self.j2+1, self)
            if state == "LYING_HORIZONTALLY":
                return Position(self.i1, max(self.j1, self.j2)+1, self.i2, max(self.j1, self.j2)+1, self)
            if state == "LYING_VERTICALLY":
                return Position(self.i1, self.j1+1, self.i2, self.j2+1, self)
    def is_visited(self, visited):
        return ([self.i1, self.j1, self.i2, self.j2] in visited) or ([self.i2, self.j1, self.i1, self.j2] in visited) or ([self.i1, self.j2, self.i2, self.j1] in visited) or ([self.i2, self.j2, self.i1, self.j1] in visited)
    def expand(self):
        return [self.move("UP"), self.move("DOWN"), self.move("LEFT"), self.move("RIGHT")]

class Bloxorz:
    def __init__(self,map,init_position):
        self.map = map
        self.init_position = init_position
    def is_goal(self,current_position):
        return current_position.get_state() == "STANDING" and self.map[current_position.i1][current_position.j1] == 10
    def is_valid_position(self,current_position):
        if current_position.i1 < 0 or current_position.i2 < 0 or current_position.j1 < 0 or current_position.j2 < 0:
            return False
        if current_position.i1 >= len(self.map) or current_position.i2 >= len(self.map) or current_position.j1 >= len(self.map[0]) or current_position.j2 >= len(self.map[0]):
            return False
        if current_position.get_state() == "STANDING":
            return self.map[current_position.i1][current_position.j1] > 1
        else:
            return self.map[current_position.i1][current_position.j1] > 0 and self.map[current_position.i2][current_position.j2] > 0
    def DFS(self, stack, visited, loop):
        while len(stack) > 0:
            this_position = stack.pop()
            visited.append([this_position.i1, this_position.j1, this_position.i2, this_position.j2])
            exp_list = this_position.expand()
            for pos in exp_list:
                if self.is_valid_position(pos):
                    if not pos.is_visited(visited):
                        stack.append(pos)
                    if self.is_goal(pos): 
                        path = [pos]
                        while path[-1].parent != None: path.append(path[-1].parent)
                        path.reverse()
                        print("Goal reached after", loop, "loops")
                        return path
            loop = loop + 1
        if len(stack) == 0:
            print("No solutions")
            exit()


initBlock = Position(3,1,3,1)
map = [[0,0,0,0,0,0,2,2,2,2,2,2,2,0,0],
        [2,2,2,2,0,0,2,2,2,0,0,2,2,0,0],
        [2,2,2,2,2,2,2,2,2,0,0,2,2,2,2],
        [2,2,2,2,0,0,0,0,0,0,0,2,2,10,2],
        [2,2,2,2,0,0,0,0,0,0,0,2,2,2,2],
        [0,0,0,0,0,0,0,0,0,0,0,0,2,2,2]]
game = Bloxorz(map, initBlock)
path = game.DFS([initBlock], [], 0)
for position in path: position.print()






# bloxorz = Position(1,1,1,1)
# print(bloxorz.i1)
# bloxorz.print()
# print(bloxorz.get_state())
# exp = bloxorz.expand()
# for e in exp:
#     e.print()
#     print(e.get_state())