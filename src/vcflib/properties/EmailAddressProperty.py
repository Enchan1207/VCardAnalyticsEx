#
# プロパティ "EMAIL" (RFC6350 6.4.2.)
#

from typing import Dict, List, Union
from .Property import Property

class EmailAddressProperty(Property):

    """
    プロパティ "EMAIL" (RFC6350 6.4.2) を扱うデータクラス。

    EMAILプロパティは連絡先のメールアドレスに関する情報を提供します。
    このプロパティはvCard内に複数存在することができ、
    パラメータ `PREF` により優先度を定義することができます。
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

