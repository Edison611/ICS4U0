from road import Road


class Highway(Road):
    """
    Highway Class

    Attributes
    ----------
    toll : float
        The toll amount

    Methods
    -------
    set_toll() -> None
        Sets the toll amount of a highway
    get_toll() -> float
        The toll amount on the highway
    """
    def __init__(self, length, lanes=2, material="asphalt", speed_limit=100, name="None", toll=0):
        super().__init__(length, lanes, material, speed_limit, name)
        self.toll = toll

    def set_toll(self, toll):
        self.toll = toll

    def get_toll(self):
        if self.toll > 0:
            return f"The toll on this road is ${self.toll}"
        else:
            return f"There is no toll on this road"
