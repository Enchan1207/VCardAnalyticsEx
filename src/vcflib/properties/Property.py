#
# vCardプロパティ
#
from typing import Dict, List, Union

class Property():

    """
    連絡先カードの情報を管理するデータクラスです。
    """

    def __init__(self, name: str = "", parameters: Dict[str, Union[str, List[str]]] = {}, value: bytes = bytes()) -> None:
        self.name: str = name
        self.parameters: Dict[str, Union[str, List[str]]] = parameters
        self.value: bytes = value

    def __str__(self) -> str:
        class_name = self.__class__.__name__
        prop_list = [f"{key}: {self.parameters[key]}" for key in self.parameters.keys()]

        return f"{class_name} (properties: {','.join(prop_list)})"

    def __eq__(self, o: object) -> bool:
        if not issubclass(type(o), Property):
            return False
        
        return self.name == o.name
