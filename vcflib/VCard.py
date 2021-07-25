#
# vCardオブジェクト
#
from typing import List, Union
from vcflib.properties.Property import Property
from vcflib.properties.VersionProperty import VersionProperty
from vcflib.properties.FullNameProperty import FullNameProperty
class VCard():

    def __init__(self, version: str="4.0", properties: List[Property] = []) -> None:
        self.__properties: List[Property] = properties
        self.addProperty(VersionProperty(version))

    def getProperties(self) -> List[Property]:
        return self.__properties

    def addProperty(self, property: Property, overwrite: bool = False):
        # 既存のものと名前が被らなければ追加
        if self.getPropertyByName(property.name) is None:
            self.__properties.append(property)
            return self

        # 上書き強制
        if overwrite:
            self.removePropertyByName(property.name)
            self.__properties.append(property)
            return self

    def removePropertyByName(self, name):
        self.__properties = list(filter(lambda prop: prop.name != name, self.__properties))

    def getPropertyByName(self, name) -> Union[Property, None]:
        candidates = list(filter(lambda prop: prop.name == name, self.__properties))
        return candidates[0] if len(candidates) > 0 else None
