#
# vCardオブジェクト
#
from typing import List, Union
from vcflib.Property import Property

class VCard():

    def __init__(self, properties: List[Property] = []) -> None:
        self.properties: List[Property] = properties

    def getProperty(self, name) -> Union[Property, None]:
        candidates = list(filter(lambda prop: prop.name == name, self.properties))
        return candidates[0] if len(candidates) > 0 else None