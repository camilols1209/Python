class Color:
    def __init__(self,color) -> None:
        self.__color=color
        pass

    @property
    def color(self):
        return self.__color
    
    @color.setter
    def color(self,color):
        self.__color=color
        pass
    pass