import logging
from municipal import City
from highway import Highway
from government import Government

# logging.basicConfig(filename='../../Output Files/log.txt', level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
# logging.info("NEW TEST: ")


class Province(Government):
    """
    A province object that holds information about cities and roads that connect them together

    We construct a sort of graph that has nodes (cities) and edges (roads) that each has its own
    separate properties. We can then use this data from the graph to perform operations using
    graph theory that can be useful for the real world.

    Attributes
    ----------
    cities : dict
        Stores all cities
    _roads : dict
        Stores all roads connecting cities

    Methods
    --------
    access_city(city : str) -> City []
        Gives access to the object in the City class
    add_city(name : str) -> boolean
        Adds a city in the Province
    add_road(city1 : str, city2 : str, length : float) -> boolean
        Adds a road connecting two cities
    get_roads() -> dict
        Returns all roads within the Province
    get_city_names() -> list
        Returns a list with all the city names
    get_cities() -> list
        Returns a list with all the city instances
    shortest_path(city1 : str, city2 : str, file : str) -> boolean
        Finds the shortest path from city1 to city2 and writes the results in a file
    """
    def __init__(self, name, leader=None, tax=0, gdp=0, health=0):
        """
        Constructor to build the province object

        Parameters
        -----------
        name : str
            The name of the province
        """
        super().__init__(name, leader, tax, gdp)

        self.cities = {}
        self._roads = {}

    def access_city(self, city):
        """
        Gives access to the methods in a City object

        Parameters
        -----------
        city : str
            The selected city

        Returns
        -------
        City []
            The City object
        """
        return self.cities[city]

    def add_city(self, name):
        """
        Adds a city to the cities dict and creates an instance of the city

        Parameters
        -----------
        name : str
            The name of the city

        Returns
        -------
        bool
            True if the method was successful
            False if the city is already in the database
        """
        if name in self.cities:
            print("This city has already been added to the database")
            return False
        self.cities[name] = City(name)
        return True

    def add_road(self, city1, city2, length, lanes=None, material=None, speed_limit=None, name=None):
        """
        Adds a road connecting 2 cities with a set length

        Parameters
        -----------
        city1 : str
            The name of the first city
        city2 : str
            The name of the second city
        length : float, int
            The distance of the road
        lanes : int
            Number of lanes
        material : str
            material of road
        speed_limit : int
            speed limit of road
        name : str
            name of the road

        Returns
        -------
        bool
            True if the method was successful
            False if a city is not in database or if length is negative
        """
        if city1 not in self.cities or city2 not in self.cities:
            logging.error("One of the cities you chose is not in the database")
            print("One of the cities you chose is not in the database")
            return False
        if length < 0:
            logging.error("You cannot have a negative length")
            print("You cannot have negative length")
            return False
        self.cities[city1].add_neighbour(city2)
        self.cities[city2].add_neighbour(city1)
        if city1 < city2:
            self._roads[(city1, city2)] = Highway(length, lanes, material, speed_limit, name)
        else:
            self._roads[(city2, city1)] = Highway(length, lanes, material, speed_limit, name)
        return True

    def get_roads(self):
        """
        Returns the roads dict

        Returns
        -------
        dict
            The dict holding the Road objects
        """
        return self._roads

    def get_city_names(self):
        """
        Returns a list with all the cities in the province

        Returns
        -------
        list
            List of the names of cities
        """
        cities = []
        for city in self.cities:
            cities.append(city)

        return cities

    def get_cities(self):
        """
        Returns a list with all the cities in the province

        Returns
        -------
        list
            List of the names of cities
        """
        cities = []
        for city in self.cities:
            cities.append(self.cities[city])

        return cities

    def shortest_path(self, city1, city2, file):
        """
        Finds the shortest path from 2 cities

        Uses a variation of Dijkstra's algorithm to find the shortest path
        between 2 Nodes in a graph. We start from city1 and choose the shortest road from
        its neighbours.We mark the newly visited city into the visited_cities array and
        find the shortest road from each visited city to each neighbouring city.

        Parameters
        -----------
        city1 : str
            The name of the first city
        city2 : str
            The name of the second city
        file : str
            The name of the output file

        Returns
        -------
        bool
            True if there is a path between city1 and city2
            False if there is no path between city1 and city2
        """
        f = open("/Users/edisony611/Documents/School/Computer Science 12/ICS4U0/Data Structures & Algorithms/Extended Data Structures/Output Files/" + file, "w")
        visited_path = {}
        visited_cities = {city1: 0}
        path = True

        # Finds the shortest path between city1 and city2
        while True:
            logging.info("-------------------")
            if city2 in visited_cities:
                break
            logging.info("Visited Cities: " + str(visited_cities))
            min_road = 9999999
            min_city = ""
            new_neighbours = 0
            # Finds the shortest road within all neighbouring cities
            for city in visited_cities:
                neighbours = self.cities[city].get_neighbours()
                logging.info("Neighbours: " + str(neighbours))
                for neighbour in neighbours:
                    if neighbour in visited_cities:
                        continue
                    new_neighbours += 1
                    if city < neighbour:
                        length = self._roads[(city, neighbour)].get_length()
                    else:
                        length = self._roads[(neighbour, city)].get_length()
                    length += visited_cities[city]
                    if length < min_road:
                        origin = city
                        min_road = length
                        min_city = neighbour
                logging.info("-------------------")
            # Checks if there is no neighbours meaning no path can be found
            if new_neighbours == 0:
                logging.info("No paths can be found")
                path = False
                break

            visited_path[min_city] = origin
            visited_cities[min_city] = min_road

            # Logging
            logging.info("Decisions : ---------")
            logging.info('Origin: ' + str(origin))
            logging.info('Minimum Road Length: ' + str(min_road))
            logging.info('City chosen: ' + str(min_city))

        if not path:
            f.write("There is no way to get from " + city1 + " to " + city2 + "\n")
            return False

        # Calculates the path taken to go from city1 to city2
        current = city2
        journey = []
        while True:
            journey.insert(0, current)
            if current == city1:
                break
            current = visited_path[current]

        # Prints the results onto an output file
        f.write("The shortest path from " + city1 + " to " + city2 + " is: \n")
        f.write("Start at " + city1 + "\n")
        for i in range(len(journey)):
            if i == len(journey) - 1:
                break

            if journey[i] < journey[i+1]:
                road = (journey[i], journey[i+1])
            else:
                road = (journey[i+1], journey[i])
            f.write(f"From {journey[i]} go to {journey[i+1]} on Highway {self._roads[road].get_name()} ({str(self._roads[road].get_length())})" + "\n")
            f.write(f"The speed limit on this road is {self._roads[road].get_speed_limit()}" + "\n")
            f.write(f"{self._roads[road].get_toll()} \n")
            f.write("\n")
        f.write("The length of this journey would be " + str(visited_cities[city2]) + "\n")
        f.write("----------------------------------------------------------")
        f.close()

        return True

