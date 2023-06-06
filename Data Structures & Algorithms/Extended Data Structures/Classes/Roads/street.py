from road import Road


class Street(Road):
    """
    Street Class
    """
    def __init__(self, length, lanes=2, material="asphalt", speed_limit=50, name=None):
        super().__init__(length, lanes, material, speed_limit, name)