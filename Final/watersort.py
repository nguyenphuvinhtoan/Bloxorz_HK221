# -*- coding: utf-8 -*-
"""WaterSort.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/github/minh-chaudang/IntroAI/blob/main/WaterSort.ipynb
"""

import itertools
import copy
import numpy as np
import heapq
import time

class State:
  def __init__(self, bottles, parent = None, capacity = None):
    self.bottles = bottles
    self.parent = parent
    if parent is None:
      if capacity is None: self.capacity = max(len(bottle) for bottle in self.bottles)
      else: self.capacity = capacity
      self.distance = 0
    else:
      self.capacity = parent.capacity
      self.distance = parent.distance + 1

  # Check if this is the goal
  def is_goal(self):
    return all(len(bottle) == 0 or len(bottle) == self.capacity and len(set(bottle)) == 1 for bottle in self.bottles)

  # Find all pourable bottle pairs
  def pourable_pairs(self):
    result = []
    for i in range(len(self.bottles)-1,-1,-1):
      for j in range(len(self.bottles)-1,-1,-1):
        if i != j:
          # One is containing and one is empty
          if len(self.bottles[i]) > 0 and len(self.bottles[j]) == 0: 
            result.append((i,j))
          # Two have the same tops
          if len(self.bottles[i]) > 0 and len(self.bottles[j]) > 0 and self.bottles[i][-1] == self.bottles[j][-1] and len(self.bottles[j]) < self.capacity:
            result.append((i,j))
    return result

  # Expand a state
  def expand(self):
    # If this state is expandible
    children = []
    for pair in self.pourable_pairs():
      
      child = State(copy.deepcopy(self.bottles), self)
      top = child.bottles[pair[0]][-1]
      while len(child.bottles[pair[0]]) > 0 and child.bottles[pair[0]][-1] == top and len(child.bottles[pair[1]]) < self.capacity:
        child.bottles[pair[0]].pop()
        child.bottles[pair[1]].append(top)
      children.append(child)
    return children

  # Estimated f = g + h
  def cost(self):
    h = 0
    for bottle in self.bottles:
      for i in range (len(bottle)-1):
        if bottle[i] != bottle[i+1]: h += 1
    return h + self.distance
  
  # Overide the comparators
  def __lt__(self, other):
    return self.cost() < other.cost()

  def __eq__(self, other):
    return self.bottles == other.bottles
   
  # Get path from root
  def getpath(self):
    path = [self]
    while path[-1].parent != None: path.append(path[-1].parent)
    return path

class Watersort:
  def __init__ (self, initial_state):
    self.initial_state = initial_state

  def DFShelper(self, stack, visited, loop, max_stack_size):
    while len(stack) > 0:
      
      max_stack_size = max(len(stack), max_stack_size)
      current = stack.pop()

      # Just to check if initial state is also goal
      if current.is_goal(): return current, loop, max_stack_size

      visited.append(current)
      children = current.expand()
      for child in children:
        if child.is_goal(): return child, loop, max_stack_size
        if child not in visited: stack.append(child)
      
      loop += 1

    return None, loop, max_stack_size

  def Astarhelper(self, heap, visited, loop, max_heap_size):
    while len(heap) > 0:
      max_heap_size = max(max_heap_size, len(heap))
      current = heapq.heappop(heap)

      # Just to check if initial state is also goal
      if current.is_goal(): return current, loop, max_heap_size

      visited.append(current)
      children = current.expand()
      # for child in children: print(child.bottles)

      for child in children:
        if child.is_goal(): return child, loop, max_heap_size
        if child not in visited: heap.append(child)
        heapq.heapify(heap) 
      
      loop += 1

    return None, loop, max_heap_size

  def DFS(self):
    goal, loop, max_stack_size = self.DFShelper([self.initial_state], [], 0, 0)
    if goal is None: print("No solution")
    else:
      path = [goal]
      while path[-1].parent is not None: path.append(path[-1].parent)
      path.reverse()
      print("DFS executed after", loop, "loops", "with max stack size", max_stack_size)
      for i in range(len(path)): print("Step", i, ":", path[i].bottles)

  def Astar(self):
    goal, loop, max_heap_size = self.Astarhelper([self.initial_state], [], 0, 0)
    if goal is None: print("No solution")
    else:
      path = [goal]
      while path[-1].parent is not None: path.append(path[-1].parent)
      path.reverse()
      print("Astar executed after", loop, "loops", "with max stack size", max_heap_size)
      for i in range(len(path)): print("Step", i, ":", path[i].bottles)

