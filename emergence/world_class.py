#!/usr/bin/python

from fsa import *

# map of world, contains xy location of each entity

class world:

    def  __init__(self, size):
        self.map = [[0 for i in range(size)] for i in range(size)]
        self.size = size


    def print_map(self):
        print("World looks like:")
        for i in range(self.size):
          print(self.map[i])

    def insert_agent(self, agent):
        self.map[agent.x][agent.y] = agent

    def update_map(self):
        for row in self.map:
            for space in row:
                if space:
                    
                    new_coords = space.update_rules(5)
