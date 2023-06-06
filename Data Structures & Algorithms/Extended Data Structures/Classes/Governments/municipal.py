from government import Government


class City(Government):
    """
    A city object that stores information about a city

    Attributes
    ----------
    _neighbours : list
        Stores all neighbouring cities (cities with direct roads connecting them)
    transit : float
        transit spending

    Methods
    --------
    add_neighbour(city : str) -> None
        Adds a city into its neighbouring list
    get_neighbours() -> list
        Returns a list with all its neighbours
    set_transit_spending() -> None
        Sets the transit spending amount
    get_transit_spending() -> float
        amount of city's transit spending
    """
    def __init__(self, name, leader=None, tax=0, transit=0):
        """
        Constructor to build the city object

        Parameters
        -----------
        name : str
            The name of the city
        """
        super().__init__(name, leader, tax)
        self.transit = transit
        self._neighbours = []

    def add_neighbour(self, city):
        """
        Appends a city to its neighbouring list

        Parameters
        -----------
        city : str
            The city that is connected with the current city
        """
        self._neighbours.append(city)
        return

    def get_neighbours(self):
        """
        Returns the city's neighbours

        Returns
        -------
        list : list of the city's neighbours
        """
        return self._neighbours

    def set_transit_spending(self, amount):
        """
        Sets the city's transit spending

        Parameters
        -------
        amount : amount of city's transit spending
        """
        self.transit = amount

    def get_transit_spending(self):
        """
        Returns the city's transit spending

        Returns
        -------
        float : amount of city's transit spending
        """
        return self.transit
