def UP(i1,j1,i2,j2):
    if i1==i2 and j1==j2:   #Khi khối hộp đứng thẳng
        i1 = i1-2
        i2 = i2-1
    elif i1==i2+1 and j1==j2:   #Khi khối hộp nằm dọc
        i1 = i1-2
        i2 = i2-1
    elif i1==i2-1 and j1==j2:   #Khi khối hộp nằm dọc
        i1 = i1-1
        i2 = i2-2
    elif i1==i2 and j1==j2+1:   #Khi khối hộp nằm ngang
        i1 = i1-1
        i2 = i2-1
    elif i1==i2 and j1==j2-1:   #Khi khối hộp nằm ngang
        i1 = i1-1
        i2 = i2-1
    return (i1,j1,i2,j2)

def DOWN(i1,j1,i2,j2):
    if i1==i2 and j1==j2:   #Khi khối hộp đứng thẳng
        i1 = i1+2
        i2 = i2+1
    elif i1==i2+1 and j1==j2:   #Khi khối hộp nằm dọc
        i1 = i1+1
        i2 = i2+2
    elif i1==i2-1 and j1==j2:   #Khi khối hộp nằm dọc
        i1 = i1+2
        i2 = i2+1
    elif i1==i2 and j1==j2+1:   #Khi khối hộp nằm ngang
        i1 = i1+1
        i2 = i2+1
    elif i1==i2 and j1==j2-1:   #Khi khối hộp nằm ngang
        i1 = i1+1
        i2 = i2+1
    return (i1,j1,i2,j2)

def LEFT(i1,j1,i2,j2):
    if i1==i2 and j1==j2:   #Khi khối hộp đứng thẳng
        j1 = j1-2
        j2 = j2-1
    elif i1==i2+1 and j1==j2:   #Khi khối hộp nằm dọc
        j1 = j1-1
        j2 = j2-1
    elif i1==i2-1 and j1==j2:   #Khi khối hộp nằm dọc
        j1 = j1-1
        j2 = j2-1
    elif i1==i2 and j1==j2+1:   #Khi khối hộp nằm ngang
        j1 = j1-2
        j2 = j2-1
    elif i1==i2 and j1==j2-1:   #Khi khối hộp nằm ngang
        j1 = j1-1
        j2 = j2-2
    return (i1,j1,i2,j2)
    
def RIGHT(i1,j1,i2,j2):
    if i1==i2 and j1==j2:   #Khi khối hộp đứng thẳng
        j1 = j1+2
        j2 = j2+1
    elif i1==i2+1 and j1==j2:   #Khi khối hộp nằm dọc
        j1 = j1+1
        j2 = j2+1
    elif i1==i2-1 and j1==j2:   #Khi khối hộp nằm dọc
        j1 = j1+1
        j2 = j2+1
    elif i1==i2 and j1==j2+1:   #Khi khối hộp nằm ngang
        j1 = j1+1
        j2 = j2+2
    elif i1==i2 and j1==j2-1:   #Khi khối hộp nằm ngang
        j1 = j1+2
        j2 = j2+1
    return (i1,j1,i2,j2)