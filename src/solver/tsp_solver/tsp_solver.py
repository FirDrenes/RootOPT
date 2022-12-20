import requests
import polyline

from src.solver.tsp_solver.annealing_algorithm import SimulatedAnnealAlgorithm


def get_route(start_lon, start_lat, end_lon, end_lat):
    """
    Function getting info about path and distance between two towns
    :param start_lon: longitude of start town
    :param start_lat: latitude of start town
    :param end_lon: longitude of end town
    :param end_lat: latitude of end town
    :return: dictionary info about path and distance between two towns
    """
    loc = "{},{};{},{}".format(start_lon, start_lat, end_lon, end_lat)
    url = "http://router.project-osrm.org/route/v1/driving/"
    r = requests.get(url + loc)
    res = r.json()
    routes_ = polyline.decode(res['routes'][0]['geometry'])
    start_point = [res['waypoints'][0]['location'][1], res['waypoints'][0]['location'][0]]
    end_point = [res['waypoints'][1]['location'][1], res['waypoints'][1]['location'][0]]
    distance = res['routes'][0]['distance']

    out = {'route': routes_,
           'start_point': start_point,
           'end_point': end_point,
           'distance': distance
           }

    return out


class TSPSolver(object):
    """
    Class solving TSP problem for user
    """

    def __init__(self, towns_dict, start_town=None):
        """
        Constructor TSPSolver
        :param towns_dict: dictionary with data about names, longitude and latitude
        :param start_town: name of the starting town
        """
        self.algorithm_result = None
        self.result_dict = None
        self.info_routes = []
        self.towns_data = towns_dict
        if start_town is None:
            self.start_town = towns_dict[0]['name']
        else:
            self.start_town = start_town

    def get_distance_info(self):
        """
        Create info about distances and paths between towns
        """
        for i in range(len(self.towns_data) - 1):
            for j in range(i + 1, len(self.towns_data)):
                test_route = get_route(self.towns_data[i]['longitude'],
                                       self.towns_data[i]['latitude'],
                                       self.towns_data[j]['longitude'],
                                       self.towns_data[j]['latitude'])
                distance_ = test_route['distance'] / 1000
                route_ = [tuple(test_route['start_point'])]
                route_ += test_route['route']
                route_.append(tuple(test_route['end_point']))
                self.info_routes.append({'start': self.towns_data[i]['name'], 'end': self.towns_data[j]['name'],
                                         'distance': distance_, 'route': route_})

    def start_algorithm(self):
        """
        Function starts simulated annealing algorithm
        """
        SimulatedAnneal = SimulatedAnnealAlgorithm(start_point=self.start_town,
                                                   towns_dist_info=self.info_routes,
                                                   towns_list=self.towns_data,
                                                   stopping_iter=5000)
        SimulatedAnneal.anneal()
        self.algorithm_result = SimulatedAnneal.get_result()

    def make_result_dictionary(self):
        """
        Function make a dict by the result of algorithm
        """
        towns_path = []
        path = []
        for i in range(len(self.algorithm_result['best_route']) - 1):
            towns_path.append(self.towns_data[self.algorithm_result['best_route'][i]]['name'])
            for route_info in self.info_routes:
                if self.towns_data[self.algorithm_result['best_route'][i]]['name'] == route_info['start'] \
                        and self.towns_data[self.algorithm_result['best_route'][i + 1]]['name'] == route_info['end']:
                    path_between = route_info['route'][0:(len(route_info['route']) - 1)]
                    path += path_between
                elif self.towns_data[self.algorithm_result['best_route'][i]]['name'] == route_info['end'] \
                        and self.towns_data[self.algorithm_result['best_route'][i + 1]]['name'] == route_info['start']:
                    path_between = route_info['route'][1:(len(route_info['route']))]
                    path_between.reverse()
                    path += path_between
        towns_path.append(self.towns_data[self.algorithm_result['best_route'][0]]['name'])
        self.result_dict = {"towns": towns_path, "distance": self.algorithm_result['distance'], "path": path}

    def get_result(self):
        """
        Main function to get a result of simulated annealing algorithm
        :return: dictionary with list of towns, distance, path
        """
        self.get_distance_info()
        self.start_algorithm()
        self.make_result_dictionary()
        return self.result_dict
