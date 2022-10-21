def UP(i1,j1,i2,j2,map):
    valid = True
    if i1==i2 and j1==j2:   #Khi khối hộp đứng thẳng
        map[i1,j1] = map[i1,j1] + 2
        i1 = i1-2
        i2 = i2-1
        if (i1 < 0 or i2 < 0 or i1 >= map.shape[0] or i2 >= map.shape[0]) or (j1 < 0 or j2 < 0 or j1 >= map.shape[1] or j2 >= map.shape[1]):
            valid = False
        if valid:
            map[i1,j1] = map[i1,j1] - 1
            map[i2,j2] = map[i2,j2] - 1
            if map[i1,j1] < 0 or map[i2,j2] < 0:
                valid = False
    elif i1==i2+1 and j1==j2:   #Khi khối hộp nằm dọc
        map[i1,j1] = map[i1,j1] + 1
        map[i2,j2] = map[i2,j2] + 1
        i1 = i1-2
        i2 = i2-1
        if (i1 < 0 or i2 < 0 or i1 >= map.shape[0] or i2 >= map.shape[0]) or (j1 < 0 or j2 < 0 or j1 >= map.shape[1] or j2 >= map.shape[1]):
            valid = False
        if valid:
            map[i1,j1] = map[i1,j1] - 2
            if map[i1,j1] < 0:
                valid = False
    elif i1==i2-1 and j1==j2:   #Khi khối hộp nằm dọc
        map[i1,j1] = map[i1,j1] + 1
        map[i2,j2] = map[i2,j2] + 1
        i1 = i1-1
        i2 = i2-2
        if (i1 < 0 or i2 < 0 or i1 >= map.shape[0] or i2 >= map.shape[0]) or (j1 < 0 or j2 < 0 or j1 >= map.shape[1] or j2 >= map.shape[1]):
            valid = False
        if valid:
            map[i1,j1] = map[i1,j1] - 2
            if map[i1,j1] < 0:
                valid = False
    elif i1==i2 and j1==j2+1:   #Khi khối hộp nằm ngang
        map[i1,j1] = map[i1,j1] + 1
        map[i2,j2] = map[i2,j2] + 1
        i1 = i1-1
        i2 = i2-1
        if (i1 < 0 or i2 < 0 or i1 >= map.shape[0] or i2 >= map.shape[0]) or (j1 < 0 or j2 < 0 or j1 >= map.shape[1] or j2 >= map.shape[1]):
            valid = False
        if valid:
            map[i1,j1] = map[i1,j1] - 1
            map[i2,j2] = map[i2,j2] - 1
            if map[i1,j1] < 0 or map[i2,j2] < 0:
                valid = False
    elif i1==i2 and j1==j2-1:   #Khi khối hộp nằm ngang
        map[i1,j1] = map[i1,j1] + 1
        map[i2,j2] = map[i2,j2] + 1
        i1 = i1-1
        i2 = i2-1
        if (i1 < 0 or i2 < 0 or i1 >= map.shape[0] or i2 >= map.shape[0]) or (j1 < 0 or j2 < 0 or j1 >= map.shape[1] or j2 >= map.shape[1]):
            valid = False
        if valid:
            map[i1,j1] = map[i1,j1] - 1
            map[i2,j2] = map[i2,j2] - 1
            if map[i1,j1] < 0 or map[i2,j2] < 0:
                valid = False
    return (i1,j1,i2,j2,map,valid)