level = {}
level[0] = Watersort(State([['O'], ['O', 'O', 'O']], capacity = 4))
level[1] = Watersort(State([['B','O','B','O'],['O','B','O','B'],[]]))
level[2] = Watersort(State([['O', 'O', 'R', 'B'], ['B', 'O', 'R', 'B'], ['R','B','O','R'],[],[]]))
level[3] = Watersort(State([['O', 'B', 'R', 'O'], ['B', 'R', 'O', 'O'], ['B','R','B','R'],[],[]]))
level[4] = Watersort(State([['P','B','G','O'],['R','O','R','P'],['B','R','G','G'],['P','B','O','G'],['B','R','P','O'],[],[]]))
level[5] = Watersort(State([['B','P','G','G'],['B','O','R','G'],['O','B','P','B'],['R','O','R','P'],['O','G','R','P'],[],[]]))
level[6] = Watersort(State([['R','R','O','B'],['P','B','P','O'],['P','B','R','P'],['O','G','R','G'],['B','G','G','O'],[],[]]))
level[7] = Watersort(State([['O','P','G','P'],['O','R','R','B'],['B','B','G','R'],['O','G','R','O'],['G','O','P','B'],[],[]]))
level[8] = Watersort(State([['G','O','B','R'],['O','P','R','G'],['O','B','R','G'],['P','B','B','G'],['P','P','R','O'],[],[]]))
level[9] = Watersort(State([['B','B','O','P'],['O','P','Y','P'],['R','G','Y','GR'],['GR','R','GR','G'],['B','B','Y','G'],['GR','O','R','Y'],['G','R','O','P'],[],[]]))
level[10] = Watersort(State([['Y','P','GR','Y'],['G','R','B','Y'],['P','GR','O','R'],['O','G','G','Y'],['B','P','G','R'],['GR','R','B','O'],['P','O','B','GR'],[],[]]))
level[11] = Watersort(State([['R','G','G','G'],['O','R','P','G'],['P','O','R','O'],['B','P','O','P'],['B','B','B','O']]))
level[12] = Watersort(State([['R','O','G','P'],['GR','O','GR','G'],['B','GR','P','O'],['P','G','Y','R'],['GR','B','B','B'],['R','Y','P','R'],['O','Y','G','Y'],[],[]]))
level[13] = Watersort(State([['Y','GR','B','Y'],['P','B','R','G'],['B','P','G','B'],['Y','R','GR','O'],['G','O','Y','G'],['R','P','O','R'],['O','P','GR','GR'],[],[]]))
level[14] = Watersort(State([['G','O','R','O'],['B','B','R','O'],['P','P','B','O'],['G','P','R','B'],['G','R','G','P'],[],[]]))
level[15] = Watersort(State([['Y','Y','B','G'],['GR','R','O','P'],['R','G','O','B'],['GR','B','R','P'],['GR','O','P','P'],['G','Y','B','Y'],['G','GR','R','O'],[],[]]))
level[16] = Watersort(State([['B','B','GR','P'],['Y','R','GR','P'],['R','R','GR','B'],['G','Y','Y','O'],['G','O','GR','O'],['O','P','GR','R'],['B','Y','P','G'],[],[]]))
level[17] = Watersort(State([['P','R','B','P'],['R','G','G','O'],['R','O','O','P'],['P','R','G','B'],['G','O','B','B'],[],[]]))
level[18] = Watersort(State([['R','P','P','R'],['Y','R','B','R'],['O','G','O','O'],['GR','B','G','GR'],['G','Y','GR','O'],['Y','GR','P','Y'],['P','B','B','G'],[],[]]))
level[19] = Watersort(State([['P','B','G','B'],['O','GR','P','R'],['B','Y','Y','G'],['P','O','O','G'],['GR','GR','G','R'],['B','R','Y','Y'],['R','P','O','GR'],[],[]]))

def main():
  start = time.time()
  lv = int(input("Choose the level: "))
  print("Please choose option:\n1.DFS\n2.A*")
  mode = int(input("Your option: "))
  if mode == 1:
    level[lv].DFS()
    end = time.time()
  elif mode == 2:
    level[lv].Astar()
    end = time.time()
  else:
    print("Please rechoose option: 1-2!")
  print("Time executed:", end-start)

if __name__=="__main__":
    main()