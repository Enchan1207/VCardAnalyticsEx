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
        self.add_property(VersionProperty(version))

    def get_properties(self) -> List[Property]:
        return self.__properties

    def add_property(self, property: Property, overwrite: bool = False):
        # 強制上書きの場合は一旦消す
        if overwrite:
            self.remove_property(property.name)

        # 追加
        self.__properties.append(property)

        return self

    def remove_property(self, name):
        self.__properties = list(filter(lambda prop: prop.name != name, self.__properties))

    def get_property_by_name(self, name) -> Union[Property, None]:
        candidates = list(filter(lambda prop: prop.name == name, self.__properties))
        return candidates[0] if len(candidates) > 0 else None