def DOWN(i1,j1,i2,j2,map):
    valid = True
    if i1==i2 and j1==j2:   #Khi khối hộp đứng thẳng
        map[i1,j1] = map[i1,j1] + 2
        i1 = i1+2
        i2 = i2+1
        if (i1 < 0 or i2 < 0 or i1 >= map.shape[0] or i2 >= map.shape[0]) or (j1 < 0 or j2 < 0 or j1 >= map.shape[1] or j2 >= map.shape[1]):
            valid = False
        if valid:
            map[i1,j1] = map[i1,j1] - 1
            map[i2,j2] = map[i2,j2] - 1
            if map[i1,j1] < 0 or map[i2,j2] < 0:
                valid = False
    elif i1==i2+1 and j1==j2:   #Khi khối hộp nằm dọc
        map[i1,j1] = map[i1,j1] + 1
        map[i2,j2] = map[i2,j2] + 1
        i1 = i1+1
        i2 = i2+2
        if (i1 < 0 or i2 < 0 or i1 >= map.shape[0] or i2 >= map.shape[0]) or (j1 < 0 or j2 < 0 or j1 >= map.shape[1] or j2 >= map.shape[1]):
            valid = False
        if valid:
            map[i1,j1] = map[i1,j1] - 2
            if map[i1,j1] < 0:
                valid = False
    elif i1==i2-1 and j1==j2:   #Khi khối hộp nằm dọc
        map[i1,j1] = map[i1,j1] + 1
        map[i2,j2] = map[i2,j2] + 1
        i1 = i1+2
        i2 = i2+1
        if (i1 < 0 or i2 < 0 or i1 >= map.shape[0] or i2 >= map.shape[0]) or (j1 < 0 or j2 < 0 or j1 >= map.shape[1] or j2 >= map.shape[1]):
            valid = False
        if valid:
            map[i1,j1] = map[i1,j1] - 2
            if map[i1,j1] < 0:
                valid = False
    elif i1==i2 and j1==j2+1:   #Khi khối hộp nằm ngang
        map[i1,j1] = map[i1,j1] + 1
        map[i2,j2] = map[i2,j2] + 1
        i1 = i1+1
        i2 = i2+1
        if (i1 < 0 or i2 < 0 or i1 >= map.shape[0] or i2 >= map.shape[0]) or (j1 < 0 or j2 < 0 or j1 >= map.shape[1] or j2 >= map.shape[1]):
            valid = False
        if valid:
            map[i1,j1] = map[i1,j1] - 1
            map[i2,j2] = map[i2,j2] - 1
            if map[i1,j1] < 0 or map[i2,j2] < 0:
                valid = False
    elif i1==i2 and j1==j2-1:   #Khi khối hộp nằm ngang
        map[i1,j1] = map[i1,j1] + 1
        map[i2,j2] = map[i2,j2] + 1
        i1 = i1+1
        i2 = i2+1
        if (i1 < 0 or i2 < 0 or i1 >= map.shape[0] or i2 >= map.shape[0]) or (j1 < 0 or j2 < 0 or j1 >= map.shape[1] or j2 >= map.shape[1]):
            valid = False
        if valid:
            map[i1,j1] = map[i1,j1] - 1
            map[i2,j2] = map[i2,j2] - 1
            if map[i1,j1] < 0 or map[i2,j2] < 0:
                valid = False
    return (i1,j1,i2,j2,map,valid)

def LEFT(i1,j1,i2,j2,map):
    valid = True
    if i1==i2 and j1==j2:   #Khi khối hộp đứng thẳng
        map[i1,j1] = map[i1,j1] + 2
        j1 = j1-2
        j2 = j2-1
        if (i1 < 0 or i2 < 0 or i1 >= map.shape[0] or i2 >= map.shape[0]) or (j1 < 0 or j2 < 0 or j1 >= map.shape[1] or j2 >= map.shape[1]):
            valid = False
        if valid:
            map[i1,j1] = map[i1,j1] - 1
            map[i2,j2] = map[i2,j2] - 1
            if map[i1,j1] < 0 or map[i2,j2] < 0:
                valid = False
    elif i1==i2+1 and j1==j2:   #Khi khối hộp nằm dọc
        map[i1,j1] = map[i1,j1] + 1
        map[i2,j2] = map[i2,j2] + 1
        j1 = j1-1
        j2 = j2-1
        if (i1 < 0 or i2 < 0 or i1 >= map.shape[0] or i2 >= map.shape[0]) or (j1 < 0 or j2 < 0 or j1 >= map.shape[1] or j2 >= map.shape[1]):
            valid = False
        if valid:
            map[i1,j1] = map[i1,j1] - 1
            map[i2,j2] = map[i2,j2] - 1
            if map[i1,j1] < 0 or map[i2,j2] < 0:
                valid = False
    elif i1==i2-1 and j1==j2:   #Khi khối hộp nằm dọc
        map[i1,j1] = map[i1,j1] + 1
        map[i2,j2] = map[i2,j2] + 1
        j1 = j1-1
        j2 = j2-1
        if (i1 < 0 or i2 < 0 or i1 >= map.shape[0] or i2 >= map.shape[0]) or (j1 < 0 or j2 < 0 or j1 >= map.shape[1] or j2 >= map.shape[1]):
            valid = False
        if valid:
            map[i1,j1] = map[i1,j1] - 1
            map[i2,j2] = map[i2,j2] - 1
            if map[i1,j1] < 0 or map[i2,j2] < 0:
                valid = False
    elif i1==i2 and j1==j2+1:   #Khi khối hộp nằm ngang
        map[i1,j1] = map[i1,j1] + 1
        map[i2,j2] = map[i2,j2] + 1
        j1 = j1-2
        j2 = j2-1
        if (i1 < 0 or i2 < 0 or i1 >= map.shape[0] or i2 >= map.shape[0]) or (j1 < 0 or j2 < 0 or j1 >= map.shape[1] or j2 >= map.shape[1]):
            valid = False
        if valid:
            map[i1,j1] = map[i1,j1] - 2
            if map[i1,j1] < 0:
                valid = False
    elif i1==i2 and j1==j2-1:   #Khi khối hộp nằm ngang
        map[i1,j1] = map[i1,j1] + 1
        map[i2,j2] = map[i2,j2] + 1
        j1 = j1-1
        j2 = j2-2
        if (i1 < 0 or i2 < 0 or i1 >= map.shape[0] or i2 >= map.shape[0]) or (j1 < 0 or j2 < 0 or j1 >= map.shape[1] or j2 >= map.shape[1]):
            valid = False
        if valid:
            map[i1,j1] = map[i1,j1] - 2
            if map[i1,j1] < 0:
                valid = False
    return (i1,j1,i2,j2,map,valid)
    
