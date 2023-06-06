from country import Country


class World:
    """
    World class

    Attributes
    ----------
    countries : dict
        Stores all countries

    Methods
    --------
    add_country(name : str) -> boolean
        Adds a city in the Province
    total_population() -> int
        Returns the total population of the province
    get_cities() -> list
        Returns a list with all the city names
    """
    def __init__(self):
        """
        Constructor to build the world object
        """
        self.countries = {}

    def add_country(self, name):
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
        if name in self.countries:
            # print("This country has already been added to the database")
            return False
        self.countries[name] = Country(name)
        return True

    # def total_population(self):
    #     """
    #     Adds the population of each city to get the total population of a province
    #
    #     Returns
    #     -------
    #     int
    #         The total population of the province
    #     """
    #     total = 0
    #     for city in self.cities:
    #         total += self.cities[city].get_population()
    #     return total

    def get_countries(self):
        """
        Returns a list with all the cities in the province

        Returns
        -------
        list
            List of the names of cities
        """
        countries = []
        for country in self.countries:
            countries.append(self.countries[country])

        return countries

    def get_country_names(self):
        """
        Returns a list with all the cities in the province

        Returns
        -------
        list
            List of the names of cities
        """
        countries = []
        for country in self.countries:
            countries.append(country)

        return countries

    def get_city_amount(self):
        total = 0
        for country in self.countries:
            total += len(self.countries[country].get_cities())
        return total

