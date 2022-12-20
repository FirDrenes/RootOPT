import math
import random


class SimulatedAnnealAlgorithm(object):
    """
            Class solving TSP problem by using simulated annealing algorithm
    """

    def __init__(self, start_point, towns_dist_info, towns_list, T=-1, alpha=-1, stopping_T=-1, stopping_iter=-1):
        """
        Constructor of the SimulatedAnnealAlgorithm class
        :param start_point: index of first town
        :param towns_dist_info: data with distances between towns
        :param towns_list: data with towns names
        :param T: starting temperature
        :param alpha: temperature coefficient
        :param stopping_T: stopping temperature
        :param stopping_iter: max iterations
        """
        self.cur_solution = None
        self.cur_fitness = None
        self.start_point = start_point
        self.towns = towns_list
        self.towns_dist_info = towns_dist_info
        self.N = len(towns_list)
        self.T = math.sqrt(self.N) if T == -1 else T
        self.T_save = self.T  # save initial T to reset if batch annealing is used
        self.alpha = 0.995 if alpha == -1 else alpha
        self.stopping_temperature = 1e-8 if stopping_T == -1 else stopping_T
        self.stopping_iter = 100000 if stopping_iter == -1 else stopping_iter
        self.iteration = 1

        self.nodes = [i for i in range(self.N)]

        self.best_solution = None
        self.best_fitness = float("Inf")
        self.fitness_list = []

    def initial_solution(self):
        """
        Greedy algorithm to get an initial solution (closest-neighbour).
        """
        cur_node = random.choice(self.nodes)  # start from a random node
        solution = [cur_node]

        free_nodes = set(self.nodes)
        free_nodes.remove(cur_node)
        while free_nodes:
            next_node = min(free_nodes, key=lambda x: self.dist(cur_node, x))  # nearest neighbour
            free_nodes.remove(next_node)
            solution.append(next_node)
            cur_node = next_node

        cur_fit = self.fit(solution)
        if cur_fit < self.best_fitness:  # If best found so far, update best fitness
            self.best_fitness = cur_fit
            self.best_solution = solution
        self.fitness_list.append(cur_fit)
        return solution, cur_fit

    def dist(self, node_0, node_1):
        """
        Get distance between two nodes.
        """
        town_0 = self.towns[node_0]['name']
        town_1 = self.towns[node_1]['name']
        for coord in self.towns_dist_info:
            if coord['start'] == town_0 and coord['end'] == town_1 \
                    or coord['end'] == town_0 and coord['start'] == town_1:
                return coord['distance']

    def fit(self, solution):
        """
        Total distance of the current solution path.
        """
        cur_fit = 0
        for i in range(self.N):
            cur_fit += self.dist(solution[i % self.N], solution[(i + 1) % self.N])
        return cur_fit

    def probability_accept(self, candidate_fitness):
        """
        Probability of accepting if the candidate is worse than current.
        Depends on the current temperature and difference between candidate and current.
        """
        return math.exp(-abs(candidate_fitness - self.cur_fitness) / self.T)

    def accept(self, candidate):
        """
        Accept with probability 1 if candidate is better than current.
        Accept with probability p_accept(..) if candidate is worse.
        """
        candidate_fitness = self.fit(candidate)
        if candidate_fitness < self.cur_fitness:
            self.cur_fitness, self.cur_solution = candidate_fitness, candidate
            if candidate_fitness < self.best_fitness:
                self.best_fitness, self.best_solution = candidate_fitness, candidate
        else:
            if random.random() < self.probability_accept(candidate_fitness):
                self.cur_fitness, self.cur_solution = candidate_fitness, candidate

    def anneal(self):
        """
        Execute simulated annealing algorithm.
        """
        # Initialize with the greedy solution.
        self.cur_solution, self.cur_fitness = self.initial_solution()

        while self.T >= self.stopping_temperature and self.iteration < self.stopping_iter:
            candidate = list(self.cur_solution)
            first_index = random.randint(2, self.N - 1)
            second_index = random.randint(0, self.N - first_index)
            candidate[second_index: (second_index + first_index)] \
                = reversed(candidate[second_index: (second_index + first_index)])
            self.accept(candidate)
            self.T *= self.alpha
            self.iteration += 1

            self.fitness_list.append(self.cur_fitness)

    def batch_anneal(self, times=10):
        """
        Execute simulated annealing algorithm times, with random initial solutions.
        """
        for i in range(1, times + 1):
            print(f"Iteration {i}/{times} -------------------------------")
            self.T = self.T_save
            self.iteration = 1
            self.cur_solution, self.cur_fitness = self.initial_solution()
            self.anneal()

    def get_result(self):
        """
        Returns result of the algorithm
        """
        while self.towns[self.best_solution[0]]['name'] != self.start_point:
            self.best_solution = self.best_solution[1:len(self.best_solution)] \
                                 + [self.best_solution[0]]
        self.best_solution.append(self.best_solution[0])
        return {'best_route': self.best_solution, 'distance': self.best_fitness}
