#
# プロパティ "NICKNAME" (RFC6350 6.2.3.)
#

from typing import Dict, List, Union
from vcflib.properties.Property import Property

class NicknameProperty(Property):

    """
        Class about Property "NICKNAME" (RFC6350 6.2.3).
        It can be include multiple-nicknames and `TYPE` value.
        example of TYPE: "WORK", "HOME", or "INDIVIDUAL".
        (the value of TYPE is handled internally as upper-case.)
    """

    def __init__(self, nicknames: Union[str, List[str]], types: Union[str, List[str], None] = None) -> None:
        # ニックネームをカンマで繋ぐ
        if isinstance(nicknames, str):
            nicknames_ = nicknames
        if isinstance(nicknames, list):
            nicknames_ = "\,".join(nicknames)

        # TYPEパラメータをparamsに突っ込む
        params: Dict[str, Union[str, List[str]]] = {}
        if types is not None:
            if isinstance(types, str):
                params = {"TYPE": types.upper()}
            if isinstance(types, list):
                params = {"TYPE": [type_.upper() for type_ in types]}
        
        super().__init__("NICKNAME", params, nicknames_.encode())

