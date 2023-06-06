from government import Government
from provincial import Province


class Federal(Government):
    """
    Federal government class that is inherited off of government class

    Attributes
    ----------
    defense : float
        The defense spending in a percent
    provinces : dict
        A dictionary to store all the province instances

    Methods
    -------
    add_province() -> bool
        Adds a province
    get_province_names() -> list
        Returns a list with all the province names
    get_provinces() -> list
        Returns a list with all the province instances
    get_defense_spending() -> float
        Returns a list
    """
    def __init__(self, name, leader=None, tax=0, gdp=0, defense=0):
        """
        Constructor to build the federal object

        Parameters
        -----------
        name : str
            The name of the government
        leader : str
            The leader of the government
        tax : int
            The percentage tax of the government
        gdp : int
            The gdp of the government
        defense : float
            The percentage of defense spending
        """
        super().__init__(name, leader, tax, gdp)
        self.defense = defense
        self.provinces = {}

    def add_province(self, name):
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
        if name in self.provinces:
            print("This province has already been added to the database")
            return False
        self.provinces[name] = Province(name)
        return True

    def get_province_names(self):
        """
        Returns the province names of the country

        Returns
        -------
        list : The names of all the provinces
        """
        li = []
        for province in self.provinces:
            li.append(province)
        return li

    def get_provinces(self):
        """
        Returns the province objects of the country

        Returns
        -------
        list : The instances of all the provinces
        """
        li = []
        for province in self.provinces:
            li.append(self.provinces[province])
        return li

    def set_defense_spending(self, amount):
        """
        sets the defense spending of the country

        Parameters
        -------
        amount : float
            The defense spending of the country
        """
        self.defense = amount

    def get_defense_spending(self):
        """
        Returns the defense spending of the country

        Returns
        -------
        float : The defense spending of the country
        """
        # print(f"The defense spending of {self.get_name()} is {self.defense}%")
        return self.defense
