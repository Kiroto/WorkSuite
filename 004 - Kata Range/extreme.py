class Extreme:
    def __init__(self: 'Extreme', value: int, isOpen: bool) -> None:
        if type(value) is not int:
            raise TypeError(value)
        if type(isOpen) is not bool:
            raise TypeError(isOpen)
        
        self.value : int = value
        self.isOpen : bool = isOpen