import math
import queue
import control
import numpy as np


def check_goal(i1,j1,i2,j2, map):
    if i1 == i2 and j1 == j2 and map[i1,j1] == 10:
        return True

def swap(arr,pos1,pos2):
    temp = arr[pos1]
    arr[pos1] = arr[pos2]
    arr[pos2] = temp
    return arr

def check_visited(check, visited):
    if check in visited:
        return True
    if check[0] == check[2] and check[1] == check[3]:
        return False
    if check[0] == check[2]:
        check = swap(check,1,3)
        if check in visited:
            return True
    if check[1] == check[3]:
        check = swap(check,0,2)
        if check in visited:
            return True
    return False

def dfs(i1,j1,i2,j2,map):
    visited = []
    stack = []
    #Thêm vào stack vị trí đầu tiên
    stack.append([i1,j1,i2,j2,map])
    while (len(stack) != 0):
        item_pop = stack.pop()
        visited.append(item_pop[:4])
        i1,j1,i2,j2,map = item_pop
        #Di chuyển lên (UP)
        temp_map = map.copy()
        x1,y1,x2,y2,new_map,valid = control.UP(i1,j1,i2,j2,temp_map)
        if valid and (not check_visited([x1,y1,x2,y2], visited)):
            stack.append([x1,y1,x2,y2,new_map])
            if check_goal(x1,y1,x2,y2,new_map):
                print(visited)
                print(f"-->[{x1},{y1},{x2},{y2}]")
                print("Success")
                exit()
        #Di chuyển xuống (DOWN)
        temp_map = map.copy()
        x1,y1,x2,y2,new_map,valid = control.DOWN(i1,j1,i2,j2,temp_map)
        if valid and (not check_visited([x1,y1,x2,y2], visited)):
            stack.append([x1,y1,x2,y2,new_map])
            if check_goal(x1,y1,x2,y2,new_map):
                print(visited)
                print(f"-->[{x1},{y1},{x2},{y2}]")
                print("Success")
                exit()
        #Di chuyển qua trái (LEFT)
        temp_map = map.copy()
        x1,y1,x2,y2,new_map,valid = control.LEFT(i1,j1,i2,j2,temp_map)
        if valid and (not check_visited([x1,y1,x2,y2], visited)):
            stack.append([x1,y1,x2,y2,new_map])
            if check_goal(x1,y1,x2,y2,new_map):
                print(visited)
                print(f"-->[{x1},{y1},{x2},{y2}]")
                print("Success")
                exit()
        #Di chuyển qua phải (RIGHT)
        temp_map = map.copy()
        x1,y1,x2,y2,new_map,valid = control.RIGHT(i1,j1,i2,j2,temp_map)
        if valid and (not check_visited([x1,y1,x2,y2], visited)):
            stack.append([x1,y1,x2,y2,new_map])
            if check_goal(x1,y1,x2,y2,new_map):
                print(visited)
                print(f"-->[{x1},{y1},{x2},{y2}]")
                print("Success")
                exit()
    print("Not found")
    exit()

def bfs(i1,j1,i2,j2, map):
    visited = []
    queue = []
    #Thêm vào queue vị trí bắt đầu
    queue.append([i1,j1,i2,j2,map])
    while (len(queue) != 0):
        item_pop = queue.pop(0)
        visited.append(item_pop[:4])
        i1,j1,i2,j2,map = item_pop
        #Di chuyển lên (UP)
        temp_map = map.copy()
        x1,y1,x2,y2,new_map,valid = control.UP(i1,j1,i2,j2,temp_map)
        if valid and (not check_visited([x1,y1,x2,y2], visited)):
            queue.append([x1,y1,x2,y2,new_map])
            if check_goal(x1,y1,x2,y2,new_map):
                print(visited)
                print(f"-->[{x1},{y1},{x2},{y2}]")
                print("Success")
                exit()
        #Di chuyển xuống (DOWN)
        temp_map = map.copy()
        x1,y1,x2,y2,new_map,valid = control.DOWN(i1,j1,i2,j2,temp_map)
        if valid and (not check_visited([x1,y1,x2,y2], visited)):
            queue.append([x1,y1,x2,y2,new_map])
            if check_goal(x1,y1,x2,y2,new_map):
                print(visited)
                print(f"-->[{x1},{y1},{x2},{y2}]")
                print("Success")
                exit()
        #Di chuyển qua trái (LEFT)
        temp_map = map.copy()
        x1,y1,x2,y2,new_map,valid = control.LEFT(i1,j1,i2,j2,temp_map)
        if valid and (not check_visited([x1,y1,x2,y2], visited)):
            queue.append([x1,y1,x2,y2,new_map])
            if check_goal(x1,y1,x2,y2,new_map):
                print(visited)
                print(f"-->[{x1},{y1},{x2},{y2}]")
                print("Success")
                exit()
        #Di chuyển qua phải (RIGHT)
        temp_map = map.copy()
        x1,y1,x2,y2,new_map,valid = control.RIGHT(i1,j1,i2,j2,temp_map)
        if valid and (not check_visited([x1,y1,x2,y2], visited)):
            queue.append([x1,y1,x2,y2,new_map])
            if check_goal(x1,y1,x2,y2,new_map):
                print(visited)
                print(f"-->[{x1},{y1},{x2},{y2}]")
                print("Success")
                exit()
    print("Not found")
    exit()


if __name__ == "__main__":
    # Map 1 //  initBlock = [1,1,1,1]
    # map = np.matrix([
    #     [2,2,2,0,0,0,0,0,0,0],
    #     [2,2,2,2,2,2,0,0,0,0],
    #     [2,2,2,2,2,2,2,2,2,0],
    #     [0,2,2,2,2,2,2,2,2,2],
    #     [0,0,0,0,0,2,2,12,2,2],
    #     [0,0,0,0,0,0,2,2,2,0]
    # ])
    
    # Map 2
    # map = np.matrix([
    #     [0,0,0,0,0,0,2,2,2,2,0,0,2,2,2],
    #     [2,2,2,2,0,0,2,2,2,2,0,0,2,12,2],
    #     [2,2,2,2,0,0,2,2,2,2,0,0,2,2,2],
    #     [2,2,2,2,0,0,2,2,2,2,0,0,2,2,2],
    #     [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
    #     [2,2,2,2,0,0,2,2,2,2,0,0,0,0,0]
    # ])

    # Map 3 //  initBlock = [3,1,3,1]
    map = np.matrix([
        [0,0,0,0,0,0,2,2,2,2,2,2,2,0,0],
        [2,2,2,2,0,0,2,2,2,0,0,2,2,0,0],
        [2,2,2,2,2,2,2,2,2,0,0,2,2,2,2],
        [2,2,2,2,0,0,0,0,0,0,0,2,2,12,2],
        [2,2,2,2,0,0,0,0,0,0,0,2,2,2,2],
        [0,0,0,0,0,0,0,0,0,0,0,0,2,2,2]
    ])

    initBlock = [3,1,3,1]
    i1 = initBlock[0]
    j1 = initBlock[1]
    i2 = initBlock[2]
    j2 = initBlock[3]
    map[i1,j1] = map[i1,j1] - 1
    map[i2,j2] = map[i2,j2] - 1

    # i1,j1,i2,j2,map,valid = control.DOWN(i1,j1,i2,j2,map)
    # print(map, valid)

    dfs(i1,j1,i2,j2,map)