
class Stats:
    """
    The statistics of a government which this class manages.

    Attributes
    -----------
    level : str
        The level of government
    population : int
        The population of the government
    density : float
        The density of the city
    timezone : str
        The timezone of the city

    Methods
    --------
    set_population(population : int) -> boolean
        Sets the city's population and makes sure it cannot be negative
    get_population(list) -> int
        Returns the population of the city, province or country
    set_density(dense : float) -> None
        sets density of the city
    get_density() -> float
        gets density of the city
    set_timezone(time : str) -> None
        sets the timezone of the city
    get_timezone() -> str
        gets the timezone of the city
    """
    def __init__(self, level, population=0, density=0, timezone=None):
        self.level = level
        self.population = population
        self.density = density
        self.timezone = timezone

    def set_population(self, population):
        """
        Sets the population

        Parameters
        -----------
        population : int
            The population

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

    def get_population(self, obj=[]):
        """
        Gets the population of the government

        Parameters
        ----------
        obj : list
            a list with instances of governments

        Returns
        --------
        int : The population of the government
        """
        pop = 0
        if self.level == "Federal":
            for province in obj:
                pop += province.get_info().get_population(province.get_cities())
            return pop
        elif self.level == "Province":
            for city in obj:
                pop += city.get_info().get_population()
            return pop
        elif self.level == "City":
            return self.population
        return None

    def set_density(self, dense):
        """
        Sets the density of the city

        Parameters
        ----------
        dense : float
        """
        self.density = dense

    def get_density(self):
        """
        Returns the density of the city

        Returns
        -------
        float : The density of the city
        """
        return self.density

    def set_timezone(self, time):
        """
        Sets the timezone of the city

        Parameters
        ----------
        time : str
        """
        self.timezone = time

    def get_timezone(self):
        """
        Returns the timezone of the city

        Returns
        -------
        str : The timezone of the city
        """
        return self.timezone

