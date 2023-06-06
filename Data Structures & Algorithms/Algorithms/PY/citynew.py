class City:
    """
    A city object that stores information about a city

    Attributes
    ----------
    name : str
        The name of the city
    population : int
        The number of people living in the city

    Methods
    --------
    set_population(population : int) -> boolean
        Sets the city's population and makes sure it cannot be negative
    change_population(change : int) -> boolean
        Changes the city's population by the given amount
    get_population() -> int
        Returns the city's population
    get_name() -> str
        Returns the name of the city
    """
    def __init__(self, name, population=0):
        """
        Constructor to build the city object

        Parameters
        -----------
        name : str
            The name of the city
        population : int
            The population of the city
        """
        # self._neighbours = []
        self.name = name
        self.population = population

    def set_population(self, population):
        """
        Sets the population of a city

        Parameters
        -----------
        population : int
            The population of the city

        Returns
        -------
        bool
            True if the method was successful
            False if the method set the population to lower than 0
        """

        population = int(population)
        if population < 0:
            print("Please enter a population greater than 0")
            return False
        self.population = population
        return True

    def change_population(self, change):
        """
        Changes (increase/decrease) the population of a city from its previous value

        Parameters
        -----------
        change : int
            The change in population of a city

        Returns
        -------
        bool
            True if the method was successful
            False if the method changes the population to lower than 0
        """
        change = int(change)
        self.population += change
        if self.population < 0:
            self.population -= change
            print("Population must be greater than 0")
            return False
        return True

    def get_population(self):
        """
        Returns the city's population

        Returns
        -------
        int : The city's population
        """
        return self.population

    def get_name(self):
        """
        Returns the city's name

        Returns
        -------
        str : the city's name
        """
        return self.name
