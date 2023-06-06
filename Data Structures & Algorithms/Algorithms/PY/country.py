from citynew import City


class Country:
    """
    Federal government class that is inherited off of government class

    Attributes
    ----------

    Methods
    -------
    add_province() -> bool
        Adds a province
    get_province_names() -> list
        Returns a list with all the province names
    get_provinces() -> list
        Returns a list with all the province instances
    """
    def __init__(self, name):
        """
        Constructor to build the federal object

        Parameters
        -----------
        name : str
            The name of the government
        """
        self.name = name
        self.cities = {}

    def add_city(self, name):
        """
        Adds a province to the provinces dict and creates an instance of the province

        Parameters
        -----------
        name : str
            The name of the province

        Returns
        -------
        bool
            True if the method was successful
            False if the province is already in the database
        """
        if name in self.cities:
            # print("This province has already been added to the database")
            return False
        self.cities[name] = City(name)
        return True

    def get_city_names(self):
        """
        Returns the province names of the country

        Returns
        -------
        list : The names of all the provinces
        """
        li = []
        for city in self.cities:
            li.append(city)
        return li

    def get_cities(self):
        """
        Returns the province objects of the country

        Returns
        -------
        list : The instances of all the provinces
        """
        li = []
        for city in self.cities:
            li.append(self.cities[city])
        return li



