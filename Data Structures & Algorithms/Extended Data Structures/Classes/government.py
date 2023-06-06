from stats import Stats


class Government:
    """
    A government object (parent class) that each type of government needs to have.
    Contains

    Attributes
    ----------
    _name : str
        The name of the government
    _tax : int
        The percentage sales tax of the government
    leader : str
        The leader of the government
    gdp : int
        The gdp of the government in dollars
    type : string
        The level of government
    stats : Stats
        The stats object of the government

    Methods
    --------
    get_type() -> str
        Returns the governments type/level (e.g. Province, Federal)
    get_info() -> Stats
        Returns the stats class (Gives access to the stats class)
    get_name() -> str
        Returns the Government name
    set_tax(tax : int) -> None
        Sets the percentage tax of the government
    get_tax() -> int
        Gets the tax of the government
    set_leader(leader : str) -> None
        Sets the leader of the government
    get_leader() -> str
        Gets the leader of the government
    set_gdp(gdp : int) -> None
        Sets the gdp of the government
    get_gdp() -> int
        Gets the gdp of the government
    """

    def __init__(self, name, leader=None, tax=0, gdp=0):
        """
        Constructor to build the government object

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
        """
        self._name = name
        self._tax = tax
        self.leader = leader
        self.gdp = gdp
        self.type = self.get_type()
        self.stats = Stats(self.type)

    def get_type(self):
        return str(self.__class__.__name__)

    def get_info(self):
        return self.stats

    def get_name(self):
        """
        Returns the name of the province

        Returns
        -------
        str
            The name of the province
        """
        return self._name

    def set_tax(self, amount):
        """
        Sets the tax of the government

        Parameters
        -------
        amount : the amount of sales tax in percentage
        """
        amount = int(amount)
        if amount < 0:
            print("Please enter a population greater than 0")
            return False
        self._tax = amount
        return True

    def get_tax(self):
        """
        Returns the amount of tax of the government

        Returns
        -------
        int : The tax of the government
        """
        return self._tax

    def set_leader(self, name):
        """
        Sets the leader of the government

        Parameters
        -------
        name : The leader of the government
        """
        self.leader = name

    def get_leader(self):
        """
        Returns the leader of the government

        Returns
        -------
        str : The leader of the government
        """
        return self.leader

    def set_gdp(self, gdp):
        """
        Sets the gdp of the government

        Parameters
        -------
        gdp : The gdp of the government
        """
        self.gdp = gdp

    def get_gdp(self):
        """
        Returns the gdp of the government

        Returns
        -------
        int : The gdp of the government
        """
        return self.gdp


