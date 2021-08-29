#
# プロパティ "TEL" (RFC6350 6.4.1.)
#

from typing import Dict, List, Union
from .Property import Property

class PhoneNumberProperty(Property):

    """
        Class about Property "TEL" (RFC6350 6.4.1).
    """

    def __init__(self, phone_num: str="", types: Union[str,List[str]] = []) -> None:

        # TYPEパラメータをparamsに突っ込む
        params: Dict[str, Union[str, List[str]]] = {}
        if types is not None:
            if isinstance(types, str):
                params = {"TYPE": types.upper()}
            if isinstance(types, list):
                params = {"TYPE": [type_.upper() for type_ in types]}
        
        super().__init__("TEL", params, phone_num.encode())

