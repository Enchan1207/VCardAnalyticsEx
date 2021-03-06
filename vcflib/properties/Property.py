#
# vCardプロパティ
#
from typing import Dict, List, Union

class Property():

    def __init__(self, name: str = "", parameters: Dict[str, Union[str, List[str]]] = {}, value: bytes = bytes()) -> None:
        self.name: str = name
        self.parameters: Dict[str, Union[str, List[str]]] = parameters
        self.value: bytes = value
