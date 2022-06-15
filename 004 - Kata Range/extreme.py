class Extreme:
    def __init__(self: 'Extreme', value: int, open: bool) -> None:
        if type(value) is not int:
            raise TypeError(value)
        if type(open) is not bool:
            raise TypeError(open)
        
        self.value : int = value
        self.open : bool = open