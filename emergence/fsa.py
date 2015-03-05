#!/usr/bin/python

# finite state machine which travels through space
# has herding behavior - seeks an optimal distance from neighbor
# can only see straight ahead
# orientation goes NESW - 00 is 12 o clock, 01 is 3 o clock, 10 is 6, 11 is 9

class agent:

    def __init__(self, location, orientation):
        self.x = location[0]
        self.y = location[1]
        self.orientation = orientation

    def update_rules(self, dist_from_friend):
        urgency = 2 - dist_from_friend
        
        
        



