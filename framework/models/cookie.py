class Cookie:
    def __init__(self, name: str, value: str):
        self.__name = name
        self.__value = value

    @property
    def name(self) -> str:
        return self.__name

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, new_value: str):
        self.__value = new_value
