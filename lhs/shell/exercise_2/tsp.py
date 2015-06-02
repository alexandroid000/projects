#!/usr/bin/python -u

import sys
import time
import random
import math
import numpy as np



# TSP class - Solves TSPs several ways
class TSP:
    """Implements solutions to the traveling salesman problem with timing."""

    # Utility functions

    ## Constructor
    def __init__ (self):
        """Call the constructor with a file that contains a city-list."""
        self._solvers = { \
            "gn": "greedy nearest neighbor", \
            "gc": "greedy smallest loop", \
            "gln": "greedy nearest neighbor all starts", \
            "glc": "greedy smallest loop all starts", \
            "rr": "relax random", \
            "rs": "relax sequential", \
            "ex": "exhaustive search"}

    ## Init distances
    def setup (self):
        self._distances = []
        for position in self._positions:
            self._distances.append (
                    [np.sqrt(np.sum((position - pos)**2)) \
                    for pos in self._positions])
        self._num_cities = len(self._positions)
        self._city_list = [i for i in range(self._num_cities)]
        self._curr_path = {"path": self._city_list, \
                            "length": self.path_length_circ(self._city_list)}

    ## Load file
    def load_file (self, filename):
        """Given a filename, reads in the file. Throws away first line, then
            reads a space separated integer pair specifying x,y positions."""
        fin = open(filename)
        self._positions = np.array (
                [[int(val) for val in point.split()] for point in fin])
        fin.close()
        self.setup()

    ## Write file
    def write_file (self, filename):
        """Given a filename, writes the city data to the file. First line is how
            many cities there are, rest are int pairs of x,y positions."""
        fout = open(filename, "w")
        fout.write (str(self._num_cities) + "\n")
        for pos in self._positions:
            fout.write(str(pos[0]) + " " + str(pos[1]) + "\n")
        fout.close()

    ## Generate random data
    def new_data (self, num_cities = 12):
        """Generate random position data, calculates new distances"""
        self._positions = np.array (
                [[random.randint(0, 10000), random.randint(0, 10000)] \
                for i in range (num_cities)])
        self.setup()

    ## To string
    def __str__ (self):
        """Output the data in a string."""
        cp = self._curr_path
        return "Length: {l!s}; Path: {p!s}".format(l=cp["length"], \
                p=cp["path"])


    # Calculation Functions

    ## Non circular path-length of a city-list
    def path_length (self, city_list):
        """Given a list of cities, returns the path-length of it.
            Note that this does not connect the last city to the first."""
        if len(city_list) <= 1:
            return 0
        path_length = 0
        for i in range(len(city_list)-1):
            c0, c1 = city_list[i], city_list[i+1]
            path_length += self._distances[c0][c1]
        return path_length

    ## Circular path-length of a city-list
    def path_length_circ (self, city_list):
        """Given a list of cities, returns the path-length of it.
            Note that this does connect the last city to the first."""
        if len(city_list) <= 1:
            return 0
        extra_dist = self._distances[city_list[0]][city_list[-1]]
        return (self.path_length (city_list) + extra_dist)

    ## Total length to both neighbors of a city
    def neigh_length (self, city_list, pos_list):
        """Given a list of cities and which city to examine, will find the
            summed length between the two neighbors of the city."""
        tot_path = 0
        for pos in pos_list:
            cities = [city_list[pos-1], city_list[pos], \
                    city_list[(pos+1)%len(city_list)]]
            tot_path += self.path_length (cities)
        return tot_path

    ## Swap two cities
    def swap_cities (self, city_list, swap_1, swap_2):
        """Given a list of cities and two indices, swap the cities inplace.
            Returns the difference in circular path length after swap."""
        curr_length = self.neigh_length (city_list, [swap_1, swap_2])
        city_list[swap_1], city_list[swap_2] = \
                city_list[swap_2], city_list[swap_1]
        new_length = self.neigh_length (city_list, [swap_1, swap_2])
        return (new_length - curr_length)

    ## Next Permutation
    def get_next_permutation (self, path):
        if len(path) < 2:
            return path
        cp = path[:]
        i = len(cp) - 1
        while True:
            j = i
            i -= 1
            if (cp[i] < cp[j]):
                k = len(cp) - 1
                while cp[i] > cp[k]:
                    k -= 1
                cp[i], cp[k] = cp[k], cp[i]
                return (cp[0:i+1] + cp[-1:i:-1])
            if i == 0:
                return cp[-1::-1]


    # Solvers

    ## Random
    def solve_random (self, num_tries = 10):
        curr_path = self._city_list[:]
        new_path = self._city_list[:]
        random.shuffle (curr_path)
        curr_len = self.path_length_circ (curr_path)
        for i in range (num_tries):
            random.shuffle (new_path)
            new_len = self.path_length_circ (new_path)
            if new_len < curr_len:
                curr_path = new_path
                curr_len = new_len
        return curr_path

    ## Relax
    def solve_relax (self, num_attempts = 10000, seq = False):
        nc = self._num_cities
        cp = self._curr_path["path"][:]
        for i in range (num_attempts):
            swap_1 = (int(i / nc) % nc) if seq else random.randrange (nc)
            swap_2 = (i % nc) if seq else random.randrange (nc)
            path_len_diff = self.swap_cities (cp, swap_1, swap_2)
            if path_len_diff > 0:
                self.swap_cities (cp, swap_1, swap_2)
        self._curr_path["path"] = cp[:]
        self._curr_path["length"] = self.path_length_circ(cp)

    ## Relax Random and Sequential default wrappers
    def rr (self):
        self.solve_relax (num_attempts = (self._num_cities**2), seq = False)
    def rs (self):
        self.solve_relax (num_attempts = (self._num_cities**2), seq = True)


    ## Exaustive
    def solve_exhaustive (self, nt = None):
        nt = math.factorial(self._num_cities) if nt is None else nt
        curr_path = self._curr_path["path"]
        curr_len = self._curr_path["length"]
        for i in range(nt):
            curr_path = self.get_next_permutation (curr_path)
            curr_len = self.path_length_circ(curr_path)
            if curr_len < self._curr_path["length"]:
                self._curr_path["path"] = curr_path[:]
                self._curr_path["length"] = curr_len

    ## Exhaustive default wrapper
    def ex (self):
        self.solve_exhaustive (nt = math.factorial(self._num_cities))

    ## Greedy Solver
    ## Objective functions for greedy search
    def obj_near_neigh (self, curr_cities, next_city, reverse = False):
        """Return the distance from the last city to the next city.
            Set reverse to True to use the reverse of curr_cities."""
        curr_city = curr_cities[0] if reverse else curr_cities[-1]
        return self._distances[curr_city][next_city]

    def obj_small_loop (self, curr_cities, next_city):
        return self.obj_near_neigh(curr_cities, next_city) + \
                self.obj_near_neigh(curr_cities, next_city, reverse = True) - \
                self._distances[curr_cities[0]][curr_cities[-1]]

    ## Generic greedy solver
    def greedy (self, start_city, objective_function = obj_near_neigh):
        """Use the greedy algorithm to solve TSP from specified city.
            <start_city>: Start solve_greedy at this city.
            <objective_function>: Function which takes a list of the current
                cities and a potential next city and returns the cost of that
                new city."""
        curr_path = [start_city]
        visited_city = [False for i in self._city_list]
        visited_city[start_city] = True
        while len(curr_path) < self._num_cities:
            next_cities = [(c, objective_function (curr_path, c)) \
                            for c in self._city_list \
                            if not visited_city[c]]
            next_city = next_cities[0]
            for next_c in next_cities:
                if next_c[1] < next_city[1]:
                    next_city = next_c
            next_city = next_city[0]
            curr_path.append(next_city)
            visited_city[next_city] = True
        self._curr_path = {"path": curr_path, \
                            "length": self.path_length_circ(curr_path)}

    ## Apply greedy solver to a list of elements
    def greedy_list (self, start_cities = None, obj_func = obj_near_neigh):
        """Use the greedy algorithm on the TSP from a list of specified cities.
            <start_cities>: List of cities to try starting 'solve_greedy' at.
            <obj_func>: Objective function to pass to 'solve_greedy'"""
        start_cities = start_cities if start_cities is not None \
                                    else self._city_list
        self.solve_greedy(start_c, objective_function = obj_func)
        curr_path = None
        best_len = None
        for start_c in start_cities:
            self.solve_greedy(start_c, objective_function = obj_func)
            new_len = self._curr_path["length"]
            if best_len is None or new_len < best_len:
                curr_path = self._curr_path["path"]
                best_len = new_len
        self._curr_path = {"path": curr_path, \
                            "length": self.path_length_circ(curr_path)}

    ## Greedy solver default wrappers
    def gn (self):
        self.greedy (0, objective_function = self.obj_near_neigh)
    def gc (self):
        self.greedy (0, objective_function = self.obj_small_loop)
    def gln (self):
        self.greedy_list (start_cities = None, obj_func = self.obj_near_neigh)
    def glc (self):
        self.greedy_list (start_cities = None, obj_func = self.obj_small_loop)


    # Wrapper Solvers

    ## Solve using a string which defines the solve method
    def solve (self, solve_method, randomize = True, quiet = False):
        """Call the tsp solvers based on <solve_method>.
            Returns: True (self._curr_path set), False (self._curr_path
                unchanged).
            <solve_method>: String containing solving techniques to use. Can
            take output of one and feed into another with a pipe '|' to string
            together solvers.
            Ex: tsp.solve ("gn|rr")   # use greedy neighbor then relax rand."""
        solvers = solve_method.replace(" ", "").split("|")
        for solver in solvers:
            if solver not in self._solvers:
                return False
            if randomize:
                self.solve_random()
            getattr (self, solver)()
        return True

    ## Solve using a string which defines the solve method, but times it
    def solve_stat (self, solver, repeat = 100, num_cities = None, quiet = False):
        """Call the solve method <repeat> times in a timer."""
        if num_cities is not None:
            self.new_data (num_cities = num_cities)
        start_time = time.time()
        solns = [self._curr_path for i in range(repeat) \
                if self.solve (solver, quiet = True)]
        soln_time = (time.time() - start_time)/repeat
        mean_path_length = np.mean ([soln["length"] for soln in solns])
        data = [self._num_cities, solver, mean_path_length, soln_time]
        if not quiet:
            print (" ".join([str(dat) for dat in data]))
        return data


    # Default demo functions

    ## Try out each solver on some different sized input
    def demo_1 (self):
        print ("num_cities solver mean_path_length soln_time")
        solvers = "ex gn gn|rr"
        sizes = [i for i in range(1,10)]
        for size in sizes:
            self.new_data (num_cities = size)
            for solver in solvers.split():
                self.solve_stat(solver, repeat = 10)
        solvers = "gn gn|rr"
        sizes = [i for i in range(5, 1410, 200)]
        for size in sizes:
            self.new_data (num_cities = size)
            for solver in solvers.split():
                self.solve_stat(solver, repeat = 10)

    ## Run various solvers on a specific input
    def demo_2 (self, filename):
        self.load_file (filename)
        solvers = "gn gc rr rs gn|rr" if self._num_cities >= 10 \
                else "gn gc rr rs ex gn|rr"
        print ("num_cities solver mean_path_length soln_time")
        for solver in solvers.split():
            self.solve_stat(solver)


# Get a TSP
tsp_solve = TSP()

# No arguments, run TSP_test1
if len(sys.argv) < 2:
    tsp_solve.demo_1()
    sys.exit(0)

# One argument, run test2
filename = sys.argv[1]
if len(sys.argv) < 3:
    tsp_solve.demo_2(filename)
    sys.exit(0)

# Three arguments, use third as solver
solvers = sys.argv[2]
tsp_solve.load_file (filename)
for solver in solvers.split():
    tsp_solve.solve_stat(solver)
sys.exit(0)
