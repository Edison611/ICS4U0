class Road:
    """
    A Road object that can store properties and information about the road

    Attributes
    ----------
    _length : float
        The length of the road
    _lanes : int
        The number of lanes on the road
    _material : str
        The material the road is made out of
    _speed_limit : int
        The speed limit on the road
    _name : str
        The name of the road

    Methods
    --------
    set_length(length : float) -> None
        sets length of the road
    get_length() -> float
        gets length of the road
    set_lanes(lanes : int) -> None
        sets lanes of the road
    get_lanes() -> int
        gets lanes of the road
    set_material(material : str) -> None
        sets material of the road
    get_material() -> str
        gets material of the road
    set_speed_limit(speed_limit : int) -> None
        sets speed limit of the road
    get_speed_limit() -> int
        gets speed limit of the road
    set_name(name : str) -> None
        sets name of the road
    get_name() -> str
        gets name of the road
    """

    def __init__(self, length, lanes=None, material=None, speed_limit=None, name=None):
        """
        Constructor to build the province object

        Parameters
        -----------
        length : int, float
            The length of the road
        lanes : int
            The number of lanes on the road
        material : str
            The material the road is made of
        speed_limit : int
            The speed limit on the road
        name : str
            The name of the road
        """
        self._length = length
        self._lanes = lanes
        self._material = material
        self._speed_limit = speed_limit
        self._name = name
        return

    def set_length(self, length):
        """
        Sets the length of the road

        Parameters
        ----------
        length : int, float
        """
        self._length = length
        return

    def get_length(self):
        """
        Returns the length of the road

        Returns
        -------
        int, float : The length of the road
        """
        return self._length

    def set_lanes(self, lanes):
        """
        Sets the lanes of the road

        Parameters
        ----------
        lanes : int
        """
        self._lanes = lanes

    def get_lanes(self):
        """
        Returns the lanes of the road

        Returns
        -------
        int : The lanes of the road
        """
        return self._lanes

    def set_material(self, material):
        """
        Sets the material of the road

        Parameters
        ----------
        material : str
        """
        self._material = material

    def get_material(self):
        """
        Returns the material of the road

        Returns
        -------
        str : The material of the road
        """
        return self._material

    def set_speed_limit(self, speed_limit):
        """
        Sets the speed limit of the road

        Parameters
        ----------
        speed_limit : int
        """
        self._speed_limit = speed_limit

    def get_speed_limit(self):
        """
        Returns the speed limit of the road

        Returns
        -------
        int : The speed limit of the road
        """
        return self._speed_limit

    def set_name(self, name):
        """
        Sets the name of the road

        Parameters
        ----------
        name : str
        """
        self._name = name

    def get_name(self):
        """
        Returns the name of the road

        Returns
        -------
        str : The name of the road
        """
        return self._name