def RIGHT(i1,j1,i2,j2,map):
    valid = True
    if i1==i2 and j1==j2:   #Khi khối hộp đứng thẳng
        map[i1,j1] = map[i1,j1] + 2
        j1 = j1+2
        j2 = j2+1
        if (i1 < 0 or i2 < 0 or i1 >= map.shape[0] or i2 >= map.shape[0]) or (j1 < 0 or j2 < 0 or j1 >= map.shape[1] or j2 >= map.shape[1]):
            valid = False
        if valid:
            map[i1,j1] = map[i1,j1] - 1
            map[i2,j2] = map[i2,j2] - 1
            if map[i1,j1] < 0 or map[i2,j2] < 0:
                valid = False
    elif i1==i2+1 and j1==j2:   #Khi khối hộp nằm dọc
        map[i1,j1] = map[i1,j1] + 1
        map[i2,j2] = map[i2,j2] + 1
        j1 = j1+1
        j2 = j2+1
        if (i1 < 0 or i2 < 0 or i1 >= map.shape[0] or i2 >= map.shape[0]) or (j1 < 0 or j2 < 0 or j1 >= map.shape[1] or j2 >= map.shape[1]):
            valid = False
        if valid:
            map[i1,j1] = map[i1,j1] - 1
            map[i2,j2] = map[i2,j2] - 1
            if map[i1,j1] < 0 or map[i2,j2] < 0:
                valid = False
    elif i1==i2-1 and j1==j2:   #Khi khối hộp nằm dọc
        map[i1,j1] = map[i1,j1] + 1
        map[i2,j2] = map[i2,j2] + 1
        j1 = j1+1
        j2 = j2+1
        if (i1 < 0 or i2 < 0 or i1 >= map.shape[0] or i2 >= map.shape[0]) or (j1 < 0 or j2 < 0 or j1 >= map.shape[1] or j2 >= map.shape[1]):
            valid = False
        if valid:
            map[i1,j1] = map[i1,j1] - 1
            map[i2,j2] = map[i2,j2] - 1
            if map[i1,j1] < 0 or map[i2,j2] < 0:
                valid = False
    elif i1==i2 and j1==j2+1:   #Khi khối hộp nằm ngang
        map[i1,j1] = map[i1,j1] + 1
        map[i2,j2] = map[i2,j2] + 1
        j1 = j1+1
        j2 = j2+2
        if (i1 < 0 or i2 < 0 or i1 >= map.shape[0] or i2 >= map.shape[0]) or (j1 < 0 or j2 < 0 or j1 >= map.shape[1] or j2 >= map.shape[1]):
            valid = False
        if valid:
            map[i1,j1] = map[i1,j1] - 2
            if map[i1,j1] < 0:
                valid = False
    elif i1==i2 and j1==j2-1:   #Khi khối hộp nằm ngang
        map[i1,j1] = map[i1,j1] + 1
        map[i2,j2] = map[i2,j2] + 1
        j1 = j1+2
        j2 = j2+1
        if (i1 < 0 or i2 < 0 or i1 >= map.shape[0] or i2 >= map.shape[0]) or (j1 < 0 or j2 < 0 or j1 >= map.shape[1] or j2 >= map.shape[1]):
            valid = False
        if valid:
            map[i1,j1] = map[i1,j1] - 2
            if map[i1,j1] < 0:
                valid = False
    return (i1,j1,i2,j2,map,valid)