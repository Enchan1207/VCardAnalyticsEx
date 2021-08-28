#
# プロパティ "EMAIL" (RFC6350 6.4.2.)
#

from typing import Dict, List, Union
from vcflib.properties.Property import Property

class EmailAddressProperty(Property):

    """
        Class about Property "EMAIL" (RFC6350 6.4.2).
    """

    def __init__(self, addr: str="", types: Union[str,List[str]] = []) -> None:

        # TYPEパラメータをparamsに突っ込む
        params: Dict[str, Union[str, List[str]]] = {}
        if types is not None:
            if isinstance(types, str):
                params = {"TYPE": types.upper()}
            if isinstance(types, list):
                params = {"TYPE": [type_.upper() for type_ in types]}
        
        super().__init__("EMAIL", params, addr.encode())

