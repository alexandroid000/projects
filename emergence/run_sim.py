#!/usr/bin/python

from world_class import *
from fsa import *

test = world(5)

agent1 = agent([1,1],1)
test.insert_agent(agent1)
test.print_map()
test.update_map()
